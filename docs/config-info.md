---
title: ⚙️ Configuration Guide
---

## Configuration File: `config.json`

When you launch **Social Media Downloader** for the first time, a configuration file named `config.json` is automatically generated. This file stores your personal settings and download preferences locally.

!!! note
    The `config.json` file is created in the same directory where you run the tool. We recommend launching the CLI from your **Desktop** or a clean folder for better file organization.

## Default Configuration

Here is the default content of the `config.json` file:

```json
{
  "default_format": "show_all",
  "download_directory": "media",
  "history_file": "download_history.csv",
  "mp3_quality": "192"
}
```

## Configuration Keys Explained

| Key                  | Description                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------- |
| `default_format`     | The preferred format for downloads. Choose `mp3`, a video quality like `720p`, or `show_all` |
| `download_directory` | The folder where downloaded files are saved (default: `media/`)                              |
| `history_file`       | CSV file used to keep track of download history                                              |
| `mp3_quality`        | MP3 bitrate quality in kbps (e.g. `192`, `320`, etc.)                                        |

## Video Quality Options (`default_format`)

You can set the `default_format` to a specific video resolution to automatically download the best available video at or below that quality:

* `"360p"` – Mobile-friendly, small file size
* `"480p"` – Standard definition (SD)
* `"720p"` – High definition (HD)
* `"1080p"` – Full HD (recommended for good balance)
* `"1440p"` – Quad HD (2K)
* `"2160p"` – Ultra HD (4K)

Or set to:

* `"mp3"` – For audio-only downloads
* `"show_all"` – Prompts you to select a format manually for each download

## MP3 Quality Options

When `default_format` is set to `"mp3"`, the tool uses `ffmpeg` to extract audio from videos. The `mp3_quality` setting determines the bitrate:

| Value | Quality               |
| ----- | --------------------- |
| `64`  | Low                   |
| `128` | Medium                |
| `192` | Default / Balanced    |
| `256` | High                  |
| `320` | Very High             |
| `396` | Maximum (rarely used) |

!!! tip
    Higher bitrates mean better audio quality — but also larger file sizes.

## Smart Config Handling (v1.1.8+)

Starting from **version 1.1.8**, there's no need to manually delete the `config.json` file if a setting is missing or invalid.

✅ The tool **automatically detects and resets** incorrect or missing values to safe defaults during startup.

## Manual Editing

You can open `config.json` in any text editor like **Notepad**, **VS Code**, or **Sublime Text** to make changes.

### Example: Auto-download MP3s to your Downloads folder

```json
{
  "default_format": "mp3",
  "download_directory": "C:/Users/YourName/Downloads",
  "history_file": "download_history.csv",
  "mp3_quality": "320"
}
```

!!! warning
    Make sure the folder you specify for `download_directory` **already exists**. The tool won’t create nested directories.

## For Users on v1.0.0 – v1.1.7

Older versions **do not automatically fix or regenerate** the config file. If you experience errors or missing settings:

🚫 **Delete your `config.json` manually**
✅ Relaunch the tool — it will create a fresh file with correct defaults.


## Other Auto-Created Files

| File Name              | Purpose                                                  |
| ---------------------- | -------------------------------------------------------- |
| `config.json`          | Stores your personal settings                            |
| `media/`               | Default folder for all downloads                         |
| `download_history.csv` | Keeps a record of every video/audio you’ve downloaded    |
| `downloader.log`       | Logs errors, messages, and download activity (debugging) |

## No Tracking or Analytics

Social Media Downloader **does not collect any personal data**. All logs, downloads, and settings are stored **locally on your own machine**. Nothing is sent to external servers.

## Need Help?

If you’re unsure about anything, feel free to:

* [Open a Discussion](https://github.com/nayandas69/Social-Media-Downloader/discussions)
* Join the [Discord community](https://discord.gg/skHyssu)

We’re here to help!

Happy downloading!