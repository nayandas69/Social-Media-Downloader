# What's New in Social Media Downloader v1.1.7

## Fixes and Improvements
- 🔧 Fixed `ModuleNotFoundError` by restructuring code into a proper package (`smd/downloader.py`).
- 🔄 Updated CLI script entry points in `pyproject.toml` to:
  - `smd = "smd.downloader:main"`
  - `social-media-downloader = "smd.downloader:main"`

✅ Now you can run the tool with:
```bash
smd
# or
social-media-downloader
```

## Upgrade now:

```bash
pip install --upgrade social-media-downloader
```