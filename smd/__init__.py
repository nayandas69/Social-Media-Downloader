# Social Media Downloader
# smd/__init__.py
# This file is part of Social Media Downloader (SMD).


from .downloader import (
    download_youtube_or_tiktok_video,
    download_instagram_post,
    extract_instagram_video_mp3,
    batch_download_from_file,
    check_for_updates,
    show_help,
)

__all__ = [
    "download_youtube_or_tiktok_video",
    "download_instagram_post",
    "extract_instagram_video_mp3",
    "batch_download_from_file",
    "check_for_updates",
    "show_help",
]
