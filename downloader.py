# -----------------------------------------
# Social Media Downloader
# Version: 1.1.0
# Author: Nayan Das
# License: MIT
# Description: A command-line tool to download videos from various social media platforms like YouTube, TikTok, Facebook, Instagram, X, Twitch, Snapchat, Reddit, Vimeo & Streamable.
# It supports instagram batch downloads, format selection, and maintains a download history.
# Dependencies: yt-dlp, instaloader, requests, tqdm, pyfiglet, termcolor
# Usage: pip install social-media-downloader
# Requirements: Python 3.6+
# Note: Ensure FFmpeg is installed and added to your PATH for audio extraction.
# -----------------------------------------

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
from pyfiglet import Figlet
from termcolor import colored
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


# ---------------------------------
# Version and Update Variables
# ---------------------------------
AUTHOR = "Nayan Das"
CURRENT_VERSION = "1.1.0"
EMAIL = "nayanchandradas@hotmail.com"
DISCORD_INVITE = "https://discord.gg/skHyssu"
WEBSITE = "https://nayandas69.github.io/link-in-bio"
GITHUB_REPO_URL = "https://github.com/nayandas69/Social-Media-Downloader"
UPDATE_URL = (
    "https://api.github.com/repos/nayandas69/Social-Media-Downloader/releases/latest"
)


# ---------------------------------
# Author Details Display
# ---------------------------------
def display_author_details():
    """Display the animated banner and author details."""

    # Clear screen
    os.system("cls" if os.name == "nt" else "clear")

    # Fancy fonts
    banner_font = Figlet(font="slant")

    # Render text
    banner_text = banner_font.renderText("Social Media Downloader")

    # Color them
    banner_colored = colored(banner_text, "cyan", attrs=["bold"])

    # Animate banner
    for line in banner_colored.splitlines():
        print(line)
        time.sleep(0.05)

    print("\n")

    # Author Info Animated
    info_lines = [
        (f"Author   : ", AUTHOR, "yellow", "white"),
        (f"Email    : ", EMAIL, "yellow", "cyan"),
        (f"Discord  : ", DISCORD_INVITE, "yellow", "cyan"),
        (f"Repo     : ", GITHUB_REPO_URL, "yellow", "cyan"),
        (f"Website  : ", WEBSITE, "yellow", "cyan"),
        (f"Version  : ", CURRENT_VERSION, "yellow", "green"),
    ]

    for label, value, label_color, value_color in info_lines:
        print(
            colored(f"{label:<10}", label_color, attrs=["bold"])
            + colored(value, value_color)
        )
        time.sleep(0.2)

    # Loader animation
    print(colored("\nLoading", "yellow", attrs=["bold"]), end="", flush=True)
    for _ in range(5):
        time.sleep(0.4)
        print(colored(".", "yellow", attrs=["bold"]), end="", flush=True)

    time.sleep(0.5)

    print()  # Final line break


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
# Check for FFmpeg
# ---------------------------------
def ensure_ffmpeg():
    """Ensure that FFmpeg is installed before proceeding."""
    if shutil.which("ffmpeg") is None:
        print(
            "\033[1;31m\nFFmpeg is not installed. Please install FFmpeg and try again.\033[0m"
        )
        print("\033[1;31mDownload FFmpeg from: https://ffmpeg.org/download.html\033[0m")
        print("\033[1;31mFor Windows users, add FFmpeg to your PATH.\033[0m")
        print("\033[1;31mFor Linux users, run: sudo apt install ffmpeg\033[0m")
        print("\033[1;31mAfter installation, restart the program.\033[0m")
        sys.exit(1)
    else:
        print("\033[1;32mFFmpeg is installed. Proceeding...\033[0m")


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
            print(f"\nNew version available: {latest_version}")
            print("\nDownload here:")
            print(f"{GITHUB_REPO_URL}")

            print("\nIf using pip, run:")
            print("\033[1;32mpip install social-media-downloader --upgrade\033[0m\n")
        else:
            print("\nNo updates available. You're up to date!")
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


# -------------------------------------
# Validate URLs for Supported Platforms
# -------------------------------------
def is_valid_platform_url(url, allowed_domains):
    """Check if the URL matches one of the allowed domains."""
    return any(domain in url for domain in allowed_domains)


