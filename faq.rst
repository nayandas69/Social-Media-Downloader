===========================
Frequently Asked Questions
===========================

What is Social Media Downloader?
===============================

Social Media Downloader is an open-source Python-based tool that allows users to download videos and media from supported public social media links such as YouTube, Instagram, TikTok, and others.

It supports multiple formats (MP4, MP3, etc.), batch downloads, and even comes with a standalone EXE or Linux binary for non-technical users.

How do I install the tool?
===========================

You can install the tool in multiple ways:

**1. Clone and Run via Python:**

.. code-block:: bash

    git clone https://github.com/nayandas69/Social-Media-Downloader.git
    cd Social-Media-Downloader
    pip install -r requirements.txt
    python downloader.py

**2. Install via pip (Recommended for Python users):**

.. code-block:: bash

    pip install social-media-downloader
    smd

**3. Use the EXE or Linux Prebuilt Binary:**

- Download the appropriate file from the `Releases` section:
  https://github.com/nayandas69/Social-Media-Downloader/releases
- For Linux, unzip the `.tar.gz` file and make the binary executable:

.. code-block:: bash
    tar -xvzf smd-linux.tar.gz
    sudo chmod +x smd
    ./smd

Note: These binaries are **not recommended** for development or advanced use. Building your own is preferred.

How to use the downloader?
===========================

After running the tool (`python downloader.py` or `social-media-downloader`), you'll see a simple CLI interface:

**Steps:**
1. Choose the platform (YouTube, Instagram, etc.) from the list.
2. Enter the URL of the video you want to download.
   - For batch download, enter the path to your `.txt` file containing URLs.
   - For example: `C:\path\to\batch_links.txt` or `/home/user/batch_links.txt`
3. Choose output format ID available `625` (or type `mp3` for audio-only)
4. Wait for the download to complete!

The downloaded files will be saved in the `downloads/` folder inside the same directory.

Can I download in batch mode?
=============================

Yes, but **batch download is currently supported only for Instagram**.

To use batch mode, create a `.txt` file containing public Instagram URLs (one per line), for example:

.. code-block:: text

    https://www.instagram.com/p/XYZ123/
    https://www.instagram.com/reel/ABC456/

Save it as `batch_links.txt` in the root directory of the tool (or provide the full path).

Then, run the tool and choose the batch download option. Make sure your file path is correct.

What are the supported platforms?
==================================

Tested and supported platforms:

- ✅ Windows 11 / 10
- ✅ Kali Linux, Parrot OS
- ⛔ macOS: Not tested (support may vary)

Can I build my own EXE or binary?
==================================

Yes! You can build your own EXE or Linux binary using PyInstaller:

**Windows:**

.. code-block:: bash

    pyinstaller --onefile downloader.py
    pyinstaller --onefile --noconsole downloader.py  # Silent mode
    python -m PyInstaller --onefile --icon=assets/logo.ico downloader.py  # With icon

**Linux:**

.. code-block:: bash

    pyinstaller --onefile downloader.py

Then find the output in the `dist/` directory.

Why is FFmpeg required?
========================

FFmpeg is used to convert or merge video/audio formats. It is **required** for proper downloading and format support.

The tool will automatically check if FFmpeg is available.

**Install FFmpeg:**

- Windows: Download from https://ffmpeg.org/download.html and add it to PATH.
- Linux: Use your package manager:

.. code-block:: bash

    sudo apt install ffmpeg

Can I install Social Media Downloader using a `.deb` file?
===========================================================

Yes! We provide `.deb` packages for Linux users.

Download the `.deb` file from the `Releases` section:
https://github.com/nayandas69/Social-Media-Downloader/releases

To install:

.. code-block:: bash

    sudo dpkg -i social-media-downloader_<version>_amd64.deb
    sudo apt-get install -f  # To fix any missing dependencies

This will install the tool system-wide as a global command: `smd`


Does the `.deb` package include all dependencies?
==================================================

The `.deb` package contains only the compiled `smd` binary.

It does **not install Python libraries** like `yt-dlp`, `requests`, or `instaloader` — but don't worry!

All dependencies are **already bundled** into the binary using PyInstaller.  
So you **do not need to install them manually**.

However, **FFmpeg is required** and must be installed separately:


.. code-block:: bash

    sudo apt install ffmpeg


How do I run the tool after installing the `.deb` package?
===========================================================

Once installed via `.deb`, simply open your terminal and run:

.. code-block:: bash

    smd

You will see the same CLI interface and functionality as with the Python version or EXE.

Can I download private videos or login to an account?
======================================================

No. **This tool only works with public URLs.**

> You cannot download private, age-restricted, or login-required content.

Is this tool safe/legal to use?
================================

The tool is intended for **educational and personal use only**.  
Do not use it to violate the terms of service of any platform.

The developer is **not responsible** for any misuse of this tool.

---

Have more questions?
=====================

- GitHub: https://github.com/nayandas69/Social-Media-Downloader
- Discord Support: https://discord.gg/skHyssu
- Contact: nayanchandradas@hotmail.com
