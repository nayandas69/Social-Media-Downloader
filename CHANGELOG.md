# Changelog  

All notable changes to this project will be documented in this file.  

## [v1.0.0] - Initial Release  
**Release Date**: December 1, 2024  

### 🎉 New Features  
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

### 🚀 Improvements and Design  
- **User-Friendly Interface**:  
  - Simple menu-driven CLI interface for easy navigation.  
  - Progress bar integration for a smooth user experience.  
- **Configurable Settings**:  
  - JSON-based configuration file (`config.json`) for download directory and format preferences.  
- **FFmpeg Integration**: Handles video and audio conversions effortlessly.  

### 🛠️ Technical Notes  
- Requires Python 3.7+ for PyPI installation.  
- FFmpeg installation is necessary for proper functionality.  

---
