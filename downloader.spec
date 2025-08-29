# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files
import os

# Collect data files from pyfiglet or any other dependency
datas = collect_data_files("pyfiglet")

# Path to your smd/ package
project_path = os.path.abspath(".")

a = Analysis(
    ['smd/__main__.py'],  # Correct entry point
    pathex=[project_path],
    binaries=[],
    datas=datas,
    hiddenimports=[
        "yt_dlp",
        "termcolor",
        "tqdm",
        "instaloader",
        "pyfiglet",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=1,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
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
    icon='assets/logo.ico',
    disable_windowed_traceback=False,
)
