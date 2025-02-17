import os
import sys
import csv
import time
import json
import shutil
import yt_dlp
import logging
import requests
import instaloader
from tqdm import tqdm
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


# ---------------------------------
# Version and Update Variables
# ---------------------------------
AUTHOR = "Nayan Das"
CURRENT_VERSION = "1.0.7"
EMAIL = "nayanchandradas@hotmail.com"
DISCORD_INVITE = "https://discord.gg/skHyssu"
WEBSITE = "https://socialportal.nayanchandradas.com"
GITHUB_REPO_URL = "https://github.com/nayandas69/Social-Media-Downloader"
UPDATE_URL = (
    "https://api.github.com/repos/nayandas69/Social-Media-Downloader/releases/latest"
)


# ---------------------------------
# Author Details Display
# ---------------------------------
def display_author_details():
    """Display the author details in a clean format."""
    print("\n\033[1;34m" + "═" * 60 + "\033[0m")
    print("\033[1;32m      SOCIAL MEDIA DOWNLOADER      \033[0m")
    print("\033[1;34m" + "═" * 60 + "\033[0m")
    print(f"\033[1;33m  Author   :\033[0m {AUTHOR}")
    print(f"\033[1;33m  Email    :\033[0m \033[4;36m{EMAIL}\033[0m")
    print(f"\033[1;33m  Website  :\033[0m \033[4;36m{WEBSITE}\033[0m")
    print(f"\033[1;33m  Version  :\033[0m {CURRENT_VERSION}")
    print("\033[1;34m" + "═" * 60 + "\033[0m\n")
    time.sleep(1)


display_author_details()


