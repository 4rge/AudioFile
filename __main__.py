import os
import sys
import urllib.request
import re
import yt_dlp as youtube_dl
from bs4 import BeautifulSoup
import wikipedia
import tempfile
import concurrent.futures
from urllib.parse import quote_plus
from plyer import notification
import shutil

class MusicDownloader:
    def __init__(self):
       # Temporary file for tracklist
        self.tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
        print(f"Temporary file created at: {self.tmp_file.name}")

    def track_search(self, artist, album):
        """Fetch track list from Wikipedia based on artist and album name."""
        try:
            page_url = wikipedia.page(f"{artist} {album}").url
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Disambiguation error: {e}. Please specify a more specific title.")
            return []
        except Exception as e:
            print(f"Could not fetch page: {e}")
            return []

        try:
            soup = BeautifulSoup(urllib.request.urlopen(page_url).read(), 'html.parser')
            tracks = []
            for link in soup.find_all("td"):
                text = link.get_text().strip()
                # Assume track names are wrapped in double quotes
                if text.startswith('"') and text.endswith('"'):
                    tracks.append(text.replace('"', ""))
            print(f"Found tracks: {tracks}")  # Debug print
            return tracks
        except Exception as e:
            print(f"Error parsing the page: {e}")
            return []

    def save_tracks(self, artist, tracks):
        """Save track list to a temporary text file."""
        band_name = artist.replace(" ", "_")  # Replace spaces with underscores for filenames
        
        with open(self.tmp_file.name, "w", encoding="utf-8") as file:
            for track in tracks:
                file.write(f"{track}\n")
        
        print(f"Saved tracks to {self.tmp_file.name}")  # Debug print

    def download_track(self, track, artist, music_dir):
        """Download a single track using yt-dlp."""
        search_query = f"ytsearch:{artist} {track.strip()}"
        try:
            with youtube_dl.YoutubeDL({'format': 'bestaudio/best', 'outtmpl': music_dir + '%(title)s.%(ext)s', 'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]}) as ydl:
                print(f"Searching: {search_query}")  # Debug print
                search_results = ydl.extract_info(search_query, download=True)  # Set download=True to download and extract immediately
                if 'entries' in search_results and len(search_results['entries']) > 0:
                    video_title = search_results['entries'][0]['title']  # Get the discovered title
                    # Find the downloaded file, which is usually named after the title provided
                    downloaded_file_path = os.path.join(music_dir, f"{video_title}.mp3")
                    print(f"Downloaded: {video_title}")

                    # Rename the downloaded file to the discovered video title
                    if os.path.isfile(downloaded_file_path):
                        print(f"Renaming file to: {video_title}.mp3")
                        new_file_path = os.path.join(music_dir, f"{video_title}.mp3")
                        if os.path.exists(new_file_path):
                            print(f"File already exists: {new_file_path}, skipping renaming.")
                        else:
                            shutil.move(downloaded_file_path, new_file_path)  # Rename the file
                    else:
                        print(f"Error: File not found after download: {downloaded_file_path}")
                else:
                    print(f"No results found for: {track.strip()}")
        except Exception as e:
            print(f"Error downloading {track.strip()}: {e}")

    def download_tracks(self, artist):
        """Download tracks with concurrency."""
        band_name = artist.replace(" ", "_")
        track_list_path = self.tmp_file.name

        try:
            with open(track_list_path, "r", encoding="utf-8") as file:
                tracks = file.readlines()
        except FileNotFoundError:
            print(f"Track list file '{track_list_path}' not found. Please ensure you save the tracks first.")
            return

        # Create output directory for music
        music_dir = f"Music/{band_name}/"
        os.makedirs(music_dir, exist_ok=True)

        # Download tracks with concurrency
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = {executor.submit(self.download_track, track, artist, music_dir): track for track in tracks}
            for future in concurrent.futures.as_completed(futures):
                track = futures[future]
                try:
                    future.result()  # This will raise an exception if the download failed
                except Exception as e:
                    print(f"Download failed for {track.strip()}: {e}")

        # Notify user when all downloads are complete
        notification.notify(
            title="Music Downloader",
            message="All downloads are complete!",
            app_name="MusicDownloader",
        )

    def cleanup(self):
        """Remove the temporary file after processing."""
        try:
            os.remove(self.tmp_file.name)
            print(f"Temporary file {self.tmp_file.name} removed.")
        except OSError as e:
            print(f"Error removing temporary file: {e}")

def main():
    print("Welcome to the AudioFile!")
    downloader = MusicDownloader()
    
    artist = input("Enter the artist name: ")
    album = input("Enter the album name: ")

    # Search for tracks and save to file
    tracks = downloader.track_search(artist, album)
    if tracks:
        downloader.save_tracks(artist, tracks)

    download = input("Do you want to download the tracks? (yes/no): ")
    if download.lower() == "yes":
        downloader.download_tracks(artist)

    # Cleanup temporary files after use
    downloader.cleanup()

if __name__ == "__main__":
    main()
