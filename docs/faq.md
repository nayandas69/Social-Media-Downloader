---
title: ❓ Frequently Asked Questions
---

Welcome to the FAQ section for **Social Media Downloader**! This page addresses the most common questions to help you use the tool effectively and confidently.

---

### What is Social Media Downloader

**Social Media Downloader** is a lightweight, open-source command-line tool that allows you to download public videos, reels, and posts from platforms like YouTube, TikTok, Instagram, Facebook, and more. It supports batch downloads and works across different operating systems.

---

### Supported Platforms

The tool currently supports content from:

- **YouTube**
- **TikTok**
- **Instagram**
- **Facebook**

See the [Supported Platforms](./supported-platforms.md) page for more information.

!!! tip
    Support for additional platforms is planned in future updates.

---

### Is It Free to Use?

Yes! The tool is completely free and open-source under the [MIT License](https://github.com/nayandas69/Social-Media-Downloader/blob/main/LICENSE). You are free to view, modify, and distribute it.

---

### Private or Password-Protected Content

The tool is designed strictly for downloading **public** content.

!!! warning
    It does not support downloading private or password-protected media, ensuring user privacy and compliance with platform rules.

---

### Installation

You can install it using `pip`:

```bash
pip install social-media-downloader
```

Or clone the repository:

```bash
git clone https://github.com/nayandas69/Social-Media-Downloader.git
cd Social-Media-Downloader
```

See the [Installation Guide](./installation.md) for complete instructions.

---

### How to Use

Run the tool with:

```bash
social-media-downloader
```

Or, from version `1.1.4+`, simply use:

```bash
smd
```

Follow the prompts to enter the URL of the content you want to download.

---

### Supported File Formats

The tool supports formats like:

* [x] MP4 (video)
* [x] MP3 (audio)
* [x] IMG (Only Instagram)    

You’ll be able to choose your preferred format during download.

---

### Batch Downloads

You can download multiple videos at once — especially for Instagram.

!!! danger
    Batch downloading currently supports **Instagram** only.

---

### Is There a GUI?

Not yet. The tool is currently CLI-based.

!!! tip
    A graphical user interface (GUI) may be introduced in a future release.

---

### How to Update

If installed via `pip`, update it using:

```bash
pip install --upgrade social-media-downloader
```

For other methods, see the [Installation Guide](./installation.md).

---

### Fixing "ModuleNotFoundError" with `pyfiglet`

This occurs when `PyInstaller` doesn’t bundle font files. Here's how to fix it:

1. Generate a spec file:

   ```bash
   pyi-makespec --onefile smd/downloader.py
   ```

2. Edit the `.spec` file to include:

   ```python
   from PyInstaller.utils.hooks import collect_data_files
   datas = collect_data_files("pyfiglet")
   ```

3. Rebuild:

   ```bash
   pyinstaller downloader.spec
   ```

More help is in the [Troubleshooting Guide](./troubleshooting.md).

---

### Supported Operating Systems

The tool works on:

* **Windows** (via `.exe`)
* **Linux** (via binaries or `.deb`)

---

### Contributing

We welcome all contributions! Fork the repo, make changes, and submit a pull request.

!!! tip
    Check the [Contributing Guide](./contribute.md) for easy steps to get started.

---

### Reporting Bugs or Requesting Features

Please use the [GitHub Issues Page](https://github.com/nayandas69/Social-Media-Downloader/issues) to submit bug reports or feature requests.

---

### Changelog

View the [Changelog](./changelog.md) to track updates, improvements, and bug fixes.

---

### Legal Notice

The tool is for downloading **public content** only.

!!! danger
    Downloading copyrighted material without permission may violate local laws. Use responsibly.

---

### No Python? No Problem

You can use the tool without installing Python by downloading a standalone executable from the [Releases Page](https://github.com/nayandas69/Social-Media-Downloader/releases) or see the [archive](./archive.md).

---

### How to Uninstall

If installed via `pip`:

```bash
pip uninstall social-media-downloader
```

See the [Installation Guide](./installation.md) for other methods.

---

### Support for Stories and Live Videos

Currently, only standard posts and videos are supported. Stories and live videos are not available.

---

### Download Location

By default, all content is saved to a folder named `media` in your current directory.

You can customize this via `config.json`.

---

### About `config.json`

This file is created the first time you run the tool and stores default settings like:

```json
{
  "default_format": "show_all",
  "download_directory": "media",
  "history_file": "download_history.csv",
  "mp3_quality": "192"
}
```

!!! tip
    You can manually edit this file to change download paths or audio quality.

!!! danger
    A new `config.json`, `media` folder, and `download_history.csv` will be created if you run the tool from a different directory.

---

### Changing MP3 Quality

Edit the `"mp3_quality"` field in `config.json`:

```json
"mp3_quality": "320"
```

!!! tip
    Make sure `ffmpeg` is installed for audio conversions.

---

### Download History

The `download_history.csv` file logs all your downloads with timestamps, formats, and URLs — useful for tracking.

---

### Log File

`downloader.log` captures error messages and failed downloads — helpful for debugging issues.

---

### Privacy and Data Collection

**Your privacy matters.** The tool does **not**:

* [x] Send URLs or metadata to a server
* [x] Use telemetry
* [x] Collect any personal data

Everything stays 100% local.

---

### Offline Use

You can use the tool offline after installation, but downloads still require an internet connection.

---

### Libraries Used

* [x] `yt-dlp`
* [x] `instaloader`
* [x] `ffmpeg-python`
* [x] `tqdm`, `requests`, `pyfiglet`, `termcolor`, `tabulate`

See `requirements.txt` for the full list.

---

### Dependency Safety

All libraries are from trusted, open-source repositories.

---

### Build Your Own Executable

See the [Build Instructions](./build.md) to compile your own `.exe` or binary.

---

### Why Trust This Tool?

* [x] MIT License
* [x] No tracking or telemetry
* [x] 100% open-source and local
* [x] Auditable codebase
* [x] GitHub Actions for builds

---

### Want to Contribute But Not Sure Where to Start?

Start by fixing typos, improving docs, or reviewing code. See the [Contributing Guide](./contribute.md).

---

### Using a `.txt` File for Batch Links

Yes, just list one URL per line in a `.txt` file.

!!! warning
    Currently supported for **Instagram** only.

---

### Update Behavior

The tool checks GitHub Releases and notifies you if a new version is available.

!!! note
    It does **not** update automatically — you must do it manually.

---

### Docker Support

A Docker image for **version `1.1.7`** is available on [GitHub Container Registry](https://github.com/nayandas69/Social-Media-Downloader/pkgs/container/social-media-downloader).

!!! info
    Only version `1.1.7` is currently available. Future versions may be added manually via the GitHub Actions workflow.

### ARM / Raspberry Pi Support

Yes, as long as `ffmpeg` and Python are installed for your architecture.

---

### Can I Customize Filenames?

Not directly yet, but you can modify the source code if needed.

---

### Should I Run as Root?

No, there’s no need to run the tool with elevated privileges.

---

### Playlist / Channel Support

Currently not available. Only individual videos or `.txt` batch input is supported.

---

### Where to Get Help

* **Bugs** → [Issues Page](https://github.com/nayandas69/Social-Media-Downloader/issues)
* **General questions** → [Discussions](https://github.com/nayandas69/Social-Media-Downloader/discussions)
* **More help** → [Troubleshooting Guide](./troubleshooting.md)

---

Thanks for using Social Media Downloader! We hope this FAQ makes your experience easier and smoother.
