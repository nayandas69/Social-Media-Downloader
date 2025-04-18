# Social Media Downloader

A powerful and easy-to-use tool to download public videos from your favorite social media platforms. Whether you're on Windows or Linux, technical or not — we've got you covered. Download in batches, choose your formats, and even use it as a command-line tool or standalone app. Built with **love**, **open-source**, and fully community-driven. **100% Free** (but hey, [a coffee wouldn’t hurt!](https://www.patreon.com/nayandas69))

> [!NOTE]
> This tool only supports **public** links. It does **not** work on private or restricted content.
> If you try to use it on private content, it will throw an error.
> **Please respect the privacy of others.**

![Workflow Status](https://img.shields.io/github/actions/workflow/status/nayandas69/Social-Media-Downloader/python-package.yml?style=flat-square&color=4DB6AC&logo=github)
![Python Version](https://img.shields.io/pypi/pyversions/social-media-downloader?style=flat-square&color=blueviolet&logo=python&logoColor=white)
![Version](https://img.shields.io/pypi/v/social-media-downloader?style=flat-square&color=green&logo=pypi&logoColor=white)
![Total Downloads](https://static.pepy.tech/badge/social-media-downloader)
![License](https://img.shields.io/github/license/nayandas69/Social-Media-Downloader?style=flat-square&color=blue&logo=github&logoColor=white)

## Supported Social Media Platforms
- [x] YouTube  
- [x] TikTok  
- [x] Instagram  
- [x] Facebook  
- [x] X (Twitter) *(New)*   
- [ ] Other platforms *(Not yet)*
- [ ] Private content *(Not yet)*
- [ ] Playlist support *(Not yet)*

## Features

- [x] Batch Downloads – Download multiple links at once ( only public links Instagram)  
- [x] Choose Formats – MP4, MP3, or whatever you vibe with   
- [x] History Log – Keeps track of what you downloaded  
- [x] Update Checker – Always stay fresh with the latest version  
- [x] Interactive CLI – Easy to use, even for non-techies

## Preview
![Preview](assets/1.0.8.gif)

## Usage

### Clone this repo (Recommended)
```bash
git clone https://github.com/nayandas69/Social-Media-Downloader.git
```

Then navigate to the directory:
```bash
cd Social-Media-Downloader
```

### Create a virtual environment (optional but recommended)

# Windows
```bash
python -m venv .venv            # (Recommended)
.venv\Scripts\activate
pip install -r requirements.txt
python downloader.py
```

# Linux
```bash
python3 -m venv .venv            # (Recommended)
source .venv/bin/activate
pip3 install -r requirements.txt
python3 downloader.py
```

## 🧩 Requirements

### Install FFmpeg

- **Windows**  
  Download from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)  
  Add the bin path to your system environment variables.

- **Linux**
```bash
sudo apt update
sudo apt install ffmpeg
```

## Installation Options

### 🔌 Install via PIP (Python Users)
```bash
pip install social-media-downloader
```
Then just run from anywhere:
```bash
social-media-downloader
```
If you want to update to the latest version, run:
```bash
pip install --upgrade social-media-downloader
```

## Prebuilt Binaries & EXE
> [!WARNING]
> Use them at your own risk.
> These are prebuilt binaries and EXE files.
> For EXE/Binaries don't forget to install FFmpeg.
> Always use the latest version from the Releases page.
> If you have any issues, please open an issue on GitHub.
> Prebuilt binaries & exe don't require Python or any dependencies.
> Just download and run!
> Note: These builds are not signed, so you may get a warning from Windows Defender or your antivirus.
> This is normal for unsigned builds. You can safely ignore it and run the EXE.
> If you are not sure about the build, please build it from source using the [Instructions](Instructions.md) above.
> We are not responsible for any issues caused by using untrusted builds.
> DO NOT use modified EXE/Binaries files outside this repository. For your security, only use trusted builds. If you get a warning, click "More Info" and then "Run Anyway".

### 🪟 Windows EXE (Prebuilt)
1. Download the EXE from [Releases](https://github.com/nayandas69/Social-Media-Downloader/releases)  
2. Double-click & run like a normal app




### 🐧 Prebuilt Linux Binaries
Download the `smd-linux.tar.gz` from [Releases](https://github.com/nayandas69/Social-Media-Downloader/releases) and:
```bash
tar -xvzf smd-linux.tar.gz
sudo chmod +x smd
./smd
```

## 🌐 Visit Our SMD Web Portal

Check out the official page: [nayandas69.github.io/Social-Media-Downloader](https://nayandas69.github.io/Social-Media-Downloader)

## How to Use

1. Run the tool (either via command line or double-click the EXE)
2. Paste the **public link** of a video
3. Choose output format ID available like `625` (or type `mp3` for audio-only)
4. Sit back and let the tool work its magic!
5. Wait for the download to finish (it’ll show you the progress)
6. Batch download? No problem! Just follow these steps:
   - Create a `.txt` file with each URL on a new line
   - For batch download, enter the path to your `.txt` file containing URLs.
   - For example: `C:\path\to\batch_links.txt` or `/home/user/batch_links.txt`
7. Find your downloaded files in the same directory as the tool
8. Enjoy your videos!

## Tested Platforms

- [x] Windows 11
- [x] Windows 10
- [x] Kali Linux
- [x] Parrot OS
- [ ] macOS *(Not tested)*
- [ ] Other Linux Distros *(Should work but not tested)*

## Legal & Ethical Use
> [!WARNING]
> **READ THIS BEFORE USING!**
> This tool is for **PERSONAL USE ONLY** and only works with **public** videos. You **CANNOT** use it to:
> - Download **private, copyrighted, or restricted** content
> - Repost videos without credit (be a decent human, c’mon)
> - Violate **YouTube, Instagram, Facebook, or TikTok** TOS
> I'm not responsible if you break the rules. **Use this ethically and responsibly!**

### Read More:
- [FAQ](faq.rst)
- [License](LICENSE)
- [What's New](whats_new.md)
- [Change Log](CHANGELOG.md)
- [Instructions](Instructions.md)
- [Contributing](.github/CONTRIBUTING.md)

## Planned & Current Features

### Completed
- [x] CLI Interface
- [x] MP4 / MP3 support
- [x] Batch mode
- [x] Update checker
- [x] Linux/Windows support
- [x] PyPI packaging
- [x] Basic EXE & binary build
- [x] Facebook, Instagram, YouTube, TikTok & X

### In Progress / Planned
- [ ] GUI Interface
- [ ] macOS support
- [ ] Proxy support
- [ ] Snapchat and other platforms

## Contributing & Support
> Have suggestions? We'd love to hear them!
> Open an issue on GitHub or join our Discord community.
> Your feedback is invaluable in making this tool even better!

Love the tool? Help improve it! Open an issue or PR on [GitHub](https://github.com/nayandas69/Social-Media-Downloader).

### Contact Me:
- Made by [Nayan Das](https://nayandas69.github.io/link-in-bio)
- Email: [nayanchandradas@hotmail.com](mailto:nayanchandradas@hotmail.com)
- Discord: [Join here!](https://discord.gg/skHyssu)

## Thank You, 4.7K+ Users!
This project is maintained by **[nayandas69](https://github.com/nayandas69)**.  
Thanks for downloading & supporting! Share your reviews and feedback.  
**Y’all are the real MVPs!**

> **Disclaimer:**  
> This tool is not affiliated with or endorsed by YouTube, TikTok, Instagram, Facebook or X. Use at your own discretion.
