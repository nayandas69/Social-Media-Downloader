---
title: Installation
---

Welcome to the installation guide for **Social Media Downloader** — a lightweight, open-source CLI tool for downloading public videos from platforms like YouTube, TikTok, Instagram, and more.

This page walks you through installing the tool via `pip`, source code, standalone `.exe`, `.deb` package, or binary `.tar.gz`.

!!! question
    Need help using the tool after installation? Check out the [Usage Guide](./usage.md) for step-by-step instructions and examples.

---

## Clone the Repository

If you'd like to run the tool from source or contribute to development:

```bash
git clone https://github.com/nayandas69/Social-Media-Downloader.git
cd Social-Media-Downloader
```

---

## Set Up a Python Environment

We recommend using **Python 3.8+** and creating a virtual environment to manage dependencies cleanly.

### On Windows

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### On Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

!!! quote
    Running from source requires installing dependencies listed in `requirements.txt`.

---

## Install FFmpeg (Required)

!!! important
    `ffmpeg` is essential for handling video/audio formats. The downloader will not work without it.

### On Windows

1. Visit [ffmpeg.org](https://ffmpeg.org/download.html) and download the latest static build.
2. Extract the archive.
3. Add the `bin` directory to your system `PATH`.

### On Linux

```bash
sudo apt update
sudo apt install ffmpeg
```

To verify:

```bash
ffmpeg -version
```

If you see version details, you're good to go!

---

## Install via `pip`

Installing via `pip` is the quickest and most recommended method.

```bash
pip install social-media-downloader
```

Once installed, you can run the downloader using:

```bash
social-media-downloader
```

Or, if you're using version **1.1.4** or newer:

```bash
smd
```

!!! warning
    The `smd` shortcut is only available in versions `v1.1.4` and above.

---

## Install on Windows via `.exe`

!!! info
    No Python required — just download and run!

1. Visit the [Releases](https://github.com/nayandas69/Social-Media-Downloader/releases/latest) page.
2. Download the latest `.exe` file.
3. Double-click to launch the terminal interface.

---

## Install on Linux via `.deb`

For Debian/Ubuntu-based distributions:

1. Download the `.deb` package from the [Releases](https://github.com/nayandas69/Social-Media-Downloader/releases/latest).
2. Install it using:

```bash
sudo dpkg -i social-media-downloader_VERSION_amd64.deb
sudo apt-get install -f
```

Once installed, run the tool with:

```bash
smd
```

!!! danger
    You may need to adjust your `$PATH` or shell environment for the CLI shortcut.

---

## Install on Linux via `.tar.gz` Binary

If you're using a non-Debian Linux distribution or prefer a portable install:

1. Download the `.tar.gz` binary from the [Releases](https://github.com/nayandas69/Social-Media-Downloader/releases/latest).
2. Extract it and make it executable:

```bash
tar -xvf smd-linux.tar.gz
chmod +x smd
./smd
```

---

## Summary of Installation Options

| Platform       | Method                                | Link                                                                       |
| -------------- | ------------------------------------- | -------------------------------------------------------------------------- |
| Universal      | `pip install social-media-downloader` | [PyPI](https://pypi.org/project/social-media-downloader)                   |
| Windows        | Standalone `.exe`                     | [Releases](https://github.com/nayandas69/Social-Media-Downloader/releases) |
| Linux (Debian) | `.deb` package                        | [Releases](https://github.com/nayandas69/Social-Media-Downloader/releases) |
| Linux (Other)  | `.tar.gz` binary                      | [Releases](https://github.com/nayandas69/Social-Media-Downloader/releases) |
| Developer      | From source (clone)                   | [GitHub Repo](https://github.com/nayandas69/Social-Media-Downloader)       |

!!! warning
    Ensure `ffmpeg` is installed on your system or the tool will not function.

---

## See Also

* [Usage Guide](./usage.md) – How to use the downloader after setup.
* [Build Instructions](./build.md) – Custom builds, silent mode, and icon integration.
* [Troubleshooting](./troubleshooting.md) – Fix setup issues or installation errors.
* [Release Archive](./archive.md) – Download previous versions or test builds.
* [FAQ](./faq.md) – Answers to common questions.
