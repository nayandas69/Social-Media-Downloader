from setuptools import setup, find_packages

# Read the README.md for a long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="social-media-downloader",
    version="1.0.7",
    author="nayandas69", # search me on github
    author_email="nayanchandradas@hotmail.com",
    description="Download videos from YouTube, TikTok, Instagram, and Facebook with ease!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nayandas69/Social-Media-Downloader",
    project_urls={
        "Source Code": "https://github.com/nayandas69/Social-Media-Downloader",
        "Bug Tracker": "https://github.com/nayandas69/Social-Media-Downloader/issues",
        "Documentation": "https://github.com/nayandas69/Social-Media-Downloader#readme",
        "Discord Community": "https://discord.gg/skHyssu",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Internet",
        "Topic :: Multimedia :: Video",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    keywords=[
        "yt-dlp",
        "cli tool",
        "video downloader",
        "tiktok downloader",
        "youtube downloader",
        "facebook downloader",
        "instagram downloader",
        "social media downloader",
    ],
    packages=find_packages(exclude=["tests*", "docs*"]),
    py_modules=["downloader"],
    python_requires=">=3.6",
    install_requires=[
        "yt-dlp>=2023.7.6",  # YouTube, TikTok, Facebook downloader
        "instaloader>=4.10.0",  # Instagram downloader
        "tqdm>=4.65.0",  # Progress bar
        "requests>=2.31.0",  # HTTP requests
        "ffmpeg-python>=0.2.0",  # FFmpeg wrapper
        "certifi>=2023.7.22",  # SSL certificates
        "setuptools>=65.5.0",  # Packaging utility
        "wheel>=0.38.4",  # Ensures proper installation
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",  # Testing framework
            "flake8>=6.0",  # Linter for code style
            "black>=23.1",  # Code formatter
        ],
    },
    entry_points={
        "console_scripts": [
            "social-media-downloader=downloader:main",  # CLI command
        ],
    },
    include_package_data=True,
    zip_safe=False,  # Allow installing as an unzipped package
    license="MIT",  # Open-source license
)
