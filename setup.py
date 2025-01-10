# Example of your setup.py
from setuptools import setup, find_packages

setup(
    name='music_downloader',
    version='0.2',  # Increment version for changes
    description='A command-line tool to download music tracks from YouTube based on album information retrieved from Wikipedia.',
    author='4rge',
    author_email='4rge@tuta.io',
    url='https://github.com/4rge/AudioFile',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'wikipedia-api',  # Ensure this is the correct package for Wikipedia API
        'yt-dlp',  # Using yt-dlp instead of youtube_dl
        'plyer',  # For desktop notifications
    ],
    entry_points={
        'console_scripts': [
            'music_downloader=music_downloader:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
