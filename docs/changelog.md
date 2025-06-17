---
title: 🫨 Changelog
---

All the spicy updates, tweaks, and new vibes are logged here. 🌟  

---

## [1.1.9] - 2025-06-18

## New Platform Support
We added support for more platforms! You can now download videos from:
- `bsky.app`


## New Scripts
> [!IMPORTANT]
> - `install.sh` script for Linux users:  
> - This script will install the package and all dependencies automatically, making it easier for Linux users to get started. That helps you install `ffmpeg` and install Social Media Downloader with a single command & it also have update, uninstall functionality in same script.

Unit tests added for the main functions to ensure reliability and stability of the codebase.

## Fixes & Improvements

- **Fixed**:  
  - Format selection issues in the `download_youtube_or_tiktok_video(url)` function. [#50](https://github.com/nayandas69/Social-Media-Downloader/issues/50)

  - `release.yml` add gpg signing to the release.

  - **added contributors section with graph** by [@nerdyboss](https://github.com/nerdyboss) pr [#41](https://github.com/nayandas69/Social-Media-Downloader/pull/41)

---

## [1.1.8] - 2025-05-21

* **New Platform Support**:
  We've added support for even more video platforms! You can now download videos from:

  * `imdb.com`
  * `weibo.com`
  * `dailymotion.com`
  * `tumblr.com`

  Big thanks to the community for the feature requests — keep 'em coming!

### Improvements

* **Configuration Loader Overhaul**
  The config loading system has been refactored to:

  * Auto-correct invalid or missing values
  * Validate supported formats and MP3 quality levels
  * Regenerate the config safely if corrupted
  * Log everything clearly to help you debug easily

* **Better Defaults & Validation**
  Now your config won't silently break — it heals itself and tells you what was fixed. Nice.

### Fixes

* Fixed occasional crash when using corrupted or incomplete `config.json`
* Corrected path handling for dynamic filenames in downloads
* Ensured `download_directory` is always created safely before use

### Heads Up

* If your config breaks or is outdated, don’t worry — we’ll auto-fix it and log everything clearly.
* Need more formats or platforms? Hit us up!

---

## [1.1.7] - 2025-05-12

### Fixes & Improvements
- Fixed `ModuleNotFoundError: No module named 'downloader'` by properly restructuring the project as a Python package (`smd/downloader.py`).
- Updated `pyproject.toml` entry points to:
```toml
  [project.scripts]
  smd = "smd.downloader:main"
  social-media-downloader = "smd.downloader:main"
```

* CLI scripts now work reliably across systems when installed via PyPI.

### How to Upgrade

To upgrade to the latest version, run:

```bash
pip install --upgrade social-media-downloader
```

Then use the CLI tool with:

```bash
smd
# or
social-media-downloader
```

---

## [1.1.6] - 2025-05-11
### Added
- Support for two new video platforms:
  - SnackVideo (`snackvideo.com`)
  - Kwai (`kwai.com`)

---

## [1.1.5] - 2025-05-10

### Fixes & Improvements
- **Fixed MP3 Quality Handling:**  
  The MP3 quality value (`mp3_quality`) from `config.json` is now properly validated and applied during audio downloads.  
  Previously, entering custom qualities like `256` or `396` wouldn't work correctly due to a bug — it's now fixed.

- **Corrected Format Selection Logic:**  
  The audio download process now correctly respects the selected `mp3_quality` value (e.g., 128, 192, 256, 320, 396) instead of defaulting silently or failing.

- **Stronger Validation:**  
  If an invalid `mp3_quality` value is provided (e.g., `60`), the app will fall back to the default `192` and show a warning in the logs.

### Config Updates
- The `config.json` now supports and validates the following MP3 qualities:  
  `64`, `128`, `192`, `256`, `320`, `396`.

---

## [1.1.4] - 2025-05-03

### Added
- New platform support for **GameClips** and **Triller**.
- New short command: After installing via pip the new version, you can use `smd` as a shortcut for `social-media-downloader`.

#### Improvements
- File structure has been improved for better organization and maintainability.

## Contributors Involved
- **Contributors**: [@mohinikhan123](https://github.com/mohinikhan123), her contribution to the project is greatly appreciated.
- [x] New Command: `smd` as a shortcut for `social-media-downloader`.
- [x] Better file structure for the project.

---

## [1.1.3] - 2025-05-01

### Added
- Introduced a new **Instagram** menu.
- Added support for **MP3 downloads** from Instagram videos and reels.
- Implemented a **format table display** for YouTube and TikTok, listing available video/audio formats in a structured way.
- Added new platform support for **Odysee** and **Rumble**.

### Fixed
- Resolved **MP3 download issues** in `download_youtube_or_tiktok_video(url)` affecting specific formats.
- No more Duplicate Format listings in the format table.
- Fixed **other minor functions** that were not behaving correctly.

---

## [1.1.2] -2025-04-22

### Added
- New platform support for **Linkedin** and **Bilibili**.

### Fixes
- version correctly update on pypi.

---

## [1.1.1] -2025-04-22

### Added
- Now new platform supports **Pinterest** for downloading videos.

### Packaging
- Support for .deb package installation.
- Added a .deb package for easy installation on Debian-based systems.

---

## [1.1.0] - 2025-04-20

### Added
- Support for new platforms: **Twitch**, **Snapchat**, **Reddit**, **Vimeo**, and **Streamable**.
- URL validation to ensure only links from supported platforms are accepted.

### Changed
- Help menu redesigned for better readability and structure.
- Improved error handling for batch downloads.

---

## [1.0.9] - 2025-04-18

### Added
- New **X (Twitter) Downloading**: Download posts from X (formerly Twitter). Only public videos are supported.

---

## [1.0.8] - 2025-04-18

### Added
- New **animated logo/splash** at startup  
- **FFmpeg presence checker** with prompt if not installed

> [!NOTE]  
> This release focuses purely on new enhancements. No bug fixes or other changes were made.

---

## [v1.0.7] - The TL;DR Version  
**Release Date**: February 18, 2025 

**FIXED ISSUES & BUG SQUASHING:**
**Batch Download from .txt Files** – Now supports bulk IG downloads effortlessly.  
**Sped-Up Processing** – Thanks to multi-threading, IG downloads are significantly faster.  

---

## [v1.0.5] - Cutie Biggest glow-up yet  
**Release Date**: February 11, 2025 

### **New Features:**  
- **YouTube/TikTok vids now ALWAYS include audio** (no more silent films, you're welcome).  
- **MP3 mode?** Just type `mp3`, and you get **crispy 192kbps audio** in seconds.  
- **Batch Insta Downloads** – Drop multiple URLs & let the bot do its thing.  
- **Update Checker 2.0** – Now actually tells you **when to update & how**.  
- **Help Menu got a makeover** – Less clutter, more clarity.  

### **Fixes & Tweaks:**  
- **Config file won't betray you anymore** – if corrupted, it **auto-fixes itself**.  
- **No more duplicate overwrites** – files get **auto-renamed** instead.  
- **Internet issues?** We **auto-retry** if your WiFi is moving sus.  
- **Better format selection for YouTube vids** – actually makes sense now.  
- **Cleaner logs & better error messages** – so you know *what* broke (and *why*).

---

## [v1.0.4] - The Evolution Era  
**Release Date**: January 11, 2025  

### **What’s Poppin’?**  
- **Discord Fam Invite**: You’re officially invited to join the squad for updates, beta tests, and vibing. [Click here to slide in](https://discord.gg/skHyssu).  
- **Internet Smarts**: No WiFi? No problem. Auto-detection for connection issues and seamless retries. **Patience is a virtue**, but downloads gotta hustle.  
- **Custom Audio Vibes**: MP3 quality is now adjustable in the config. Go for 192kbps or vibe low-key—it’s your jam.  
- 🕵️**Meta Detective for FB**: Facebook video downloader now works Sherlock mode, sniffing out videos in more sneaky spots.  

---

### **Leveling Up the Game**  
- **Progress You Can See**: No progress bar? Couldn’t be us. Get visuals while your downloads grind.  
- **Pause, Retry, Repeat**: Internet drop? We wait. You’re back? We pick up like nothing happened. **Relationship goals.**  
- **Batch Mode Zen**: The whole batch keeps grooving—even if a link is feeling a lil’ off. Smooth ops guaranteed.  

---

### **Bug Jailbreak Squad**  
- Squashed rare **YouTube format issues** messing with quality choices. HD or audio-only? You do you.  
- Fixed **batch mode timeout probs**. Keep ‘em coming, we got it now.  
- No more silent FB errors. Every glitch gets logged, every move accounted for.  

---

## [v1.0.1] - The Glow-Up Edition   
**Release Date**: January 10, 2025  

### **What’s New, Fam?**  
- **Snap Insta Reels**: Insta reels are now supported—download those aesthetic vibes with no sweat!  
- **Auto-Save Mode**: Forget manual clicks. Your downloads are now auto-saved to your preferred folder without interruptions.  

---

### **Better, Faster, Smoother**  
- **Speed Boost**: Optimized the downloader engine for 2x faster downloads. *Time is money, bb.*  
- **Smarter Batch Mode**: Got bad links? We skip ‘em now and keep the hustle going. No interruptions.  

---

### **Bug Killa Mode**  
- Fixed that annoying glitch with **Facebook downloads**. FB vids are back and better.  
- Squashed a rare issue where **batch mode** stopped mid-run. Smooth like butter now.  
- Updated **update checker**. No more false alarms. It’s 💯 accurate.  

---

## [v1.0.0] - The OG Drop  
**Release Date**: December 1, 2024  

### New Features  
- **Platform Support**:  
  - Download videos from **YouTube**, **TikTok**, and **Facebook**.  
  - Download posts from **Instagram**.  
- **Batch Download**: Download multiple URLs at once using a text file.  
- **Custom Format Selection**:  
  - Choose video or audio formats (e.g., MP4, MP3) for YouTube and TikTok downloads.  
- **Update Checker**: Automatically checks for new versions and provides easy update functionality.  
- **Download Logs and History**:  
  - Logs all activities in `downloader.log`.  
  - Maintains a history of downloads in `download_history.csv`.  
- **Cross-Platform CLI Support**:  
  - Windows `.exe` for easy execution.  
  - Linux binary for terminal users.  
- **PyPI Availability**: Installable via `pip` for Python users.  

### Improvements and Design  
- **User-Friendly Interface**:  
  - Simple menu-driven CLI interface for easy navigation.  
  - Progress bar integration for a smooth user experience.  
- **Configurable Settings**:  
  - JSON-based configuration file (`config.json`) for download directory and format preferences.  
- **FFmpeg Integration**: Handles video and audio conversions effortlessly.  

### Technical Notes  
- Requires Python 3.10+ for PyPI installation.  
- FFmpeg installation is necessary for proper functionality.

---

**Keep it chill, keep it legal.** 💌 Feedback? [Slide into the discussions](https://github.com/nayandas69/Social-Media-Downloader/discussions).  

---

Your downloads are vibin’ on a whole new level. Stay aesthetic. ✌️