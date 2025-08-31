#!/usr/bin/env python3
"""
Social Media Downloader - A comprehensive CLI tool for downloading videos from various platforms.

This module provides functionality to download videos from YouTube, TikTok, Instagram, Facebook,
Twitter/X, and many other social media platforms. It supports format selection, batch downloads,
and maintains download history.

Author: Nayan Das
Version: 1.1.12
License: MIT
"""

import os
import sys
import csv
import time
import json
import shutil
import logging
import tempfile
import subprocess
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Optional, Tuple, Any

# Third-party imports
import yt_dlp
import requests
import instaloader
from tqdm import tqdm
from pyfiglet import Figlet
from termcolor import colored
from tabulate import tabulate


# ---------------------------------
# Constants and Configuration
# ---------------------------------
AUTHOR = "Nayan Das"
CURRENT_VERSION = "1.1.12"
EMAIL = "nayanchandradas@hotmail.com"
DISCORD_INVITE = "https://discord.gg/skHyssu"
WEBSITE = "https://nayandas69.github.io/Social-Media-Downloader"
GITHUB_REPO_URL = "https://github.com/nayandas69/Social-Media-Downloader"
PYPI_API_URL = "https://pypi.org/pypi/social-media-downloader/json"

# Configuration constants
CONFIG_FILE = "config.json"
DEFAULT_CONFIG = {
    "default_format": "show_all",
    "download_directory": "media",
    "history_file": "download_history.csv",
    "mp3_quality": "192",
}

VALID_DEFAULT_FORMATS = {
    "show_all",
    "mp3",
    "360p",
    "480p",
    "720p",
    "1080p",
    "1440p",
    "2160p",
    "4320p",
}
VALID_MP3_QUALITIES = {"64", "128", "192", "256", "320", "396"}

# Supported platform domains
SUPPORTED_DOMAINS = [
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
    "pinterest.com",
    "pin.it",
    "linkedin.com",
    "bilibili.tv",
    "odysee.com",
    "rumble.com",
    "gameclips.io",
    "triller.co",
    "snackvideo.com",
    "kwai.com",
    "imdb.com",
    "weibo.com",
    "dailymotion.com",
    "dai.ly",
    "tumblr.com",
    "bsky.app",
]

INSTAGRAM_DOMAINS = ["instagram.com"]

# Network timeout settings
NETWORK_TIMEOUT = 10
CONNECTION_CHECK_TIMEOUT = 5
RETRY_DELAY = 5


# ---------------------------------
# Logging Setup
# ---------------------------------
def setup_logging() -> None:
    """Configure logging for the application."""
    logging.basicConfig(
        filename="downloader.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="a",
    )


setup_logging()


# ---------------------------------
# Display Functions
# ---------------------------------
def display_author_details() -> None:
    """Display the animated banner and author details with improved error handling."""
    try:
        # Clear screen cross-platform
        os.system("cls" if os.name == "nt" else "clear")

        # Create and display banner
        banner_font = Figlet(font="slant")
        banner_text = banner_font.renderText("Social Media Downloader")
        banner_colored = colored(banner_text, "cyan", attrs=["bold"])

        # Animate banner display
        for line in banner_colored.splitlines():
            print(line)
            time.sleep(0.05)

        print("\n")

        # Display author information with animation
        info_lines = [
            ("Author   : ", AUTHOR, "yellow", "white"),
            ("Email    : ", EMAIL, "yellow", "cyan"),
            ("Discord  : ", DISCORD_INVITE, "yellow", "cyan"),
            ("Repo     : ", GITHUB_REPO_URL, "yellow", "cyan"),
            ("Website  : ", WEBSITE, "yellow", "cyan"),
            ("Version  : ", CURRENT_VERSION, "yellow", "green"),
        ]

        for label, value, label_color, value_color in info_lines:
            print(
                colored(f"{label:<10}", label_color, attrs=["bold"])
                + colored(value, value_color)
            )
            time.sleep(0.2)

        # Loading animation
        print(colored("\nLoading", "yellow", attrs=["bold"]), end="", flush=True)
        for _ in range(5):
            time.sleep(0.4)
            print(colored(".", "yellow", attrs=["bold"]), end="", flush=True)

        time.sleep(0.5)
        print()

    except Exception as e:
        logging.error(f"Error displaying banner: {e}")
        print("Social Media Downloader - Starting...")


