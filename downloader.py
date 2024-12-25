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
from subprocess import Popen
import logging
import json
from tqdm import tqdm

# ---------------------------------
# Version and Update Variables
# ---------------------------------
CURRENT_VERSION = "1.0.0"
UPDATE_URL = "https://api.github.com/repos/nayandas69/Social-Media-Downloader/releases/latest"
WHATS_NEW_FILE = "whats_new.txt"

# ---------------------------------
# Logging Setup
# ---------------------------------
logging.basicConfig(
    filename='downloader.log',  # Log file to record events
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------------------------------
# Configuration File Setup
# ---------------------------------
config_file = 'config.json'
default_config = {
    "default_format": "show_all",  # Default format behavior
    "download_directory": "media",  # Default download directory
    "history_file": "download_history.csv"  # Default history file
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
def is_windows():
    """Check if the operating system is Windows."""
    return sys.platform.startswith('win')

def is_linux():
    """Check if the operating system is Linux."""
    return sys.platform.startswith('linux')

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
# Check for updates functionality
# ---------------------------------
def check_for_updates():
    """
    Check for and apply updates if a newer version is available.
    """
    print(f"Current version: {CURRENT_VERSION}")
    print("Checking for updates...")
    try:
        response = requests.get(UPDATE_URL)
        response.raise_for_status()
        data = response.json()

        latest_version = data.get('tag_name')
        download_link = None
        if 'assets' in data and data['assets']:
            for asset in data['assets']:
                if is_linux() and 'linux' in asset['name'].lower():
                    download_link = asset.get('browser_download_url')
                    break
                elif is_windows() and asset['name'].lower().endswith('.exe'):
                    download_link = asset.get('browser_download_url')

        if latest_version:
            if latest_version > CURRENT_VERSION:
                print(f"\nNew version available: {latest_version}")
                print(f"Current version: {CURRENT_VERSION}")

                # Display contents of whats_new.txt if available
                print("\n\033[1;34mWhat's New in This Version:\033[0m")
                if os.path.exists(WHATS_NEW_FILE):
                    try:
                        with open(WHATS_NEW_FILE, 'r') as file:
                            whats_new = file.read()
                            print(whats_new)
                    except Exception as e:
                        print(f"Could not read 'whats_new.txt': {e}")
                        logging.warning(f"Failed to read 'whats_new.txt': {str(e)}")
                else:
                    print("No 'what's new' information found.")

                # Prompt user for confirmation
                confirm = input("\nDo you want to update to the latest version? (y/n): ")
                if confirm.lower() == 'y':
                    download_update(download_link, latest_version)
                else:
                    print("You can update anytime when you want.\n")
            else:
                print("You are already using the latest version.\n")
        else:
            print("Error: Could not retrieve the latest version information.")
    except requests.RequestException as e:
        print(f"Error checking for updates: {str(e)}")
        logging.error(f"Update check failed: {str(e)}")

def download_update(download_link, latest_version):
    """
    Download and apply updates.
    """
    if not download_link:
        print("Error: No download link available for the update.")
        return

    print("Downloading update...")
    update_file = "SocialMediaDownloader_latest"
    if is_windows():
        update_file += ".exe"

    try:
        response = requests.get(download_link, stream=True)
        with open(update_file, 'wb') as file:
            for chunk in progress_bar(response.iter_content(chunk_size=8192), description="Downloading"):
                file.write(chunk)

        print("Update downloaded successfully.")
        old_exe = sys.argv[0]
        new_exe = os.path.abspath(update_file)
        shutil.move(new_exe, old_exe)
        print("Old version replaced with the updated version.")
        print("Restarting with the latest version...\n")
        time.sleep(2)
        if is_windows():
            Popen([old_exe])
        else:
            os.chmod(old_exe, 0o755)
            Popen(["./" + old_exe])
        sys.exit()
    except Exception as e:
        print(f"Failed to update: {str(e)}")
        logging.error(f"Update failed: {str(e)}")

# ---------------------------------
# YouTube and TikTok download with format selection
# ---------------------------------
def download_youtube_or_tiktok_video(url):
    """
    Download a YouTube or TikTok video with format selection or MP3 option.
    """
    try:
        ydl_opts = {'listformats': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info['formats']
            print("\nAvailable formats:")
            for i, format in enumerate(formats):
                format_id = format['format_id']
                ext = format['ext']
                height = format.get('height', 'Unknown')
                fps = format.get('fps', 'Unknown')
                vcodec = format.get('vcodec', 'none')
                acodec = format.get('acodec', 'none')
                format_note = format.get('format_note', '')
                print(f"{i + 1}. {format_id} - {ext} - {height}p - {fps}fps - {vcodec} - {acodec} - {format_note}")

        choice = input("\nEnter the format ID to download (or type 'mp3' for best audio): ").strip()
        if choice.lower() == 'mp3':
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(download_directory, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        else:
            ydl_opts = {
                'format': f'{choice}+bestaudio/best',
                'merge_output_format': 'mp4',
                'outtmpl': os.path.join(download_directory, '%(title)s.%(ext)s'),
            }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            title = info.get("title", "video")
            log_download(url, "Success")
            print(f"\nDownloaded video: {title}.")
    except Exception as e:
        log_download(url, f"Failed: {str(e)}")
        print(f"Error downloading video: {str(e)}")
        logging.error(f"Error downloading video: {url} - {str(e)}")

# ---------------------------------
# Instagram post download
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
# Facebook post download using BeautifulSoup to find video link
# ---------------------------------
def download_facebook_video(url):
    """Download a Facebook video."""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        video_url = soup.find('meta', property="og:video")['content']
        if video_url:
            video_response = requests.get(video_url)
            file_path = os.path.join(download_directory, 'facebook_video.mp4')
            with open(file_path, 'wb') as f:
                for chunk in progress_bar(video_response.iter_content(chunk_size=8192), description="Downloading"):
                    f.write(chunk)
            log_download(url, "Success")
            print("Downloaded Facebook video.")
        else:
            raise ValueError("Could not find video URL")
    except Exception as e:
        log_download(url, f"Failed: {str(e)}")
        print(f"Error: {str(e)}")
        logging.error(f"Facebook download error for {url}: {str(e)}")

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
    print("3. Instagram Download: Enter '3' to download an Instagram post.")
    print("4. Batch Download: Enter '4' and provide a text file with URLs.")
    print("5. Update Checker: Enter '5' to check and apply updates.")
    print("6. Help: Enter '6' to show this help menu.")
    print("7. Quit: Enter '7' to exit the program.\n")
    print("\nAll downloads are saved in the 'media' directory, and a log is saved in 'download_history.csv'.")
    print("If you encounter any issues, crashes, bugs, or have new feature requests, please contact the author:")
    display_author_details()

# ---------------------------------
# Main Function CLI interface for the Social Media Downloader
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
            download_youtube_or_tiktok_video(url)
        elif choice == "2":
            url = input("Enter the Facebook video URL: ").strip()
            download_facebook_video(url)
        elif choice == "3":
            url = input("Enter the Instagram post URL: ").strip()
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
            continue  # Skip the "Download complete!" message for help
        elif choice in {"7", "q"}:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
