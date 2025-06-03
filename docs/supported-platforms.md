---
title: ✅ Supported Platforms
---

# Supported Platforms

Social Media Downloader supports a wide variety of popular platforms and video types. Below is a detailed breakdown of what you can download from each platform — including support for MP4 (video) and MP3 (audio) formats.

---

## Powered by yt-dlp — Full Platform Support

This tool uses [**yt-dlp**](https://github.com/yt-dlp/yt-dlp) under the hood, so it supports **all sites yt-dlp supports** — not just the ones listed below.

[See the full list of supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

You can also extend support by editing the `allowed_domains` list in `downloader.py`.

---

## SMD – General Platform Support

| Platform     | Video (MP4) | Audio (MP3) | Notes                                   |
|--------------|-------------|-------------|-----------------------------------------|
| YouTube      | ✅ Yes       | ✅ Yes       | Only public videos & Shorts.                 |
| TikTok       | ✅ Yes       | ✅ Yes       | Only public Videos.                        |
| Instagram    | ✅ Yes       | ✅ Yes       | See special table below for details.  |
| Facebook     | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| X (Twitter)  | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| Twitch       | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| Snapchat     | ✅ Yes       | ✅ Yes       | Only public spotlight videos.              |
| Reddit       | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| Vimeo        | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| Streamable   | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| Pinterest    | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| LinkedIn     | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| BiliBili     | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| Odysee       | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| Rumble       | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| GameClips    | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| Snackvideo   | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| kwai         | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| IMDB         | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| Weibo        | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| Dailymotion  | ✅ Yes       | ✅ Yes       | Only public videos.                          |
| Tumblr       | ✅ Yes       | ✅ Yes       | Only public videos.                          |

---

## Special Instagram Support

| Content Type   | Video (MP4) | Audio (MP3)   | Notes                                |
|----------------|-------------|---------------|--------------------------------------|
| Reels          | ✅ Yes       | ✅ Yes       | Public reels only.                   |
| Posts          | ✅ Yes       | ✅ Yes       | Videos & Pictures posted to feed.               |
| Stories        | ❌ No        | ❌ No        | Not supported.                       |
| IGTV           | ✅ Yes       | ✅ Yes       | Where still available.               |
| Carousels      | ✅ Yes       | ✅ Yes       | Multi-video posts are supported.     |
| Private media  | ❌ No        | ❌ No        | Login/auth not supported.            |

---

## MP3 Audio Support

- MP3 download is supported for all platforms that offer a valid video stream.
- Converts video to audio using internal tools — no extra steps needed.
- Example: Downloading a YouTube video as `.mp3` is fully supported.

---

## Multi-Link Support

!!! danger
    Only supported Instagram.
    You can download **multiple links at once** in batch mode using a `.txt` file.

**How it works:**

1. Create a `.txt` file with one URL per line (example: `links.txt`)
2. Run the downloader and provide the file path when prompted.
3. The downloader will process each link one by one.


---

!!! important

    - Only **public content** is supported — no private/locked/paid videos.
    - If you want to improve a platform's support, check our [Contributing Guide](./contribute.md).
    - All binaries (EXE, .deb, etc.) are built via GitHub Actions. If you want to improve packaging, update the [CI workflow](https://github.com/nayandas69/Social-Media-Downloader/blob/main/.github/workflows/release.yml).

---

## OS Support (Tested)

| Platform | Supported OS Versions |
|----------|-----------------------|
| Windows  | Windows 10 and later  |
| Linux    | Ubuntu, Debian        |

---

## Need Help?

Need a platform added or having issues with one? Open an [Issue](https://github.com/nayandas69/Social-Media-Downloader/issues) — we love improving things with your help! You can also check our [FAQ](./faq.md) for common questions and troubleshooting tips. If you need further assistance, feel free to reach out to our community for support. We appreciate your feedback and suggestions! We are always looking to improve our platform support and user experience. Thank you for using Social Media Downloader!