# ---------------------------------
# Logging Setup
# ---------------------------------
logging.basicConfig(
    filename="downloader.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# ---------------------------------
# Load Configuration
# ---------------------------------
CONFIG_FILE = "config.json"
DEFAULT_CONFIG = {
    "default_format": "show_all",
    "download_directory": "media",
    "history_file": "download_history.csv",
    "mp3_quality": "192",
}


def load_config():
    """Load or create configuration file safely."""
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)

    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        logging.error("Invalid config file. Resetting to defaults.")
        with open(CONFIG_FILE, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG


config = load_config()
download_directory = config["download_directory"]
history_file = config["history_file"]
mp3_quality = config["mp3_quality"]

os.makedirs(download_directory, exist_ok=True)  # Ensure download directory exists


# ---------------------------------
# Check for Updates
# ---------------------------------
def check_for_updates():
    """Check for updates and notify users."""
    if not check_internet_connection():
        print("\nNo internet connection. Please connect and try again.")
        return

    print(f"\nChecking for updates... (Current version: {CURRENT_VERSION})")

    try:
        response = requests.get(UPDATE_URL)
        response.raise_for_status()
        data = response.json()

        latest_version = data.get("tag_name", "Unknown Version").strip()

        if latest_version > CURRENT_VERSION:
            print(f"\n New version available: {latest_version}")
            print("\nDownload here:")
            print(f"{GITHUB_REPO_URL}")

            print("\nIf using pip, run:")
            print("\033[1;32mpip install social-media-downloader --upgrade\033[0m\n")
        else:
            print("\n No updates available. You're up to date!")
            print(f"\nJoin Discord for testing:\n{DISCORD_INVITE}\n")

    except requests.RequestException as e:
        print(f"\n Error checking for updates: {e}")
        logging.error(f"Update check failed: {e}")


# ---------------------------------
# Utility Functions
# ---------------------------------
def check_internet_connection():
    """Check if the system has an active internet connection."""
    try:
        requests.head("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False


def ensure_internet_connection():
    """Ensure that an internet connection is active before proceeding."""
    while not check_internet_connection():
        print("\nNo internet connection. Retrying in 5 seconds...")
        time.sleep(5)
    print("Internet connection detected. Proceeding...")


def log_download(url, status):
    """Log the download status in history and log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(history_file, "a+", newline="") as f:
        csv.writer(f).writerow([url, status, timestamp])
    logging.info(f"Download status for {url}: {status}")


def get_unique_filename(filename):
    """Ensure downloaded files are renamed if duplicates exist."""
    base, ext = os.path.splitext(filename)
    counter = 1
    while os.path.exists(filename):
        filename = f"{base} ({counter}){ext}"
        counter += 1
    return filename


# ----------------------------------------
# Download Functions for Youtube & TikTok
# ----------------------------------------
def download_youtube_or_tiktok_video(url):
    """Download a YouTube or TikTok video with user-selected format (ensuring video has audio)."""
    ensure_internet_connection()
    try:
        ydl_opts = {"listformats": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        # Extract video details
        title = info.get("title", "Unknown Title")
        uploader = info.get("uploader", "Unknown Uploader")
        upload_date = info.get("upload_date", "Unknown Date")
        upload_date_formatted = (
            datetime.strptime(upload_date, "%Y%m%d").strftime("%B %d, %Y")
            if upload_date != "Unknown Date"
            else upload_date
        )

        # Display video details
        print("\n\033[1;36mVideo Details:\033[0m")
        print(f"\033[1;33mTitle:\033[0m {title}")
        print(f"\033[1;33mUploader:\033[0m {uploader}")
        print(f"\033[1;33mUpload Date:\033[0m {upload_date_formatted}")

        # List available formats
        print("\nAvailable formats:")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.list_formats(info)

        # Prompt user for format choice
        choice = input(
            "\nEnter the format ID to download (or type 'mp3' for audio-only): "
        ).strip()

        filename = get_unique_filename(os.path.join(download_directory, f"{title}.mp4"))

        # Prepare download options
        if choice.lower() == "mp3":
            ydl_opts = {
                "format": "bestaudio/best",
                "outtmpl": os.path.join(download_directory, f"{title}.mp3"),
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    },
                ],
            }
        else:
            ydl_opts = {
                "format": f"{choice}+bestaudio/best",
                "outtmpl": filename,
                "merge_output_format": "mp4",
            }

        # Download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            log_download(url, "Success")
            print(f"\n\033[1;32mDownloaded successfully:\033[0m {title}")

    except Exception as e:
        log_download(url, f"Failed: {str(e)}")
        logging.error(f"Error downloading video from {url}: {str(e)}")
        print(f"\033[1;31mError downloading video:\033[0m {str(e)}")


# --------------------------------
# Download Functions for Instagram
# --------------------------------
def download_instagram_post(url):
    """Download an Instagram post."""
    ensure_internet_connection()
    try:
        L = instaloader.Instaloader()
        shortcode = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target=download_directory)
        log_download(url, "Success")
        print(f"Downloaded Instagram post from {url}")
    except Exception as e:
        log_download(url, f"Failed: {str(e)}")
        logging.error(f"Instagram download error for {url}: {str(e)}")


# -------------------------------
# Download Functions for Facebook
# -------------------------------
def download_facebook_video(url):
    """Download a Facebook video."""
    ensure_internet_connection()
    try:
        ydl_opts = {
            "format": "best",
            "outtmpl": os.path.join(download_directory, "%(title)s.%(ext)s"),
            "continue_dl": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            log_download(url, "Success")
            print(f"Downloaded Facebook video from {url}")
    except Exception as e:
        log_download(url, f"Failed: {str(e)}")
        logging.error(f"Facebook download error for {url}: {str(e)}")


# -------------------------
# Batch Download Instagram
# -------------------------
def batch_download_from_file(file_path):
    """Read URLs from a text file and download them concurrently."""
    print(f"Reading URLs from {file_path}...")

    # Read all lines and clean up empty lines
    with open(file_path, "r") as file:
        urls = [line.strip() for line in file.readlines() if line.strip()]

    if not urls:
        print("No URLs found in the file.")
        return

    print("Starting batch download...")

    with ThreadPoolExecutor() as executor:
        list(
            tqdm(
                executor.map(download_instagram_post, urls),
                total=len(urls),
                desc="Instagram Batch",
            )
        )

    print("Download complete.")


# ---------------------------------
# Help Menu
# ---------------------------------
def show_help():
    """Display the help menu with usage instructions."""
    print("\n\033[1;36mHow to Use Social Media Downloader:\033[0m")
    print(
        "1. \033[1;33mDownload YouTube/TikTok Videos:\033[0m Enter '1' to download a public YouTube or TikTok video."
    )
    print(
        "2. \033[1;33mDownload Facebook Videos:\033[0m Enter '2' to download a public Facebook video."
    )
    print(
        "3. \033[1;33mDownload Instagram Content:\033[0m Enter '3' to download a public Instagram post, video, reel, or picture."
    )
    print(
        "4. \033[1;33mBatch Download Instagram Posts:\033[0m Enter '4' and provide a text file containing public Instagram post URLs."
    )
    print(
        "5. \033[1;33mCheck for Updates:\033[0m Enter '5' to check for software updates and install the latest version."
    )
    print("6. \033[1;33mHelp Menu:\033[0m Enter '6' to display this help guide.")
    print("7. \033[1;33mExit the Program:\033[0m Enter '7' to close the application.\n")

    print("\033[1;31mImportant Notice:\033[0m")
    print("\033[1;31mThis tool only supports downloading public videos.\033[0m")
    print(
        "\033[1;31mPrivate, restricted, or non-public content cannot be downloaded.\033[0m\n"
    )

    print("\033[1;32mAdditional Information:\033[0m")
    print("• All downloaded files are saved in the 'media' directory.")
    print("• Download history and logs are automatically recorded for reference.")
    print(
        "• For support, feature requests, or bug reports, please contact the author below:\n"
    )

    display_author_details()


# ---------------------------------
# Main Function: CLI Interface
# ---------------------------------
def main():
    """Main function for user interaction."""
    try:
        input(
            "\nPress Enter to start the Social Media Downloader..."
        )  # Wait for user input before execution
        print("Welcome to Social Media Downloader!")

        while True:
            print("\n" + "─" * 60)
            print("\n1. Download YouTube/TikTok")
            print("2. Download Facebook")
            print("3. Download Instagram")
            print("4. Instagram Batch Download")
            print("5. Check for updates")
            print("6. Help")
            print("7. Exit")

            choice = input("\nEnter your choice: ").strip()
            if not choice:
                continue  # skip empty input

            if choice == "1":
                url = input("Enter the YouTube/TikTok video URL: ").strip()
                download_youtube_or_tiktok_video(url)
            elif choice == "2":
                url = input("Enter the Facebook video URL: ").strip()
                download_facebook_video(url)
            elif choice == "3":
                url = input("Enter the Instagram post URL: ").strip()
                download_instagram_post(url)
            elif choice == "4":
                file_path = input("Enter the path to your .txt file: ").strip()
                batch_download_from_file(file_path)
            elif choice == "5":
                check_for_updates()
            elif choice == "6":
                show_help()
            elif choice == "7":
                print(
                    "\nSocial Media Downloader has exited successfully. Thank you for using it!\n"
                )

                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        logging.critical(f"Unexpected error: {e}", exc_info=True)
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
