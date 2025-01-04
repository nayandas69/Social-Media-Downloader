# Social Media Downloader

## Overview  
**Social Media Downloader** is a versatile tool designed to download videos and posts from popular platforms like YouTube, TikTok, Instagram, and Facebook. It provides an intuitive CLI interface for Windows, and Linux users and is also available on PyPI for easy installation via `pip`.  

This tool is intended for **personal use only**. Unauthorized downloading of copyrighted material is prohibited.  

---

## Key Features  
- **Platform Support**:  
  - Download videos from **YouTube**, **TikTok**, and **Facebook**.  
  - Download posts from **Instagram**.  
- **Batch Download**: Download multiple URLs in one go using a text file.  
- **Update Checker**: Keep the software updated with the latest features and fixes.  
- **Customizable**: Configure download directory and format preferences.  
- **Platform Compatibility**:  
  - Windows CLI support with `.exe` file.  
  - Linux CLI support via terminal commands.  
  - Python users can install it using `pip`.  

---

## Installation  

### Option 1: Install via PyPI (Python 3.7+ required)  
```bash
pip install social-media-downloader
```

### Option 2: Download Executable for Windows  
1. Visit the **[Latest Releases](https://github.com/nayandas69/Social-Media-Downloader/releases/latest)** page.  
2. Download the `.exe` file.  
3. Run the executable directly via command prompt or double-click to start.  

### Option 3: Use on Linux  
1. Download the appropriate binary from the **[Latest Releases](https://github.com/nayandas69/Social-Media-Downloader/releases/latest)** page.  
2. Extract the downloaded archive:  
   ```bash
   unzip SocialMediaDownloader_latest_Linux.zip # Linux
   ```
   Or
   ```bash
   tar -xzvf SocialMediaDownloader_latest_Linux.tar.gz  # Linux
   ```  
3. Run the binary:  
   ```bash
   ./SocialMediaDownloader_latest
   ```  

---

## Requirements  

### FFmpeg Installation  
FFmpeg is required for video/audio conversion. Below are the platform-specific installation instructions:  

#### **Windows**  
1. Download FFmpeg from the official website: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).  
2. Extract the downloaded zip file to a folder (e.g., `C:\ffmpeg`).  
3. Add FFmpeg to your system PATH:  
   - Open "Environment Variables" from System Properties.  
   - Under "System Variables", find `Path`, click "Edit", and add the path to the `bin` folder (e.g., `C:\ffmpeg\bin`).  
4. Verify the installation by running:  
   ```cmd
   ffmpeg -version
   ```  

#### **Linux**  
Install FFmpeg using your distribution's package manager:  
- **Ubuntu/Debian**:  
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```  
- **Fedora/RHEL**:  
  ```bash
  sudo dnf install ffmpeg
  ```  
- **Arch Linux**:  
  ```bash
  sudo pacman -S ffmpeg
  ```  

#### **macOS**  
Use Homebrew to install FFmpeg:  
1. Install Homebrew if not already installed:  
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```  
2. Install FFmpeg:  
   ```bash
   brew install ffmpeg
   ```  
3. Verify the installation:  
   ```bash
   ffmpeg -version
   ```  

### Verifying FFmpeg in the Tool  
The downloader will check for FFmpeg during runtime. If it is missing, the tool will display a prompt with platform-specific installation instructions.  

---

## Usage  

### Running the Tool  
For all platforms:  
```bash
social-media-downloader
```  

Alternatively, on Windows:  
```bash
SocialMediaDownloader_latest.exe
```  

### Features and Options  
1. **Download YouTube/TikTok Video**: Provide the video URL to download in your desired format.  
2. **Download Facebook Video**: Enter the video URL to download directly.  
3. **Download Instagram Post**: Provide the Instagram post URL to save it locally.  
4. **Batch Download**: Provide a text file containing URLs (one per line).  
5. **Check for Updates**: Ensure you are using the latest version.  
6. **Help**: Learn more about using the tool.  

---

## Configuration  
Modify the `config.json` file to customize:  
- **Default Download Directory**  
- **Default History File**  
- **Default Format Behavior**  

---

## Logs and History  
- All downloads are logged in `downloader.log`.  
- A detailed history of downloads is saved in `download_history.csv`.  

---

## Disclaimer  
This software is intended for **personal use only**. Downloading content without the permission of the content owner may violate copyright laws. The developer is not responsible for any misuse of this tool.  

---

## Troubleshooting and Support  
If you encounter any issues or have feature requests:  
- Contact the author: **Nayan Das**  
- Email: **nayanchandradas@hotmail.com**  
- Website: [https://socialportal.nayanchandradas.com](https://socialportal.nayanchandradas.com)  
- Report issues on [GitHub Issues](https://github.com/nayandas69/Social-Media-Downloader/issues).  

Enjoy using Social Media Downloader! 🎉  
