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
- [x] X (Twitter)
- [x] Twitch
- [x] Snapchat
- [x] Reddit
- [x] Vimeo
- [x] Streamable
- [x] Pinterest  
- [x] LinkedIn 
- [x] BiliBili 
- [x] Odysee 
- [x] Rumble 
- [x] GameClips  **(New!)**
- [x] Triller  **(New!)**
- [ ] Other platforms *(Not yet)*
- [ ] Private content *(Not yet)*
- [ ] Playlist support *(Not yet)*

## Features

- [x] Multiple Platforms – YouTube, Instagram & more
- [x] Batch Downloads – Download multiple links at once ( only public links Instagram)  
- [x] Choose Formats – MP4, MP3, or whatever you vibe with   
- [x] History Log – Keeps track of what you downloaded  
- [x] Update Checker – Always stay fresh with the latest version  
- [x] Interactive CLI – Easy to use, even for non-techies

## Preview
![Preview](https://raw.githubusercontent.com/nayandas69/Social-Media-Downloader/refs/heads/main/assets/1.1.0.gif)

## Usage

### Clone this repo (Recommended)
```bash
git clone https://github.com/nayandas69/Social-Media-Downloader.git
```

Then navigate to the directory:
```bash
cd Social-Media-Downloader
```

### Recommended (Create a virtual environment)

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

## Requirements Must Be Installed

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

### Install via PIP (Python Users Only)
> [!NOTE]
> You need to have Python 3.7 or higher installed on your system.
> If you don't have Python, please install it from [python.org](https://www.python.org/downloads).
> If you are using Windows, make sure to check the box "Add Python to PATH" during installation.
> If you are using Linux, make sure to install `python3-pip` and `python3-venv`.
> Then run the following command to install the tool:

```bash
pip install social-media-downloader
```
Then just run from anywhere:
```bash
social-media-downloader
```
also you can run it shortcut command `smd`
```bash
smd
```
If you want to update to the latest version, run:
```bash
pip install --upgrade social-media-downloader
```

### Install via .deb package
> [!NOTE]
> This is only for Debian-based systems (like Ubuntu).
> If you are using other Linux distros, please use the prebuilt binaries or build from source.

1. Download the `.deb` file from [Releases](https://github.com/nayandas69/Social-Media-Downloader/releases/latest)
2. Open a terminal and navigate to the directory where you downloaded the file.
3. Run the following command:
```bash
sudo dpkg -i social-media-downloader_VERSION_amd64.deb
```
4. If you get any dependency errors, run:
```bash
sudo apt-get install -f
```
5. After installation, you can run the tool by typing `smd` in the terminal.
6. To uninstall, run:
```bash
sudo apt-get remove social-media-downloader
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
> Note: These builds are not signed, so you may get a warning from Windows Defender or your antivirus. If you get a 
  warning, click "More Info" and then "Run Anyway".
> This is normal for unsigned builds. You can safely ignore it and run the EXE.
> If you are not sure about the build, please build it from source using the [Instructions](https://github.com/nayandas69/Social-Media-Downloader/blob/b1e4c9b8dc44e072167938c7eff306f8818f09eb/Instructions.md) above.
> We are not responsible for any issues caused by using untrusted builds.
> DO NOT use modified EXE/Binaries files outside this repository. For your security, only use trusted builds.

### 🪟 Windows EXE (Prebuilt)
1. Download the EXE from [Releases](https://github.com/nayandas69/Social-Media-Downloader/releases)  
2. Double-click & run like a normal app
3. Boom! You're ready to download videos!


### 🐧 Prebuilt Linux Binaries
Download the `smd-linux.tar.gz` from [Releases](https://github.com/nayandas69/Social-Media-Downloader/releases) and:
```bash
tar -xvzf smd-linux.tar.gz
sudo chmod +x smd
./smd
```

## Visit SMD Web Portal to Download the EXE or Binaries
> [!NOTE]
> This is a web portal to download the EXE or Binaries files.
> You can also use the web portal to download the latest version of the tool.
> The web portal is hosted on GitHub Pages and is updated automatically whenever a new version is released.

Check out the official page: [nayandas69.github.io/Social-Media-Downloader](https://nayandas69.github.io/Social-Media-Downloader)

## How to Use

1. Run the tool (either via command line or double-click the EXE)
2. Select the platform you want to download from (YouTube, Instagram, etc.)
3. Paste the **public link** of a video
4. Choose output format ID available like `625` (or type `mp3` for audio-only)
5. Sit back and let the tool work its magic!
6. Wait for the download to finish (it’ll show you the progress)
7. Batch download? No problem! Just follow these steps:
   - Create a `.txt` file with each URL on a new line
   - For batch download, enter the path to your `.txt` file containing URLs.
   - For example: `C:\path\to\batch_links.txt` or `/home/user/batch_links.txt`
8. Find your downloaded files in the same directory as the tool
9. Enjoy your videos!

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
> - Violate **YouTube, Instagram, Facebook, TikTok or other social media** TOS
> I'm not responsible if you break the rules. **Use this ethically and responsibly!**

### Read More:
- [FAQ](https://github.com/nayandas69/Social-Media-Downloader/blob/main/faq.rst)
- [License](https://github.com/nayandas69/Social-Media-Downloader/blob/main/LICENSE)
- [What's New](https://github.com/nayandas69/Social-Media-Downloader/blob/main/whats_new.md)
- [Change Log](https://github.com/nayandas69/Social-Media-Downloader/blob/main/CHANGELOG.md)
- [Instructions](https://github.com/nayandas69/Social-Media-Downloader/blob/main/Instructions.md)
- [Contributing](https://github.com/nayandas69/Social-Media-Downloader/blob/main/.github/CONTRIBUTING.md)
- [CONTRIBUTORS.md](https://github.com/nayandas69/Social-Media-Downloader/blob/main/docs/CONTRIBUTORS.md)

## Planned & Current Features

### Completed
- [x] CLI Interface
- [x] MP4 / MP3 support
- [x] Batch mode
- [x] Update checker
- [x] Linux/Windows support
- [x] PyPI packaging
- [x] Basic EXE & binary build
- [x] Facebook, Instagram, YouTube, TikTok, X
- [x] Snapchat, Reddit, Vimeo, Streamable & Pinterest
- [x] LinkedIn, BiliBili, Odysee, Rumble, GameClips & triller
- [x] Instagram Reels & Videos Audio download

### In Progress / Planned
- [ ] GUI Interface **(Next Comming Soon!)**
- [ ] Web Interface **(Next Comming Soon!)**
- [ ] macOS support
- [ ] Other platforms
- [ ] Proxy support
- [ ] Playlist support

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
**Your support means the world to me!**

> **Disclaimer:**  
> This tool is not affiliated with or endorsed by YouTube, TikTok, Instagram, Facebook, X, or other social media. Use at your own discretion.
