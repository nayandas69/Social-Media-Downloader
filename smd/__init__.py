"""
Social Media Downloader (SMD) - A comprehensive CLI tool for downloading videos.

This package provides functionality to download videos from various social media platforms
including YouTube, TikTok, Instagram, Facebook, Twitter/X, and many others.

Author: Nayan Das
Version: 1.1.12
License: MIT
"""

from .downloader import (
    download_youtube_or_tiktok_video,
    download_instagram_post,
    extract_instagram_video_mp3,
    batch_download_from_file,
    check_for_updates,
    show_help,
    load_config,
    check_internet_connection,
    is_valid_platform_url,
    get_unique_filename,
    log_download,
    cli,
)


__version__ = "1.1.12"
__author__ = "Nayan Das"
__email__ = "nayanchandradas@hotmail.com"

__all__ = [
    "download_youtube_or_tiktok_video",
    "download_instagram_post",
    "extract_instagram_video_mp3",
    "batch_download_from_file",
    "check_for_updates",
    "show_help",
    "load_config",
    "check_internet_connection",
    "is_valid_platform_url",
    "get_unique_filename",
    "log_download",
    "cli",
]
