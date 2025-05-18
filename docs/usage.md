---
title: Usage Guide 🪴
---

Ready to download videos like a pro? This guide shows you how to use **Social Media Downloader** — whether you're running it from source, using the `.exe`, `.deb`, binary, or pip install.

---

## Step 1: Install the Tool

!!! question "Not Installed Yet?"
    If you haven’t installed the tool yet, check out our [Installation Guide](./installation.md) first. Once you're set up, come back here to start using it!

---

## Step 2: Run the Program

Depending on how you installed the tool, use one of the methods below:

### Run from Source (Python)

```bash
python3 smd/downloader.py
```

!!! info
    This runs the tool directly from the source code.

---

### Run the `.exe` (Windows)

1. Download the `.exe` from the [latest release](https://github.com/nayandas69/Social-Media-Downloader/releases/latest)
2. Double-click it.
3. A terminal window will open — paste your URL when prompted.

!!! tip
    No setup needed. Just click and go!

---

### Run the `.deb` Package (Ubuntu/Debian)

```bash
sudo dpkg -i social-media-downloader_VERSION_amd64.deb
smd
```

!!! abstract
    This installs the tool globally — run it anytime with `smd`.

---

### Run the Binary (Other Linux)

```bash
chmod +x smd
./smd
```

!!! info
    Make sure you extracted the `.tar.gz` binary from [Releases](https://github.com/nayandas69/Social-Media-Downloader/releases/latest) first.

---

### Run via pip

```bash
pip install social-media-downloader
```

Then use:

* `social-media-downloader` → works in all versions
* `smd` → works in **v1.1.4 and newer only**

!!! danger
    Use the `smd` shortcut only if you're using v1.1.4 or newer.

---

## Step 3: What You’ll See

Once the program starts, you’ll be greeted with a screen like this:

> ![screenshot of program welcome screen](https://raw.githubusercontent.com/nayandas69/Social-Media-Downloader/4d0aebcc7433bb47bbfdce34b88ece1e7e41fd4f/docs/assets/intro.gif)

---

## Step 4: Choose a Platform and Paste a URL

!!! example "Example Interaction"
    ```text
    Welcome to Social Media Downloader!
    ────────────────────────────────────────────────────────────

    1. Download YouTube/TikTok... etc.
    2. Download Instagram
    3. Check for updates
    4. Help
    5. Exit

    Enter your choice: 1
    Enter video URL: https://www.youtube.com/watch?v=EXAMPLE_ID
    ```

The tool will automatically detect your system, check for internet and FFmpeg, and start downloading.

---

## Sample Output

!!! quote "Typical Output Preview"
    ```text
    [youtube] Extracting URL...
    [youtube] Downloading webpage...
    ...
    Video Details:
    Title: Social-Media-Downloader
    Uploader: nayandas69
    Upload Date: Dec 1, 2024

    Available formats:
    ╒══════╤═══════╤══════════════╤═══════╤═══════════╤═══════════════╤═══════════╤═══════════════╕
    │  ID  │ EXT   │ RESOLUTION   │ FPS   │ SIZE      │ VCODEC        │ ACODEC    │ NOTE          │
    ├──────┼───────┼──────────────┼───────┼───────────┼───────────────┼───────────┼───────────────┤
    │  136 │ mp4   │ 1280x720     │ 30    │ 56.82 MB  │ avc1.4d401f   │ none      │ 720p          │
    │  251 │ webm  │ audio        │       │ 0.48 MB   │ none          │ opus      │ medium        │
    │  299 │ mp4   │ 1920x1080    │ 60    │ 114.83 MB │ avc1.64002a   │ none      │ 1080p60       │
    ╘══════╧═══════╧══════════════╧═══════╧═══════════╧═══════════════╧═══════════╧═══════════════╛
    ```

Then it will prompt you to choose a format, and begin downloading.

---

!!! success "You're Ready!"
Happy downloading!