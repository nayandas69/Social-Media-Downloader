---
title: 🫗 Build Instructions
---

Want to turn Social Media Downloader into a standalone executable? Whether you're building for Windows or Linux, this guide will walk you through everything you need using **PyInstaller**.

---

## Install PyInstaller

First, make sure you have PyInstaller installed. It converts your Python scripts into standalone executables for easy distribution — no Python installation required on the end user’s system.

```bash
pip3 install pyinstaller
```

---

## Building on Windows

You’ve got a few options depending on how you want your executable to behave:

### Console Version

This version will open a terminal/console window when run.

```bash
pyinstaller --onefile smd/downloader.py
```

### Silent Version (No Console Window)

If you want to hide the terminal window (for example, when launching from a desktop shortcut or GUI), use:

```bash
pyinstaller --onefile --noconsole smd/downloader.py
```

### With a Custom Icon

Want a polished feel? Add your own `.ico` file to give the executable a custom icon:

```bash
pyinstaller --onefile --icon=assets/logo.ico smd/downloader.py
```
!!! important
    Make sure your icon file is in `.ico` format. If you’re using `.png`, you can convert it using an online tool or image editor.

After the build completes, your `.exe` file will be located in the `dist/` folder.

---

## Building on Linux

Building on Linux is just as straightforward. Run:

```bash
pyinstaller --onefile smd/downloader.py
```

Once the build finishes, make the output binary executable:

```bash
chmod +x dist/downloader
./dist/downloader
```

You now have a portable binary that can run on any compatible Linux system.

---

## Font Issues?

!!! tip
    If you're seeing missing fonts or broken ASCII art from `pyfiglet`, head over to the [Troubleshooting](./troubleshooting.md) page for help resolving that.

---

## Output

By default, PyInstaller creates two folders:

* `dist/` — contains your final executable
* `build/` — temporary build files (you can usually delete this after packaging)

Your single-file executable will always be located in the `dist/` directory.

---

## Clean Up (Optional)

Want to clean the extra files after a build?

```bash
rm -rf build __pycache__ *.spec
```

This will leave you with just your source code and the `dist/` folder containing your binary.

---

You're now ready to distribute your own standalone version of Social Media Downloader!

!!! tip
    Need `.deb` or other platform-specific packages? Stay tuned for packaging instructions in the future or check out our [Release Archive](./archive.md).