display_author_details()


# ---------------------------------
# Configuration Management
# ---------------------------------
def load_config() -> Dict[str, Any]:
    """
    Load, validate, and auto-correct the configuration file.

    Returns:
        Dict[str, Any]: Configuration dictionary with validated values
    """
    config_changed = False

    # Create config file if it doesn't exist
    if not os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
            logging.info(f"Created new config file: {CONFIG_FILE}")
            return DEFAULT_CONFIG.copy()
        except IOError as e:
            logging.error(f"Failed to create config file: {e}")
            return DEFAULT_CONFIG.copy()

    # Load existing configuration
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config_data = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logging.error(f"Failed to load config file: {e}. Using defaults.")
        return DEFAULT_CONFIG.copy()

    # Validate and fix configuration
    config_data = _validate_config(config_data)

    # Save corrected config if needed
    if config_changed:
        _save_config(config_data)

    return config_data


def _validate_config(config_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate configuration data and fix invalid values.

    Args:
        config_data: Configuration dictionary to validate

    Returns:
        Dict[str, Any]: Validated configuration dictionary
    """
    config_changed = False

    # Add missing keys from default
    for key, default_value in DEFAULT_CONFIG.items():
        if key not in config_data:
            logging.warning(
                f"Missing '{key}' in config. Setting to default: {default_value}"
            )
            config_data[key] = default_value
            config_changed = True

    # Validate mp3_quality
    mp3_quality = str(config_data.get("mp3_quality", "192"))
    if mp3_quality not in VALID_MP3_QUALITIES:
        logging.warning(f"Invalid mp3_quality '{mp3_quality}', resetting to '192'.")
        config_data["mp3_quality"] = "192"
        config_changed = True

    # Validate default_format
    default_format = str(config_data.get("default_format", "show_all")).lower()
    if default_format not in VALID_DEFAULT_FORMATS:
        logging.warning(
            f"Invalid default_format '{default_format}', resetting to 'show_all'."
        )
        config_data["default_format"] = "show_all"
        config_changed = True

    return config_data


def _save_config(config_data: Dict[str, Any]) -> None:
    """Save configuration data to file."""
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config_data, f, indent=4)
        logging.info("Config file updated with corrected values.")
    except IOError as e:
        logging.error(f"Failed to write corrected config: {e}")


# Load configuration and setup global variables
config = load_config()
download_directory = config.get("download_directory", "media")
history_file = config.get("history_file", "download_history.csv")
mp3_quality = str(config.get("mp3_quality", "192"))
default_format = config.get("default_format", "show_all")

# Ensure download directory exists
try:
    os.makedirs(download_directory, exist_ok=True)
except OSError as e:
    logging.error(f"Failed to create download directory '{download_directory}': {e}")
    raise SystemExit("Cannot proceed without a valid download directory.")


# ---------------------------------
# System Requirements Check
# ---------------------------------
def ensure_ffmpeg() -> None:
    """
    Ensure that FFmpeg is installed and available in PATH.

    Raises:
        SystemExit: If FFmpeg is not found
    """
    if shutil.which("ffmpeg") is None:
        error_msg = [
            "\033[1;31m\nFFmpeg is not installed. Please install FFmpeg and try again.\033[0m",
            "\033[1;31mDownload FFmpeg from: https://ffmpeg.org/download.html\033[0m",
            "\033[1;31mFor Windows users, add FFmpeg to your PATH.\033[0m",
            "\033[1;31mFor Linux users, run: sudo apt install ffmpeg\033[0m",
            "\033[1;31mAfter installation, restart the program.\033[0m",
        ]
        for msg in error_msg:
            print(msg)
        sys.exit(1)
    else:
        print("\033[1;32mFFmpeg is installed. Proceeding...\033[0m")


# ---------------------------------
# Network Utilities
# ---------------------------------
def check_internet_connection() -> bool:
    """
    Check if the system has an active internet connection.

    Returns:
        bool: True if internet connection is available, False otherwise
    """
    try:
        response = requests.head(
            "https://www.google.com", timeout=CONNECTION_CHECK_TIMEOUT
        )
        return response.status_code == 200
    except Exception:  # Catch all exceptions, not just requests.RequestException
        return False


def ensure_internet_connection() -> None:
    """Ensure internet connection is available, retry if not."""
    while not check_internet_connection():
        print("\033[91m\nNo internet connection. Retrying in 5 seconds...\033[0m")
        time.sleep(RETRY_DELAY)
    print("\033[92mInternet connection detected. Proceeding...\033[0m")


# ---------------------------------
# Update Management
# ---------------------------------
def check_for_updates() -> None:
    """Check for updates from PyPI and notify users."""
    if not check_internet_connection():
        print(
            "\n\033[1;31mNo internet connection. Please connect and try again.\033[0m"
        )
        return

    print(f"\n\033[1;36mChecking for updates...\033[0m")
    print(f"\033[1;33mCurrent version:\033[0m {CURRENT_VERSION}")

    try:
        response = requests.get(PYPI_API_URL, timeout=NETWORK_TIMEOUT)
        response.raise_for_status()
        data = response.json()

        latest_version = data.get("info", {}).get("version", "Unknown")
        print(f"\033[1;33mLatest version:\033[0m {latest_version}")

        current_parsed = _parse_version(CURRENT_VERSION)
        latest_parsed = _parse_version(latest_version)

        if latest_parsed > current_parsed:
            _display_update_available(latest_version, data)
        elif latest_parsed == current_parsed:
            _display_up_to_date()
        else:
            _display_development_version()

    except requests.exceptions.Timeout:
        print(
            f"\n\033[1;31mRequest timed out. Please check your internet connection.\033[0m"
        )
        logging.error("Update check timed out")
    except requests.exceptions.RequestException as e:
        print(f"\n\033[1;31mError checking for updates: {e}\033[0m")
        print(f"\033[1;36mManually check: {GITHUB_REPO_URL}/releases\033[0m")
        logging.error(f"Update check failed: {e}")
    except Exception as e:
        print(f"\n\033[1;31mUnexpected error during update check: {e}\033[0m")
        logging.error(f"Unexpected update check error: {e}", exc_info=True)


def _parse_version(version_str: str) -> Tuple[int, ...]:
    """Parse version string into tuple of integers for comparison."""
    try:
        clean_version = str(version_str).strip()
        return tuple(map(int, clean_version.split(".")))
    except (ValueError, AttributeError, TypeError):
        return (0, 0, 0)


def _display_update_available(latest_version: str, data: Dict[str, Any]) -> None:
    """Display update available message."""
    print(f"\n\033[1;32mNew version available: {latest_version}\033[0m")
    print(f"\n\033[1;36mUpdate options:\033[0m")
    print(f"\033[1;33m1. Using pip:\033[0m")
    print(f"   \033[1;32mpip install social-media-downloader --upgrade\033[0m")
    print(f"\n\033[1;33m2. Download from GitHub:\033[0m")
    print(f"   {GITHUB_REPO_URL}/releases/latest")

    # Show release info if available
    release_info = data.get("info", {})
    summary = release_info.get("summary", "")
    if summary:
        print(f"\n\033[1;36mWhat's new:\033[0m {summary}")


def _display_up_to_date() -> None:
    """Display up-to-date message."""
    print(f"\n\033[1;32mYou're up to date!\033[0m")
    print(f"\033[1;36mJoin our Discord for updates and support:\033[0m")
    print(f"{DISCORD_INVITE}")


def _display_development_version() -> None:
    """Display development version message."""
    print(
        f"\n\033[1;33mYou're running a newer version than what's published on PyPI.\033[0m"
    )
    print(f"\033[1;36mThis might be a development or beta version.\033[0m")


# ---------------------------------
# Utility Functions
# ---------------------------------
def log_download(url: str, status: str) -> None:
    """
    Log the download status in history file and application log.

    Args:
        url: The URL that was downloaded
        status: Status of the download (Success/Failed)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(history_file, "a+", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([url, status, timestamp])
        logging.info(f"Download status for {url}: {status}")
    except IOError as e:
        logging.error(f"Failed to log download: {e}")


def get_unique_filename(filename: str) -> str:
    """
    Ensure downloaded files have unique names by appending numbers if duplicates exist.

    Args:
        filename: Original filename

    Returns:
        str: Unique filename
    """
    if not os.path.exists(filename):
        return filename

    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = f"{base} ({counter}){ext}"
    while os.path.exists(new_filename):
        counter += 1
        new_filename = f"{base} ({counter}){ext}"
    return new_filename


def is_valid_platform_url(url: str, allowed_domains: List[str]) -> bool:
    """
    Check if the URL matches one of the allowed domains.

    Args:
        url: URL to validate
        allowed_domains: List of allowed domain strings

    Returns:
        bool: True if URL contains any allowed domain
    """
    return any(domain in url.lower() for domain in allowed_domains)


# ---------------------------------
# Format Display
# ---------------------------------
def print_format_table(info: Dict[str, Any]) -> None:
    """
    Display available video formats in a formatted table.

    Args:
        info: Video information dictionary from yt-dlp
    """
    formats = info.get("formats", [])
    table_data = []

    for fmt in formats:
        # Skip non-downloadable formats
        if fmt.get("vcodec") == "none" and fmt.get("acodec") == "none":
            continue

        fmt_id = fmt.get("format_id", "")
        ext = fmt.get("ext", "")
        resolution = _get_resolution_string(fmt)
        fps = fmt.get("fps", "")
        filesize_str = _get_filesize_string(fmt.get("filesize", 0))
        vcodec = fmt.get("vcodec", "")
        acodec = fmt.get("acodec", "")
        note = fmt.get("format_note", "")

        # Color format ID
        fmt_id_colored = f"\033[1;32m{fmt_id}\033[0m"

        table_data.append(
            [fmt_id_colored, ext, resolution, fps, filesize_str, vcodec, acodec, note]
        )

    # Create colored headers
    headers = [
        f"\033[1;33m{header}\033[0m"
        for header in [
            "ID",
            "EXT",
            "RESOLUTION",
            "FPS",
            "SIZE",
            "VCODEC",
            "ACODEC",
            "NOTE",
        ]
    ]

    print("\n\033[1;36mAvailable formats:\033[0m")
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


def _get_resolution_string(fmt: Dict[str, Any]) -> str:
    """Get resolution string from format info."""
    width = fmt.get("width")
    height = fmt.get("height")
    if height:
        return f"{width or ''}x{height}"
    return "audio"


def _get_filesize_string(filesize: Optional[int]) -> str:
    """Convert filesize to human-readable string."""
    if filesize and filesize > 0:
        return f"{filesize / (1024 * 1024):.2f} MB"
    return "-"


# -----------------------------------------------------------
# Download Functions for Youtube, TikTok and other platforms
# -----------------------------------------------------------
def download_youtube_or_tiktok_video(url: str) -> None:
    """
    Download a video from supported platforms using yt-dlp.

    Args:
        url: Video URL to download
    """
    if not is_valid_platform_url(url, SUPPORTED_DOMAINS):
        print("\n\033[1;31mInvalid URL. Please enter a valid URL.\033[0m")
        print(f"\033[1;31mSupported platforms: {WEBSITE}/supported-platforms\033[0m")
        return

    ensure_ffmpeg()
    ensure_internet_connection()

    try:
        # Extract video information
        with yt_dlp.YoutubeDL({"listformats": False}) as ydl:
            info = ydl.extract_info(url, download=False)

        _display_video_info(info)

        # Determine download format
        format_choice = _get_format_choice(info)

        # Prepare download options
        ydl_opts = _prepare_download_options(info, format_choice)

        # Perform download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            log_download(url, "Success")
            print(
                f"\n\033[1;32mDownloaded successfully:\033[0m {info.get('title', 'Unknown')}"
            )

    except Exception as e:
        log_download(url, f"Failed: {str(e)}")
        logging.error(f"Error downloading video from {url}: {str(e)}", exc_info=True)
        print(f"\033[1;31mError downloading video:\033[0m {str(e)}")


def _display_video_info(info: Dict[str, Any]) -> None:
    """Display video metadata information."""
    title = info.get("title", "Unknown Title")
    uploader = info.get("uploader", "Unknown Uploader")
    upload_date = info.get("upload_date", "Unknown Date")

    # Format upload date
    upload_date_formatted = upload_date
    if upload_date != "Unknown Date":
        try:
            upload_date_formatted = datetime.strptime(upload_date, "%Y%m%d").strftime(
                "%B %d, %Y"
            )
        except ValueError:
            pass

    print("\n\033[1;36mVideo Details:\033[0m")
    print(f"\033[1;33mTitle:\033[0m {title}")
    print(f"\033[1;33mUploader:\033[0m {uploader}")
    print(f"\033[1;33mUpload Date:\033[0m {upload_date_formatted}")


def _get_format_choice(info: Dict[str, Any]) -> str:
    """Get format choice from user or config."""
    preferred_format = config.get("default_format", "show_all").lower()

    if preferred_format == "show_all":
        print_format_table(info)
        return input(
            "\nEnter format ID to download (or type 'mp3' for audio only): "
        ).strip()

    # Map friendly format names to yt-dlp format strings
    friendly_format_map = {
        "360p": "bestvideo[height<=360]+bestaudio/best",
        "480p": "bestvideo[height<=480]+bestaudio/best",
        "720p": "bestvideo[height<=720]+bestaudio/best",
        "1080p": "bestvideo[height<=1080]+bestaudio/best",
        "1440p": "bestvideo[height<=1440]+bestaudio/best",
        "2160p": "bestvideo[height<=2160]+bestaudio/best",
        "4320p": "bestvideo[height<=4320]+bestaudio/best",
        "mp3": "mp3",
        "best": "bestvideo+bestaudio/best",
    }

    return friendly_format_map.get(preferred_format, preferred_format)


def _prepare_download_options(info: Dict[str, Any], choice: str) -> Dict[str, Any]:
    """Prepare yt-dlp download options based on format choice."""
    title = info.get("title", "Unknown")
    filename_base = get_unique_filename(os.path.join(download_directory, title))

    if choice == "mp3":
        return {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(download_directory, f"{title}.%(ext)s"),
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": config.get("mp3_quality", "192"),
                }
            ],
        }
    else:
        # Handle video-only formats by auto-merging with audio
        selected_fmt = next(
            (f for f in info.get("formats", []) if f.get("format_id") == choice),
            None,
        )

        if selected_fmt and selected_fmt.get("acodec") in ["none", None, ""]:
            print(f"\n\033[1;33mNote:\033[0m Selected format '{choice}' has no audio.")
            print(f"\033[1;32mAuto-fix:\033[0m Merging with best available audio.")
            choice = f"{choice}+bestaudio"

        return {
            "format": choice,
            "outtmpl": f"{filename_base}.%(ext)s",
            "merge_output_format": "mp4",
            "noplaylist": True,
        }


