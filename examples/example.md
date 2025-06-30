# Examples — Social Media Downloader (`smd`)

This folder contains Python example scripts that demonstrate how to use the `social-media-downloader` package as an importable Python module.

## Requirements

Make sure you’ve installed version **`>=1.1.10`** of the package from PyPI:

```bash
pip install --upgrade social-media-downloader
````

Or install dependencies locally via:

```bash
pip install -r requirements.txt
```

& Run the example:

```bash
python3 examples/example-usage.py
```

### What it does:

* Downloads a YouTube or TikTok video
* Downloads an Instagram post
* Extracts MP3 from Instagram reel
* Downloads posts in bulk from `batch_links.txt`
* Checks for updates
* Loads and modifies config
* Logs downloads
* Deduplicates filenames


## Import Support (`import smd`)

As of version **`1.1.10`**, this package can be imported like any standard Python library:

```python
from smd import download_youtube_or_tiktok_video
```

This works seamlessly once installed via pip (`pip install social-media-downloader`), and you can integrate it in your own Python scripts, tools, or automation workflows.


If you're developing locally and want to import `smd` from source, use:

```bash
pip install -e .
```

Happy coding!
