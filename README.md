# YT_to_mp3
This is a Python script that extracts audio from YouTube videos and saves it as an MP3 file. This script uses the `yt-dlp` library (a maintained fork of youtube-dl) along with `ffmpeg` for audio processing.I've created a Python script that can extract audio from YouTube videos and save them as MP3 files. Here's what the script does:

## Features:
- **URL Validation**: Checks if the provided URL is a valid YouTube link
- **Audio Extraction**: Downloads the best available audio quality and converts it to MP3 (192 kbps)
- **Clean Filenames**: Sanitizes video titles to create valid filenames
- **Progress Display**: Shows download progress and video information
- **Error Handling**: Gracefully handles errors and invalid inputs
- **Batch Processing**: Allows downloading multiple videos in one session

## Prerequisites:
Before running the script, you'll need to install:

1. **yt-dlp** (the main library):
   ```bash
   pip install yt-dlp
   ```

2. **ffmpeg** (for audio conversion):
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
   - **Mac**: `brew install ffmpeg`
   - **Linux**: `sudo apt-get install ffmpeg` (Ubuntu/Debian) or `sudo yum install ffmpeg` (RHEL/CentOS)

## How to Use:
1. Save the script as `youtube_to_mp3.py`
2. Run it: `python youtube_to_mp3.py`
3. Paste a YouTube URL when prompted
4. The MP3 file will be saved in the `downloads` folder (or a custom folder you specify)

## Important Notes:
- This tool should only be used to download content that you have permission to download
- Respect copyright laws and YouTube's Terms of Service
- Some videos may have download restrictions
- The script downloads at 192 kbps quality by default (you can modify the `preferredquality` parameter for different bitrates)
