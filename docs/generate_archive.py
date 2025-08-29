import os
import requests
from datetime import datetime

# Configuration
OWNER = "nayandas69"
REPO = "Social-Media-Downloader"
ARCHIVE_PATH = os.path.join("docs", "archive.md")


def fetch_releases():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/releases"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def generate_markdown_table(releases):
    header = (
        "| Release Date | Version | Windows EXE | Linux Binary | Debian Package |\n"
    )
    separator = (
        "|--------------|---------|-------------|--------------|----------------|\n"
    )
    rows = []

    for idx, release in enumerate(releases):
        date = release["published_at"][:10]
        version = release["tag_name"]

        # Add Recommended badge to latest release
        if idx == 0:
            version += " <br>🟢 **Recommended**"

        assets = {
            asset["name"]: asset["browser_download_url"] for asset in release["assets"]
        }

        exe_link = next(
            (
                f"[Download]({url})"
                for name, url in assets.items()
                if name.endswith(".exe")
            ),
            "No EXE available",
        )
        tar_link = next(
            (
                f"[Download]({url})"
                for name, url in assets.items()
                if name.endswith(".tar.gz")
            ),
            "No binary available",
        )
        deb_link = next(
            (
                f"[Download]({url})"
                for name, url in assets.items()
                if name.endswith(".deb")
            ),
            "No .deb package available",
        )

        row = f"| {date} | {version} | {exe_link} | {tar_link} | {deb_link} |"
        rows.append(row)

    return header + separator + "\n".join(rows)


from datetime import datetime


def main():
    releases = fetch_releases()
    markdown_table = generate_markdown_table(releases)

    content = (
        "---\n"
        "title: 📦 Release Archive\n"
        "---\n\n"
        "!!! note\n"
        "    This page lists all official releases of the Social Media Downloader project.  \n"
        f"    For the latest release, visit the [Releases](https://github.com/{OWNER}/{REPO}/releases) page.\n\n"
        f"{markdown_table}\n\n"
        "!!! danger\n"
        "    Versions **v1.0.0 through v1.0.7** do not include Build Artifacts EXE, Linux binary, or `.deb` packages.  \n"
        "    Only source code is available for these releases. If you need to use them, you'll have to **build manually** from source.  \n"
        "    We always recommend using the **latest release** to get the best features and compatibility.\n\n"
        f"---\n"
        f"**Last Updated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC\n"
    )

    with open(ARCHIVE_PATH, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    main()
