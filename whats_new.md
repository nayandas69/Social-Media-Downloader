# What's New in Social Media Downloader v1.1.5

### MP3 Quality Fix
- Fixed a bug where custom `mp3_quality` values (e.g., 256, 320) were ignored.
- Now respects and validates values from `config.json`.

### Improved Validation
- Falls back to default `192` if invalid quality is set.
- Logs a warning for incorrect config values.

### Docs Moved!
All documentation is now hosted separately:  
[https://nayandas69.github.io/smd-docsite/](https://nayandas69.github.io/smd-docsite/)

New docs repo:  
[https://github.com/nayandas69/smd-docsite](https://github.com/nayandas69/smd-docsite)