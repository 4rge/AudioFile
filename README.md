# AudioFile

A CLI tool that allows users to download music tracks from an album by an artist. The application fetches the track list from Wikipedia and uses `yt-dlp` to download the audio files in MP3 format.
**Note**:A previous iteration of this tool is archived in .Pyrate.

## Features

- Fetches album track lists directly from Wikipedia.
- Downloads tracks concurrently for faster processing.
- Saves the track list to a temporary file.
- Notifies users upon completion of downloads.

## Requirements

- Python 3.x
- `yt-dlp` for downloading media
- `beautifulsoup4` for scraping HTML
- `pyWikipedia` for fetching Wikipedia pages
- `plyer` for sending notifications

You can install the required packages via pip:

```pip install yt-dlp beautifulsoup4 wikipedia-api plyer```

## Setup

The scripts provided `make_venv.py` and `setup.py` setup and download all requirements to a virtual environment in the cloned folder.

- First `git clone` this repo and `cd` into the directory.
- Run `python3 make_venv.py` to setup a virtual environment.
- You will be prompted to run `sudo python3 setup.py install`.

Afterward you can continue to usege.

## Usage

**Run the script**:
```python audiofile.py```

Follow the prompts to enter the artist name and album title.
Choose whether to download the tracks after they have been fetched.

#### Example:
`Welcome to AudioFile CLI!
Enter the artist name: The Beatles
Enter the album name: Abbey Road
Found tracks: ['Come Together', 'Something', 'Maxwell\'s Silver Hammer', ...]
Do you want to download the tracks? (yes/no): yes`

## Directory Structure

Downloaded tracks will be saved in the Music/{artist_name}/ directory, where {artist_name} is the name of the artist you specify.

## Cleaning Up

The application creates a temporary file to store the track list, which is automatically removed after the download completes.

## Handling Errors

The application handles various exceptions, such as:
Disambiguation errors when fetching Wikipedia pages
File IO errors when saving tracks or renaming downloaded files
Errors during the downloading process

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contribution

Contributions are welcome! Please feel free to open issues or submit pull requests.

## Acknowledgments

`yt-dlp` for the media downloading capabilities.
`Wikipedia` for providing the album information.
`Beautiful Soup` for HTML parsing.

**Note**: It is your responsibility to use this tool only to download from authorized sources. I do not take any responsibility for your misuse of a theoretical demonstration.
