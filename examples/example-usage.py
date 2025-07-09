# example-usage.py
# --------------------------------------------
# Example usage of the Social Media Downloader (smd) package.
# This script shows how to import and use the main functions
# provided by the package as a Python module (not CLI).
# Requires: pip install social-media-downloader
# --------------------------------------------

from smd import (
    download_youtube_or_tiktok_video,
    download_instagram_post,
    extract_instagram_video_mp3,
    batch_download_from_file,
    check_for_updates,
    load_config,
    is_valid_platform_url,
    get_unique_filename,
    log_download,
)

# --------------------------------------------
# Example 1: Download a YouTube video
# --------------------------------------------
youtube_url = "https://www.youtube.com/watch?v=Q2e_FsDMi3I"

if is_valid_platform_url(youtube_url, ["youtube.com", "youtu.be"]):
    print("[+] Downloading YouTube video...")
    download_youtube_or_tiktok_video(youtube_url)
else:
    print("[-] Invalid YouTube URL")

# --------------------------------------------
# Example 2: Download an Instagram post
# --------------------------------------------
instagram_url = "https://www.instagram.com/p/CxyzExample/"

if is_valid_platform_url(instagram_url, ["instagram.com"]):
    print("[+] Downloading Instagram post...")
    download_instagram_post(instagram_url)

# --------------------------------------------
# Example 3: Extract MP3 from Instagram video
# --------------------------------------------
reel_url = "https://www.instagram.com/reel/CabcExample/"

print("[+] Extracting MP3 from Instagram reel...")
extract_instagram_video_mp3(reel_url)

# --------------------------------------------
# Example 4: Batch download from a file
# --------------------------------------------
batch_file = "batch_links.txt"  # Create a text file with 1 Instagram URL per line

print("[+] Starting batch download from file...")
batch_download_from_file(batch_file)

# --------------------------------------------
# Example 5: Check for Updates
# --------------------------------------------
print("[*] Checking for updates...")
check_for_updates()

# --------------------------------------------
# Example 6: Load Configuration and modify
# --------------------------------------------
config = load_config()
print("Current format preference:", config["default_format"])
config["default_format"] = "720p"

# (Optional) Save the updated config back to file
import json
with open("config.json", "w") as f:
    json.dump(config, f, indent=4)
print("[*] Config updated to 720p")

# --------------------------------------------
# Example 7: Log a manual download entry
# --------------------------------------------
log_download("https://customsource.com/vid.mp4", "Success")
print("[*] Logged custom download entry.")

# --------------------------------------------
# Example 8: Filename deduplication
# --------------------------------------------
filename = get_unique_filename("sample_video.mp4")
print("Safe filename to use:", filename)
