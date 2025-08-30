#!/usr/bin/env python3
"""
YouTube to MP3 Extractor
This script downloads audio from YouTube videos and converts them to MP3 format.
"""

import os
import sys
import re
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("Error: yt-dlp is not installed.")
    print("Please install it using: pip install yt-dlp")
    sys.exit(1)

def validate_youtube_url(url):
    """
    Validate if the provided URL is a valid YouTube URL.
    """
    youtube_regex = (
        r'(https?://)?(www\.)?'
        r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    )
    
    youtube_pattern = re.compile(youtube_regex)
    match = youtube_pattern.match(url)
    
    return match is not None

def sanitize_filename(filename):
    """
    Remove invalid characters from filename.
    """
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '')
    return filename.strip()

def download_audio(url, output_path="downloads"):
    """
    Download audio from YouTube video and convert to MP3.
    
    Args:
        url: YouTube video URL
        output_path: Directory to save the MP3 file
    """
    # Create output directory if it doesn't exist
    Path(output_path).mkdir(parents=True, exist_ok=True)
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
        'extract_flat': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\nFetching video information...")
            
            # Extract video info
            info = ydl.extract_info(url, download=False)
            video_title = sanitize_filename(info.get('title', 'Unknown'))
            duration = info.get('duration', 0)
            
            print(f"Video Title: {video_title}")
            print(f"Duration: {duration // 60}:{duration % 60:02d}")
            print(f"\nDownloading and converting to MP3...")
            
            # Download and convert
            ydl.download([url])
            
            output_file = os.path.join(output_path, f"{video_title}.mp3")
            print(f"\n✅ Successfully saved as: {output_file}")
            
            return True
            
    except yt_dlp.utils.DownloadError as e:
        print(f"\n❌ Download error: {str(e)}")
        return False
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        return False

def main():
    """
    Main function to run the YouTube to MP3 converter.
    """
    print("=" * 50)
    print("YouTube to MP3 Converter")
    print("=" * 50)
    
    while True:
        print("\nEnter a YouTube video URL (or 'quit' to exit):")
        url = input("> ").strip()
        
        if url.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye!")
            break
        
        if not url:
            print("Please enter a valid URL.")
            continue
        
        if not validate_youtube_url(url):
            print("❌ Invalid YouTube URL. Please try again.")
            continue
        
        # Ask for custom output directory (optional)
        print("\nEnter output directory (press Enter for 'downloads'):")
        output_dir = input("> ").strip()
        if not output_dir:
            output_dir = "downloads"
        
        # Download the audio
        success = download_audio(url, output_dir)
        
        if success:
            print("\nWould you like to download another video? (yes/no)")
            choice = input("> ").strip().lower()
            if choice not in ['yes', 'y']:
                print("\nGoodbye!")
                break
        else:
            print("\nWould you like to try again? (yes/no)")
            choice = input("> ").strip().lower()
            if choice not in ['yes', 'y']:
                print("\nGoodbye!")
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
