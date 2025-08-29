<div align="center">

# Social Media Downloader

A fast, simple, and open-source tool to grab **public videos** from all your favorite platforms — including YouTube, TikTok, Instagram, Facebook, X and see all [supported platforms](https://nayandas69.github.io/Social-Media-Downloader/supported-platforms). Whether you're a techie or a casual user, this tool works seamlessly across **Windows** and **Linux**. Download single videos or entire batches, pick your desired format, and save content hassle-free. With a user-friendly command-line interface, you can easily download videos in just a few clicks.

![Workflow Status](https://img.shields.io/github/actions/workflow/status/nayandas69/Social-Media-Downloader/python-package.yml?style=flat-square&color=4DB6AC&logo=github)
![Python Version](https://img.shields.io/pypi/pyversions/social-media-downloader?style=flat-square&color=blueviolet&logo=python&logoColor=white)
[![Version](https://img.shields.io/pypi/v/social-media-downloader?style=flat-square&color=green&logo=pypi&logoColor=white)](https://pypi.org/project/social-media-downloader)
![Total Downloads](https://static.pepy.tech/badge/social-media-downloader)
![License](https://img.shields.io/github/license/nayandas69/Social-Media-Downloader?style=flat-square&color=blue&logo=github&logoColor=white)
[![Read Docs](https://img.shields.io/badge/docs-Read%20Docs-blue?style=flat-square&logo=githubpages&logoColor=white)](https://nayandas69.github.io/Social-Media-Downloader)    

</div>

> [!NOTE] 
> This tool **only works with publicly available videos**. It **cannot download private, restricted, or protected content**. Attempting to do so will result in an error.  
> Please use responsibly and respect content ownership and privacy.

## Intro
![Social Media Downloader](https://raw.githubusercontent.com/nayandas69/Social-Media-Downloader/4d0aebcc7433bb47bbfdce34b88ece1e7e41fd4f/docs/assets/intro.gif)

## Quick Start

### Clone the Repository
```bash
git clone https://github.com/nayandas69/Social-Media-Downloader.git
cd Social-Media-Downloader
```

## Requirements

> ✅ Before running the tool, make sure **FFmpeg** is installed:

### Install FFmpeg

* **Windows:**
  Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add bin folder to your **System PATH**.

* **Linux:**

```bash
sudo apt update
sudo apt install ffmpeg
```

## Install the Tool

<details>

<summary><strong>Click to expand the installation options for Social Media Downloader</strong></summary>

### Installation Options

| Platform   | Method              | Instructions                                                                                                  |
| ---------- | ------------------- | ------------------------------------------------------------------------------------------------------------- |
| Windows | Standalone `.exe`   | Download from [Releases](https://github.com/nayandas69/Social-Media-Downloader/releases), double-click to run |
| Linux   | `Binary` / `.deb`     | Use the `.deb` installer or download the `binary` for direct execution                                          |
| Universal | `pip` (recommended) | `pip install social-media-downloader`                                                                         |
| Manual  | From Source         | Clone repo → install deps → python smd/downloader.py                                                        |

</details>

> [!TIP]
> Choose the method that works best for your setup. Full guide: [Installation Guide](https://nayandas69.github.io/Social-Media-Downloader/installation)

## 📚 Full Documentation

Our complete user guide is available online:

**Docs:** [https://nayandas69.github.io/Social-Media-Downloader](https://nayandas69.github.io/Social-Media-Downloader)

### Highlights:

* [Requirements & Setup](https://nayandas69.github.io/Social-Media-Downloader/installation/)
* [Using the Downloader](https://nayandas69.github.io/Social-Media-Downloader/usage/)
* [Supported Platforms](https://nayandas69.github.io/Social-Media-Downloader/supported-platforms/)
* [Common Issues](https://nayandas69.github.io/Social-Media-Downloader/faq/)
* [Build & Troubleshooting](https://nayandas69.github.io/Social-Media-Downloader/build/)
* [Feature Roadmap](https://nayandas69.github.io/Social-Media-Downloader/roadmap/)

## Features

* **Multi-platform** support: YouTube, TikTok, Instagram, etc.
* **Batch downloads**: Just paste multiple links in a .txt file
* **Format options**: Choose between MP4, MP3, or ID-based formats
* **Download history** tracking
* **Update checker** built-in
* **Interactive CLI**: Beginner-friendly and simple to use
* Works on both **Windows** and **Linux**

## How It Works

1. Launch the tool (EXE or Python script)
2. Choose a platform (YouTube, Instagram, etc.)
3. Paste a **public video URL**
4. Select a format (e.g., `mp3`, `625`)
5. The tool handles the rest! You'll see real-time progress.
6. For **batch downloads**:

   * Create a `.txt` file with one URL per line
   * Provide the file path when prompted

Your videos will be saved in the same folder where the tool is located.

## Tested Environments

| OS          | Status         |
| ----------- | -------------- |
| Windows 11/10  | ✅ Tested       |
| Kali Linux / Parrot OS  | ✅ Tested       |
| macOS       | ⚠️ Not tested  |
| Other Linux | ⚠️ Should work |

## Legal & Usage Notice

> 🚫 This tool is provided for **educational and personal use only**. You **must not**:
>
> * Use it to download **private, copyrighted, or restricted** content
> * Violate any **Terms of Service** of the platforms supported
> * Re-upload or redistribute videos without proper permission or credit
>
> ❗ The developer is **not responsible** for how this tool is used. Please respect digital ownership and platform policies.

## Contributing

Have suggestions, bug reports, or ideas?
We welcome contributions!
👉 [Open an issue](https://github.com/nayandas69/Social-Media-Downloader/issues) or [submit a PR](https://github.com/nayandas69/Social-Media-Downloader/pulls)

Read the [Contribution Guide](https://github.com/nayandas69/Social-Media-Downloader/blob/dev/.github/CONTRIBUTING.md)

## Credits & Community

Made with ❤️ by [**Nayan Das**](https://nayandas69.github.io/link-in-bio)  
Email: [nayanchandradas@hotmail.com](mailto:nayanchandradas@hotmail.com)  
Join us on [Discord](https://discord.gg/skHyssu)  

🙌 Special thanks to all [contributors](https://github.com/nayandas69/Social-Media-Downloader/blob/dev/docs/contributors.md)

## Thank You — 7K+ Users and Growing!

If this tool helped you, show some love by ⭐ starring the repo or [Support](https://www.patreon.com/nayandas69)!
Your support keeps this project alive ❤️

> *This project is not affiliated with or endorsed by YouTube, TikTok, Instagram, Facebook, X or other platforms.*

## Full yt-dlp Support + Easy CLI Integration

This tool uses [**yt-dlp**](https://github.com/yt-dlp/yt-dlp) under the hood, so it supports **all sites yt-dlp supports** — not just the ones listed below.

**[Click here to view the full list of sites supported by yt-dlp](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)**

But we’ve gone a step further!
In `downloader.py`, we’ve added **CLI program support for the most commonly used social media platforms** (like YouTube, TikTok, Reddit, X, etc.) via an internal `allowed_domains` list.

This makes it easier for users to:

* Paste a URL from a popular site
* Automatically validate it
* Download videos or extract audio seamlessly

✅ All without needing to memorize complex flags or command-line options!

You can even expand support by **editing the `allowed_domains` list** inside the script. This makes it super customizable for your own needs.

## Built With

This tool wouldn't be possible without these amazing open-source projects:

* [**yt-dlp**](https://github.com/yt-dlp/yt-dlp)
* [**Instaloader**](https://github.com/instaloader/instaloader)

> **Huge thanks** to their developers and contributors for making this tool possible!

## License
This project is licensed under the [MIT License](LICENSE).
