Project Structure Update
========================

This document outlines the recent changes made to the structure of the project repository.
The updates simplify organization and align the layout with modern Python packaging standards.

Overview
--------

The following changes were introduced:

- The `docs/` folder was removed.
- All user-facing files (including HTML pages) were moved to the root of the repository.
- `setup.py` was removed and replaced with `pyproject.toml`, in line with PEP 621.
- A new `MANIFEST.in` was added to control packaging content.
- Executable names and download links were updated for clarity and consistency.

Old Structure
-------------

::

    .
    ├── downloader.py
    ├── docs/
    │   └── index.html
    |   └── index.css
    |   └── index.js
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    └── setup.py

New Structure
-------------

::

    .
    ├── downloader.py
    ├── index.html
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    ├── pyproject.toml
    ├── MANIFEST.in
    ├── AUTHOR.rst
    └── .github/
        └── workflows/
            ├── page.yml
            └── release.yml
            └── python-package.yml
            └── update-contributors.yml

Important Notes
---------------

- HTML files have been moved directly to the root for easier access and maintenance.
- `pyproject.toml` now defines the project metadata, dependencies, and entry points.
- Users who previously relied on `Social.Media.Downloader.exe` will now receive `smd.exe`, and download links were updated accordingly.
- The script entry point includes both ``social-media-downloader`` and ``smd`` to preserve compatibility for previous users:

  .. code-block:: toml

      [project.scripts]
      social-media-downloader = "downloader:main"
      smd = "downloader:main"

- These changes aim to make the project easier to maintain, package, and distribute going forward.

Acknowledgments
---------------

Special thanks to [@mohinikhan123](https://github.com/mohinikhan123) for contributing to this structural improvement and streamlining the project layout.