# -----------------------------------------------------------
# Download Functions for Youtube, TikTok and other platforms
# -----------------------------------------------------------
def download_youtube_or_tiktok_video(url):
    """Download a video with user-selected format (ensuring video has audio)."""

    allowed_domains = [
        "youtube.com",
        "youtu.be",
        "tiktok.com",
        "facebook.com",
        "fb.watch",
        "x.com",
        "twitter.com",
        "twitch.tv",
        "clips.twitch.tv",
        "snapchat.com",
        "reddit.com",
        "packaged-media.redd.it",
        "vimeo.com",
        "streamable.com",
    ]
    if not is_valid_platform_url(url, allowed_domains):
        print("\n\033[1;31mInvalid URL. Please enter a valid URL.\033[0m")
        print(
            "\033[1;31mSupported platforms: YouTube, TikTok, X (Tweeter), Twitch, Snapchat, Vimeo & Streamable.\033[0m"
        )
        return

    ensure_ffmpeg()
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


# ----------------------------------------------------------------------------
# Download Functions for Instagram public posts, videos, reels, and pictures
# ----------------------------------------------------------------------------
def download_instagram_post(url):
    """Download an Instagram post."""
    allowed_domains = ["instagram.com"]
    if not is_valid_platform_url(url, allowed_domains):
        print("\n\033[1;31mInvalid URL. Please enter a valid Instagram URL.\033[0m")
        return
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


# -------------------------
# Batch Download Instagram
# -------------------------
def batch_download_from_file(file_path):
    """Read URLs from a text file and download them concurrently."""
    ensure_internet_connection()
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


# --------------------------------
# Help Menu
# --------------------------------
def show_help():
    """Display the help menu with usage instructions."""
    print("\n\033[1;36mHow to Use Social Media Downloader:\033[0m")
    print(
        "1. \033[1;33mDownload Videos:\033[0m Enter '1' to download a public YouTube, TikTok, Facebook, X, Twitch, Snapchat, Reddit, Vimeo, Streamable videos."
    )
    print(
        "2. \033[1;33mDownload Instagram Content:\033[0m Enter '2' to download a public Instagram post, video, reel, or picture."
    )
    print(
        "3. \033[1;33mBatch Download Instagram Posts:\033[0m Enter '3' and provide a text file containing public Instagram post URLs."
    )
    print(
        "4. \033[1;33mCheck for Updates:\033[0m Enter '4' to check for software updates and install the latest version."
    )
    print("5. \033[1;33mHelp Menu:\033[0m Enter '5' to display this help guide.")
    print("6. \033[1;33mExit the Program:\033[0m Enter '6' to close the application.\n")

    print("\033[1;31mImportant Notice:\033[0m")
    print("\033[1;31mThis tool only supports downloading public videos.\033[0m")
    print(
        "\033[1;31mPrivate, restricted, or non-public content cannot be downloaded.\033[0m\n"
    )
    print("\033[1;32mSupported Platforms:\033[0m")
    print(
        "• YouTube, TikTok, Facebook, Instagram, X (Twitter), Twitch, Snapchat, Reddit, Vimeo & Streamable.\n"
    )

    print("\033[1;32mAdditional Information:\033[0m")
    print("• All downloaded files are saved in the 'media' directory.")
    print("• Download history and logs are automatically recorded for reference.")
    print(
        "• For support, feature requests, or bug reports, please contact the author below:\n"
    )
    print(f"\033[1;33mEmail: {EMAIL}\033[0m")
    print(f"\033[1;33mDiscord: {DISCORD_INVITE}\033[0m")
    print(f"\033[1;33mGitHub: {GITHUB_REPO_URL}\033[0m")
    print(f"\033[1;33mWebsite: {WEBSITE}\033[0m")


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
            print("\n1. Download YouTube/TikTok... etc.")
            print("2. Download Instagram")
            print("3. Instagram Batch Download")
            print("4. Check for updates")
            print("5. Help")
            print("6. Exit")

            choice = input("\nEnter your choice: ").strip()
            if not choice:
                continue  # skip empty input

            if choice == "1":
                url = input("Enter video URL: ").strip()
                download_youtube_or_tiktok_video(url)
            elif choice == "2":
                url = input("Enter the Instagram URL: ").strip()
                download_instagram_post(url)
            elif choice == "3":
                file_path = input(
                    "Enter the path to the text file containing Instagram URLs: "
                ).strip()
                if os.path.exists(file_path):
                    batch_download_from_file(file_path)
                else:
                    print(f"File not found: {file_path}")
                    print(f"\nFor example: /home/user/batch_links.txt")
            elif choice == "4":
                check_for_updates()
            elif choice == "5":
                show_help()
            elif choice == "6":
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
