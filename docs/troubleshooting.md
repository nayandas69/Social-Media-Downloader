---
title: 🛠️ Troubleshooting
---

Ran into a hiccup while building or running Social Media Downloader? No worries — here’s how to fix the most common issue related to **PyFiglet** fonts when using **PyInstaller**.

---

## Problem: Missing PyFiglet Fonts

If you see an error like this when you run the executable:

```bash
ModuleNotFoundError: No module named 'pyfiglet.fonts'
```

!!! note
    This happens because PyInstaller doesn't automatically bundle the font files that `pyfiglet` uses internally.

Without these fonts, your fancy ASCII banners won’t show up, and the script will crash on launch. Let’s fix that.

---

## Solution: Manually Include the Font Data

### Step 1: Generate a `.spec` File

Run this command to generate a basic `.spec` file for your project:

```bash
pyi-makespec --onefile --icon=assets/logo.ico smd/downloader.py
```

This will create a file called `downloader.spec`.

---

### Step 2: Edit the Spec File

Open `downloader.spec` in your code editor and replace its content with the following:

```python
# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files("pyfiglet")

a = Analysis(
    ['smd/downloader.py'],
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

What this does:

* It tells PyInstaller to explicitly include all the font data from `pyfiglet`, so your executable has everything it needs to render text art properly.

---

### Step 3: Rebuild Using the `.spec` File

Now that your spec file is set up, rebuild the project using:

```bash
pyinstaller downloader.spec
```

This will package the fonts correctly and produce a working binary inside the `dist/` folder.

---

###  Final Result

After building, check inside the `dist/` directory. You should now have a fully working standalone executable with no missing font errors — and your sweet ASCII art banners will look just the way they should.

---

!!! tip
    Want more help customizing your build? Head over to the [Build Instructions](./build.md) for extra tips on icons, silent mode, and cleanup options.

Got another error or issue? Feel free to [open an issue](https://github.com/nayandas69/Social-Media-Downloader/issues) on GitHub — we’re here to help.
