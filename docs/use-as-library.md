---
title: 📦 Using `social-media-downloader` in Your Python Project
---

Welcome to the guide on how to use the **Social Media Downloader (SMD)** Python package in your own projects or as a standalone CLI tool. This page covers installation, importing functions, using the CLI, and working examples.


## Installation

To get started, install the package from [PyPI](https://pypi.org/project/social-media-downloader/):

```bash
pip install social-media-downloader
````

!!! note
   Requires **Python 3.10+**. Ensure your environment uses a compatible version.


## Importing SMD in Your Python Code

Once installed, you can import and use all major functions directly:

```python
from smd import (
    download_youtube_or_tiktok_video,
    download_instagram_post,
    extract_instagram_video_mp3,
    batch_download_from_file,
    check_for_updates,
    show_help,
)
```

### Example: Download a YouTube Video

```python
from smd import download_youtube_or_tiktok_video

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
download_youtube_or_tiktok_video(video_url)
```

### Example: Download an Instagram Post

```python
from smd import download_instagram_post

post_url = "https://www.instagram.com/p/CxA-Example/"
download_instagram_post(post_url)
```

### Example: Batch Download from File

```python
from smd import batch_download_from_file

batch_download_from_file("batch_links.txt")
```

!!! tip
   The `batch_links.txt` file should contain one Instagram post URL per line.


## Use in Tests and Dev Projects

You can install with development tools using:

```bash
pip install 'social-media-downloader[dev]'
```

This will install additional tools like `pytest`, `flake8`, and `black`.


## Using SMD as a CLI Tool

After installation, you can run it from your terminal:

```bash
smd
```

or

```bash
social-media-downloader
```

This launches the interactive menu where you can select to download from YouTube, Instagram, check for updates, or view help.

### Running as a Python Module

Alternatively, you can launch it like this:

```bash
python -m smd
```

!!! tip
   This is helpful when running from a virtual environment or inside scripts.


## Full API Reference

Here's a quick reference of available methods:

| Function                                      | Description                                             |
| --------------------------------------------- | ------------------------------------------------------- |
| `download_youtube_or_tiktok_video(url)`       | Downloads video from supported platforms                |
| `download_instagram_post(url)`                | Downloads single Instagram post                         |
| `extract_instagram_video_mp3(url)`            | Extracts MP3 from an Instagram video                    |
| `batch_download_from_file(file_path)`         | Batch downloads from a file                             |
| `check_for_updates()`                         | Checks for the latest version                           |
| `show_help()`                                 | Displays the CLI help menu                              |
| `load_config()`                               | Loads or resets the configuration file                  |
| `check_internet_connection()`                 | Checks if internet is available                         |
| `is_valid_platform_url(url, allowed_domains)` | Validates URL against supported platforms               |
| `get_unique_filename(filename)`               | Ensures downloaded file doesn't overwrite existing ones |
| `log_download(url, status)`                   | Logs download attempts to history                       |

