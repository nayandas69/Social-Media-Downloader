---
title: ⚙️ Configuration Info
---

## Configuration File: `config.json`

When you run Social Media Downloader for the first time, the CLI automatically generates a configuration file called `config.json`. This file stores your personal tool settings and preferences locally.

!!! note
    The config file is created in the same directory where you launch the CLI. We recommend running the tool from your **Desktop** to keep things tidy. You can always customize the config later.

---

## Default Configuration

Here’s what the default `config.json` looks like:

```json
{
  "default_format": "show_all",
  "download_directory": "media",
  "history_file": "download_history.csv",
  "mp3_quality": "192"
}
```

### Key Settings Explained:

| Key                  | Description                                                                   |
| -------------------- | ----------------------------------------------------------------------------- |
| `default_format`     | Format selector — can be set to `mp4`, `mp3`, or `show_all` (default option)  |
| `download_directory` | Folder where downloaded files will be saved. Default is `media/`              |
| `history_file`       | CSV file to log your download history. Helps you track what you've downloaded |
| `mp3_quality`        | Bitrate quality (in kbps) for MP3 audio downloads. Default is `192`           |

---

## Customizing Your Settings

You can open and edit the `config.json` manually in any text editor (like VS Code, Notepad, etc.).

### Example Changes:

Want to download only MP3s to your `Downloads` folder at 320kbps? Your config might look like:

```json
{
  "default_format": "mp3",
  "download_directory": "C:/Users/YourName/Downloads",
  "history_file": "download_history.csv",
  "mp3_quality": "320"
}
```

!!! tip
    Make sure the folder you specify in `download_directory` exists — the tool won’t create nested directories automatically.

---

## Additional Files Created Automatically

When you run the tool, it also creates these helpful files in the same directory:

| File Name              | Purpose                                               |
| ---------------------- | ----------------------------------------------------- |
| `config.json`          | Stores your settings                                  |
| `media/`               | Default folder where downloaded files are saved       |
| `download_history.csv` | Tracks all your downloads for easy reference          |
| `downloader.log`       | Stores runtime logs and errors (useful for debugging) |

---

## No User Tracking

Social Media Downloader **does not track** or store any personal data. All files, logs, and configs are kept **locally on your machine**. Nothing gets sent to any server.

!!! important
    If you ever want to reset your settings, just delete the `config.json` file and it will be re-generated the next time you run the tool.

---

## Need Help?

If you’re not sure how to configure something, open a [Discussion](https://github.com/nayandas69/Social-Media-Downloader/discussions) or ask in the [Discord community](https://discord.gg/skHyssu). We’re here to help you!

---

Happy downloading!