# ---------------------------------
# Download Functions for Instagram
# ---------------------------------
def download_instagram_post(url: str) -> None:
    """
    Download an Instagram post using instaloader.

    Args:
        url: Instagram post URL
    """
    if not is_valid_platform_url(url, INSTAGRAM_DOMAINS):
        print("\n\033[1;31mInvalid URL. Please enter a valid Instagram URL.\033[0m")
        return

    ensure_internet_connection()

    try:
        loader = instaloader.Instaloader()
        shortcode = _extract_instagram_shortcode(url)

        if not shortcode:
            print("\n\033[1;31mCould not extract shortcode from URL.\033[0m")
            log_download(url, "Failed: Invalid URL format")
            return

        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=download_directory)

        log_download(url, "Success")
        print(f"\n\033[1;32mDownloaded Instagram post successfully:\033[0m {url}")

    except Exception as e:
        log_download(url, f"Failed: {str(e)}")
        logging.error(f"Instagram download error for {url}: {str(e)}")
        print(f"\033[1;31mError downloading Instagram post:\033[0m {str(e)}")


def extract_instagram_video_mp3(url: str) -> None:
    """
    Download Instagram video and convert to MP3.

    Args:
        url: Instagram video URL
    """
    if not is_valid_platform_url(url, INSTAGRAM_DOMAINS):
        print(
            "\n\033[1;31mError: This feature only supports Instagram video URLs.\033[0m"
        )
        log_download(url, "Failed: Invalid Instagram URL")
        return

    ensure_internet_connection()

    shortcode = _extract_instagram_shortcode(url)
    if not shortcode:
        print("\n\033[1;31mError: Could not extract shortcode from URL.\033[0m")
        log_download(url, "Failed: Invalid URL format")
        return

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            loader = instaloader.Instaloader(
                dirname_pattern=temp_dir, save_metadata=False, download_comments=False
            )

            post = instaloader.Post.from_shortcode(loader.context, shortcode)

            if not post.is_video:
                print("\n\033[1;31mThis post is not a video.\033[0m")
                log_download(url, "Failed: Not a video post")
                return

            print("Downloading video...")
            loader.download_post(post, target=shortcode)

            # Find downloaded video file
            video_path = _find_video_file(temp_dir)
            if not video_path:
                print("\n\033[1;31mVideo file not found after download.\033[0m")
                log_download(url, "Failed: Video file not found")
                return

            ensure_ffmpeg()

            # Convert to MP3
            mp3_path = os.path.join(download_directory, f"instagram_{shortcode}.mp3")
            _convert_video_to_mp3(video_path, mp3_path)

            print(f"\n\033[1;32mDownloaded and converted successfully:\033[0m {url}")
            log_download(url, "Success")

    except Exception as e:
        print(f"\033[1;31mError: {e}\033[0m")
        log_download(url, f"Failed: {str(e)}")
        logging.error(f"Instagram MP3 extract error for {url}: {str(e)}")


