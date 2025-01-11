from setuptools import setup, find_packages

# Read the README.md for a long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="social-media-downloader",
    version="1.0.4",
    author="Nayan Das",
    author_email="nayanchandradas@hotmail.com",
    author_website="https://nayanchandradas.com",
    description=(
        "✨ Snatch the hottest content from YouTube, TikTok, Instagram, & Facebook effortlessly! "
        "🚀💖 Whether it's viral vids, inspo reels, or iconic memes—this tool's gotchu covered. 🌟🔥"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nayandas69/Social-Media-Downloader",
    project_urls={
        "Bug Tracker": "https://github.com/nayandas69/Social-Media-Downloader/issues",
        "Documentation": "https://github.com/nayandas69/Social-Media-Downloader#readme",
        "Source Code": "https://github.com/nayandas69/Social-Media-Downloader",
        "Discord Community": "https://discord.gg/skHyssu",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Multimedia :: Video",
        "Topic :: Internet",
    ],
    keywords=[
        "social media downloader", "downloader", "youtube downloader",
        "tiktok downloader", "instagram downloader", "facebook downloader",
        "cli tool", "video downloader", "content saver",
    ],
    packages=find_packages(include=["*"], exclude=["tests*", "docs*"]),  # Finds all packages
    py_modules=["downloader"],  # Ensures main script is included
    python_requires=">=3.6",  # Compatible with Python 3.6+
    install_requires=[
        "yt-dlp>=2023.7.6",          # Download from YouTube and TikTok
        "instaloader>=4.10.0",       # Instagram scraping
        "beautifulsoup4>=4.12.2",    # Scraping FB video metadata
        "tqdm>=4.65.0",              # Progress bar
        "requests>=2.31.0",          # HTTP requests
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",           # For testing
            "flake8>=6.0",           # For linting
            "black>=23.1",           # Code formatting
        ],
    },
    entry_points={
        "console_scripts": [
            "social-media-downloader=downloader:main",  # Command for CLI
        ],
    },
    include_package_data=True,
    zip_safe=False,
    license="MIT",
)