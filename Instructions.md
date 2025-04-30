# Instructions for Building & Running Social Media Downloader

Welcome to the **Social Media Downloader** project!  
Follow the steps below to build, run, and distribute the tool across different platforms.

## Clone the Repository

First, clone this repo to your system:

```bash
git clone https://github.com/nayandas69/Social-Media-Downloader.git
cd Social-Media-Downloader
```

## Install Requirements

Make sure you have Python installed (preferably Python 3.8+).  
We recommend using a virtual environment.

### Create and Activate a Virtual Environment (Recommended)

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python downloader.py
```

#### On Linux:

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 downloader.py
```

## Build an Executable (EXE or Binary)

You can generate standalone executables using **PyInstaller**.

First, install it if you haven't:

```bash
pip install pyinstaller
```

### Windows EXE (Console Mode):

```bash
pyinstaller --onefile downloader.py
```

### Windows EXE (Silent/No Console):

```bash
pyinstaller --onefile --noconsole downloader.py
```

### Build with Custom Icon (Recommended):

```bash
python -m PyInstaller --onefile --icon=assets/logo.ico downloader.py
```

The output EXE will be available inside the `dist/` folder.

---

## Build Linux Binary

You can build a binary for Linux in the same way:

```bash
pyinstaller --onefile downloader.py
```

Or with custom icon (optional, if supported):

```bash
python3 -m PyInstaller --onefile --icon=assets/logo.ico downloader.py
```

Once built, move into the `dist/` folder and run:

```bash
chmod +x downloader
./downloader
```

### Handling PyFiglet Font Error
If you get an error like:
```
ModuleNotFoundError: No module named 'pyfiglet.fonts'
```
You need to manually include font data.

Run this step **once**:
```bash
pyi-makespec --onefile --icon=assets/logo.ico downloader.py
```
Then open the generated `downloader.spec` and replace its content with:

```python
# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files("pyfiglet")

a = Analysis(
    ['downloader.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='downloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/logo.ico',
)
```

This will ensure that the fonts are included in the build.

Then build it:
```bash
pyinstaller downloader.spec
```

The working `.exe` will be in the `dist/` folder.


## Notes

> [!IMPORTANT]
> - Make sure **FFmpeg** is installed and accessible in your system PATH. The tool will automatically check this.
> - The downloader **only works with public links** (YouTube, TikTok, etc.), not private content.

> [!TIP]
> It is **not recommended** to redistribute modified binaries or EXEs outside this repository unless you're contributing through official channels.

## Tested Platforms

- [x] Windows 11 / 10 ✅
- [x] Kali Linux ✅
- [x] Parrot OS ✅
- [ ] macOS ❌ (Not tested)
- [ ] Other Linux Distros ✅ (Should work but not tested)


## Recommended Setup

While prebuilt binaries (EXE, Linux) are available, **we recommend** cloning the repo and building the tool yourself for the best compatibility and security.


## Why Build from Source?

- **Security**: Ensure the code is safe and free from malware.
- **Customization**: Modify the code to suit your needs.
- **Latest Features**: Get the latest updates and features directly from the source.
- **User Feedback**: We value your input to improve the tool.


## Stay Updated

For updates, improvements, and support:
- Visit the official repo: [GitHub - Social Media Downloader](https://github.com/nayandas69/Social-Media-Downloader)
- Join the [Discord Community](https://discord.gg/skHyssu)


## See Tutorials
[![Watch the demo](https://img.youtube.com/vi/a_O1oQwZPlk/0.jpg)](https://www.youtube.com/watch?v=a_O1oQwZPlk)


## See Also
> [!NOTE]
> This Web Portal is maintained by the original author.
> You can download the tool from the web portal as well.
> - [Social Media Downloader - Web Portal](https://nayandas69.github.io/Social-Media-Downloader)