def _extract_instagram_shortcode(url: str) -> Optional[str]:
    """Extract shortcode from Instagram URL."""
    if "/reel/" in url:
        return url.split("/reel/")[1].split("/")[0]
    elif "/p/" in url:
        return url.split("/p/")[1].split("/")[0]
    elif "/tv/" in url:
        return url.split("/tv/")[1].split("/")[0]
    return None


def _find_video_file(directory: str) -> Optional[str]:
    """Find the first .mp4 file in the directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp4"):
                return os.path.join(root, file)
    return None


def _convert_video_to_mp3(video_path: str, mp3_path: str) -> None:
    """Convert video file to MP3 using FFmpeg."""
    print("Extracting MP3...")
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            video_path,
            "-vn",
            "-ab",
            f"{mp3_quality}k",
            "-ar",
            "44100",
            "-y",
            mp3_path,
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )


# -------------------------
# Batch Download Instagram
# -------------------------
def batch_download_from_file(file_path: str) -> None:
    """
    Read URLs from a text file and download them concurrently.

    Args:
        file_path: Path to file containing URLs (one per line)
    """
    ensure_internet_connection()

    if not os.path.exists(file_path):
        print(f"\n\033[1;31mFile not found: {file_path}\033[0m")
        return

    print(f"Reading URLs from {file_path}...")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            urls = [line.strip() for line in file.readlines() if line.strip()]
    except IOError as e:
        print(f"\033[1;31mError reading file: {e}\033[0m")
        logging.error(f"Error reading batch file {file_path}: {e}")
        return

    if not urls:
        print("\033[1;31mNo URLs found in the file.\033[0m")
        return

    print(f"Found {len(urls)} URLs. Starting batch download...")

    with ThreadPoolExecutor(max_workers=3) as executor:
        list(
            tqdm(
                executor.map(download_instagram_post, urls),
                total=len(urls),
                desc="Instagram Batch",
            )
        )

    print("\n\033[1;32mBatch download complete.\033[0m")


# ---------------------------------
# Help and Menu Functions
# ---------------------------------
def show_help() -> None:
    """Display comprehensive help information."""
    help_sections = [
        (
            "\n\033[1;36mHow to Use Social Media Downloader:\033[0m",
            [
                "1. \033[1;33mDownload Videos:\033[0m Enter '1' to download public videos.",
                "2. \033[1;33mDownload Instagram Content:\033[0m Enter '2' for Instagram posts, videos, reels.",
                "3. \033[1;33mCheck for Updates:\033[0m Enter '3' to check for software updates.",
                "4. \033[1;33mHelp Menu:\033[0m Enter '4' to display this help guide.",
                "5. \033[1;33mExit the Program:\033[0m Enter '5' to close the application.",
            ],
        ),
        (
            "\033[1;31mImportant Notice:\033[0m",
            [
                "\033[1;31mThis tool only supports downloading public videos.\033[0m",
                "\033[1;31mPrivate, restricted, or non-public content cannot be downloaded.\033[0m",
            ],
        ),
        (
            "\033[1;32mSupported Platforms:\033[0m",
            [f"• Visit: {WEBSITE}/supported-platforms"],
        ),
        (
            "\033[1;32mAdditional Information:\033[0m",
            [
                "• All downloaded files are saved in the 'media' directory.",
                "• Download history and logs are automatically recorded.",
                "• For support, feature requests, or bug reports, contact:",
            ],
        ),
        (
            "\033[1;33mContact Information:\033[0m",
            [
                f"Email: {EMAIL}",
                f"Discord: {DISCORD_INVITE}",
                f"GitHub: {GITHUB_REPO_URL}",
                f"Website: {WEBSITE}",
            ],
        ),
    ]

    for title, items in help_sections:
        print(title)
        for item in items:
            print(item)
        print()


def instagram_menu() -> None:
    """Display Instagram-specific download options."""
    print("\n\033[1;36mInstagram Menu\033[0m")
    options = [
        "1. Download Reel, Video & Pictures",
        "2. Extract MP3 from Instagram Video",
        "3. Batch Download Instagram Posts",
    ]

    for option in options:
        print(option)

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        url = input("Enter Instagram URL: ").strip()
        if url:
            download_instagram_post(url)
    elif choice == "2":
        url = input("Enter Instagram video URL: ").strip()
        if url:
            extract_instagram_video_mp3(url)
    elif choice == "3":
        file_path = input("Enter path to text file containing Instagram URLs: ").strip()
        if file_path:
            batch_download_from_file(file_path)
        else:
            print("\033[1;31mExample paths:\033[0m")
            print("Linux: /home/user/batch_links.txt")
            print("Windows: C:\\Users\\user\\batch_links.txt")
    else:
        print("\033[1;31mInvalid choice.\033[0m")


# ---------------------------------
# Main CLI Interface
# ---------------------------------
def main() -> None:
    """Main function for user interaction and CLI interface."""
    try:
        input("\nPress Enter to start the Social Media Downloader...")
        print(f"\033[38;2;255;105;180mWelcome to Social Media Downloader!\033[0m")

        while True:
            _display_main_menu()
            choice = input("\nEnter your choice: ").strip()

            if not choice:
                continue

            if choice == "1":
                url = input("Enter video URL: ").strip()
                if url:
                    download_youtube_or_tiktok_video(url)
            elif choice == "2":
                instagram_menu()
            elif choice == "3":
                check_for_updates()
            elif choice == "4":
                show_help()
            elif choice == "5":
                print(
                    f"\033[38;2;255;105;180mThank you for using Social Media Downloader!\033[0m"
                )
                sys.exit(0)
            else:
                print("\033[1;31mInvalid choice. Please try again.\033[0m")

    except KeyboardInterrupt:
        print(f"\n\033[38;2;255;105;180mProgram interrupted by user. Goodbye!\033[0m")
        sys.exit(0)
    except Exception as e:
        logging.critical(f"Unexpected error in main: {e}", exc_info=True)
        print(f"\033[1;31mUnexpected error: {e}\033[0m")
        sys.exit(1)


def _display_main_menu() -> None:
    """Display the main menu options."""
    print("\n" + "─" * 60)
    menu_options = [
        "1. Download YouTube/TikTok... etc.",
        "2. Download Instagram",
        "3. Check for updates",
        "4. Help",
        "5. Exit",
    ]

    for option in menu_options:
        print(option)


def cli() -> None:
    """Entry point for the CLI application."""
    main()
