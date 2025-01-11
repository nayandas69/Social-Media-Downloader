import os
import sys
import yt_dlp
import instaloader
import requests
from bs4 import BeautifulSoup
import csv
import time
import shutil
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import logging
import json
from tqdm import tqdm

# ---------------------------------
# Version and Update Variables
# ---------------------------------
CURRENT_VERSION = "1.0.4"
UPDATE_URL = "https://api.github.com/repos/nayandas69/Social-Media-Downloader/releases/latest"
WHATS_NEW_FILE = "whats_new.txt"
GITHUB_REPO_URL = "https://github.com/nayandas69/Social-Media-Downloader"
DISCORD_INVITE = "https://discord.gg/skHyssu"

# ---------------------------------
# Logging Setup
# ---------------------------------
logging.basicConfig(
    filename='downloader.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------------------------------
# Configuration File Setup
# ---------------------------------
config_file = 'config.json'
default_config = {
    "default_format": "show_all",
    "download_directory": "media",
    "history_file": "download_history.csv",
    "mp3_quality": "192",  # Default to 192 kbps
}

def load_config():
    """
    Load the configuration file. Create one if it doesn't exist.
    """
    if not os.path.exists(config_file):
        with open(config_file, 'w') as f:
            json.dump(default_config, f, indent=4)
    with open(config_file, 'r') as f:
        return json.load(f)

config = load_config()
download_directory = config['download_directory']
history_file = config['history_file']
mp3_quality = config['mp3_quality']

# Ensure the download directory exists
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# ---------------------------------
# Author Details Display
# ---------------------------------
def display_author_details():
    """
    Display the author and script details.
    """
    print("\033[1;34m" + "=" * 50 + "\033[0m")
    print("\033[1;32mSocial Media Downloader\033[0m")
    print("\033[1;33mAuthor:\033[0m Nayan Das")
    print("\033[1;33mEmail:\033[0m \033[4;36mnayanchandradas@hotmail.com\033[0m")
    print("\033[1;33mWebsite:\033[0m \033[4;36mhttps://socialportal.nayanchandradas.com\033[0m")
    print("\033[1;33mVersion:\033[0m " + CURRENT_VERSION)
    print("\033[1;34m" + "=" * 50 + "\033[0m\n")
    time.sleep(1)

display_author_details()

# ---------------------------------
# Helper Functions
# ---------------------------------
def check_internet_connection():
    """
    Check if the system has an active internet connection.
    """
    try:
        requests.head("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def log_download(url, status, timestamp=None):
    """
    Log the download status in both history and log file.
    """
    if not timestamp:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(history_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([url, status, timestamp])
    logging.info(f"Download status for {url}: {status}")

def progress_bar(iterable, description="Processing"):
    """
    Wrap iterable with a tqdm progress bar.
    """
    return tqdm(iterable, desc=description, ncols=100, leave=False)

# ---------------------------------
# Update Checker with Discord Invite
# ---------------------------------
def check_for_updates():
    """
    Check for updates, notify about new version, or suggest joining the Discord for development updates.
    """
    if not check_internet_connection():
        print("\nPlease connect to the internet and try again.")
        return

    print(f"Current version: {CURRENT_VERSION}")
    print("Checking for updates...")
    try:
        response = requests.get(UPDATE_URL)
        response.raise_for_status()
        data = response.json()

        latest_version = data.get('tag_name', "Unknown Version")
        if latest_version and latest_version > CURRENT_VERSION:
            print(f"\nNew version available: {latest_version}")

            # Display contents of what's_new.txt
            if os.path.exists(WHATS_NEW_FILE):
                with open(WHATS_NEW_FILE, 'r') as f:
                    print("\nWhat's New in This Version:")
                    print(f.read())
            else:
                print("\nNo 'what's new' information found.")

            confirm = input("\nDo you want to update to the latest version? (y/n): ").strip().lower()
            if confirm == 'y':
                print(f"\nVisit the repository and download the latest version:\n{GITHUB_REPO_URL}")
                print("\nIf you are using pip, run:\n\033[1;32mpip install social-media-downloader --upgrade\033[0m\n")
            else:
                print("\nThe new version includes exciting features and bug fixes.")
                print("You can update anytime at your convenience.")
        else:
            print("No updates available. Thank you!")
            print(f"\nThe new version is under development. Join the Discord server for testing:\n{DISCORD_INVITE}\n")
    except requests.RequestException as e:
        print(f"Error checking for updates: {e}")
        logging.error(f"Update check failed: {e}")

# ---------------------------------
# Internet Connection Check Wrapper
# ---------------------------------
def ensure_internet_connection():
    """
    Ensure that an internet connection is active. Retry until successful.
    """
    while not check_internet_connection():
        print("\nNo internet connection. Please connect to the internet and try again.")
        time.sleep(5)  # Retry every 5 seconds
    print("Internet connection detected. Proceeding...")

# ---------------------------------
# YouTube and TikTok Download
# ---------------------------------
def download_youtube_or_tiktok_video(url):
    ensure_internet_connection()
    """
    Download a YouTube or TikTok video with pause, resume, and quality selection.
    """
    try:
        ydl_opts = {'listformats': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

            # Display video details
            title = info.get('title', 'Unknown Title')
            uploader = info.get('uploader', 'Unknown Uploader')
            upload_date = info.get('upload_date', 'Unknown Date')
            upload_date_formatted = (
                datetime.strptime(upload_date, '%Y%m%d').strftime('%B %d, %Y')
                if upload_date != 'Unknown Date'
                else upload_date
            )
            print("\nVideo Details:")
            print(f"Title: {title}")
            print(f"Uploader: {uploader}")
            print(f"Upload Date: {upload_date_formatted}\n")

            # Display format options
            formats = info['formats']
            print("Available formats:")
            for fmt in formats:
                print(f"ID: {fmt['format_id']} | Ext: {fmt['ext']} | Resolution: {fmt.get('height', 'N/A')}p | Note: {fmt.get('format_note', '')}")

        choice = input("\nEnter the format ID to download (or type 'mp3' for audio-only): ").strip()
        if choice.lower() == 'mp3':
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(download_directory, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': mp3_quality,
                }],
            }
        else:
            ydl_opts = {
                'format': f'{choice}+bestaudio/best',
                'outtmpl': os.path.join(download_directory, '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
                'noprogress': False,
            }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            log_download(url, "Success")
            print(f"\nDownloaded video: {title}.")
    except Exception as e:
        log_download(url, f"Failed: {str(e)}")
        print(f"Error downloading video: {str(e)}")
        logging.error(f"Error downloading video from {url}: {str(e)}")

# ---------------------------------
# Instagram Download (Posts, Videos, Pictures, Reels)
# ---------------------------------
def download_instagram_post(url):
    """Download an Instagram post."""
    try:
        L = instaloader.Instaloader()
        shortcode = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target=download_directory)
        log_download(url, "Success")
        print(f"Downloaded Instagram post from {url}")
    except Exception as e:
        log_download(url, f"Failed: {str(e)}")
        print(f"Error: {str(e)}")
        logging.error(f"Instagram download error for {url}: {str(e)}")

# ---------------------------------
# Facebook Video Download
# ---------------------------------
def download_facebook_video(url, download_directory="media"):
    """
    Download a public Facebook video by extracting the video URL.
    """
    ensure_internet_connection()

    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/91.0.4472.124 Safari/537.36"
            )
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        video_url = None

        # Attempt to find the video URL in multiple ways
        meta_tag = soup.find('meta', property="og:video")
        if meta_tag:
            video_url = meta_tag.get('content')

        # If not found in the meta tag, try alternative attributes
        if not video_url:
            meta_alternate = soup.find('meta', attrs={"name": "twitter:player:stream"})
            if meta_alternate:
                video_url = meta_alternate.get('content')

        if not video_url:
            raise ValueError("Could not extract the video URL. The video might not be public.")

        # Download the video
        video_response = requests.get(video_url, stream=True)
        video_response.raise_for_status()

        file_path = os.path.join(download_directory, 'facebook_video.mp4')
        with open(file_path, 'wb') as f:
            for chunk in progress_bar(video_response.iter_content(chunk_size=8192), description="Downloading"):
                if chunk:
                    f.write(chunk)

        print(f"Downloaded Facebook video to {file_path}.")
        logging.info(f"Successfully downloaded Facebook video from {url} to {file_path}.")
    except Exception as e:
        logging.error(f"Error downloading Facebook video from {url}: {e}")
        print(f"Error: {e}")

# ---------------------------------
# Unified Media Downloader Function
# ---------------------------------
def download_media(url):
    """Download media based on the platform."""
    if "youtube.com" in url or "tiktok.com" in url:
        download_youtube_or_tiktok_video(url)
    elif "instagram.com" in url:
        download_instagram_post(url)
    elif "facebook.com" in url:
        download_facebook_video(url)
    else:
        print(f"Unsupported platform for URL: {url}")
        log_download(url, "Unsupported platform")

# ---------------------------------
# Batch Download
# ---------------------------------
def batch_download(urls):
    ensure_internet_connection()
    """Download multiple URLs from a list."""
    print("Starting batch download...")
    with ThreadPoolExecutor() as executor:
        list(progress_bar(executor.map(download_media, urls), description="Batch Download"))

# ---------------------------------
# Help Menu
# ---------------------------------
def show_help():
    """Display the help menu."""
    print("\n\033[1;36mHow to Use Social Media Downloader:\033[0m")
    print("1. YouTube/TikTok Download: Enter '1' to download a YouTube or TikTok video.")
    print("2. Facebook Download: Enter '2' to download a Facebook video.")
    print("3. Instagram Download: Enter '3' to download an Instagram post, video, picture, or reel.")
    print("4. Batch Download: Enter '4' and provide a text file with URLs.")
    print("5. Update Checker: Enter '5' to check and apply updates.")
    print("6. Help: Enter '6' to show this help menu.")
    print("7. Quit: Enter '7' to exit the program.\n")
    print("All downloads are saved in the 'media' directory.")
    print("Logs and download history are maintained for your convenience.")
    print("For issues or suggestions, please contact the author:")
    display_author_details()

# ---------------------------------
# Main Function: CLI Interface
# ---------------------------------
def main():
    """Main function for user interaction."""
    print("Welcome to Social Media Downloader!")
    while True:
        print("\nAvailable Options:")
        print("1. Download YouTube/TikTok Video")
        print("2. Download Facebook Video")
        print("3. Download Instagram Post")
        print("4. Batch Download")
        print("5. Check for Updates")
        print("6. Help")
        print("7. Quit")

        choice = input("\nEnter your choice: ").strip().lower()
        if choice == "1":
            url = input("Enter the video URL: ").strip()
            if not url:
                print("URL cannot be empty. Please try again.")
                continue
            download_youtube_or_tiktok_video(url)
        elif choice == "2":
            url = input("Enter the Facebook video URL: ").strip()
            if not url:
                print("URL cannot be empty. Please try again.")
                continue
            download_facebook_video(url)
        elif choice == "3":
            url = input("Enter the Instagram post URL: ").strip()
            if not url:
                print("URL cannot be empty. Please try again.")
                continue
            download_instagram_post(url)
        elif choice == "4":
            file_path = input("Enter the path to the text file with URLs: ").strip()
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    urls = file.read().splitlines()
                batch_download(urls)
            else:
                print("File not found. Please provide a valid file path.")
        elif choice == "5":
            check_for_updates()
        elif choice == "6":
            show_help()
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
