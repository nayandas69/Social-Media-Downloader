from setuptools import setup

# Read the README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="social-media-downloader",
    version="1.0.0",
    author="Nayan Das",
    author_email="nayanchandradas@hotmail.com",
    author_portfolio="https://socialportal.nayanchandradas.com",
    description="A versatile downloader for YouTube, TikTok, Instagram, and Facebook.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nayandas69/Social-Media-Downloader",
    project_urls={
        "Bug Tracker": "https://github.com/nayandas69/Social-Media-Downloader/issues",
        "Documentation": "https://github.com/nayandas69/Social-Media-Downloader#readme",
        "Source Code": "https://github.com/nayandas69/Social-Media-Downloader",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Multimedia :: Video",
        "Topic :: Internet",
    ],
    keywords=[
        "downloader", "social media downloader", "youtube", "tiktok", "instagram", "facebook",
        "video downloader", "cli downloader"
    ],
    packages=[""],  # Empty string for top-level scripts like `downloader.py`
    py_modules=["downloader"],  # Name of Python script
    python_requires=">=3.6",
    install_requires=[
        "yt-dlp>=2023.7.6",
        "instaloader>=4.10.0",
        "beautifulsoup4>=4.12.2",
        "tqdm>=4.65.0",
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "social-media-downloader=downloader:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    license="MIT",
)
