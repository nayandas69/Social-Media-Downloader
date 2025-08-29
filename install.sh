#!/bin/bash

# ====================================================
# SMD Installer - Social Media Downloader
# Author: nayandas69
# Repo: https://github.com/nayandas69/Social-Media-Downloader
# License: MIT
# ====================================================

# GitHub repository path
REPO="nayandas69/Social-Media-Downloader"

# Debian package name (must match .deb package)
PACKAGE_NAME="social-media-downloader"

# ---------------------------------------------
# Function: Display the installer header
# ---------------------------------------------
function show_header() {
    clear
    echo -e "\e[96m===========================================\e[0m"
    echo -e "\e[1;95m         SMD Installer - v1.0             \e[0m"
    echo -e "\e[96m===========================================\e[0m"
    echo -e "\e[93mAuthor:\e[0m nayandas69"
    echo -e "\e[93mRepo  :\e[0m https://github.com/$REPO"
    echo ""
}

# ---------------------------------------------
# Function: Ensure FFmpeg is installed
# ---------------------------------------------
function ensure_ffmpeg() {
    if ! command -v ffmpeg &>/dev/null; then
        echo -e "\nFFmpeg is not installed. Installing..."
        sudo apt update && sudo apt install -y ffmpeg
    else
        echo -e "\nFFmpeg is already installed."
    fi
}

# ---------------------------------------------
# Function: Get the latest .deb file URL
# ---------------------------------------------
function get_latest_deb_url() {
    curl -s "https://api.github.com/repos/$REPO/releases/latest" |
        grep "browser_download_url" |
        grep ".deb" |
        cut -d '"' -f 4
}

# ---------------------------------------------
# Function: Get the latest version number
# ---------------------------------------------
function get_latest_version() {
    curl -s "https://api.github.com/repos/$REPO/releases/latest" |
        grep '"tag_name":' |
        sed -E 's/.*"([^"]+)".*/\1/'
}

# ---------------------------------------------
# Function: Perform install/update using .deb
# ---------------------------------------------
function perform_install() {
    # Fetch latest URL and version
    DEB_URL=$(get_latest_deb_url)
    LATEST_VERSION=$(get_latest_version)

    # Safety check
    if [ -z "$DEB_URL" ] || [ -z "$LATEST_VERSION" ]; then
        echo -e "\nError: Unable to fetch release info from GitHub."
        return
    fi

    echo -e "\nLatest version available: $LATEST_VERSION"
    read -p $'\nProceed with installation? (y/n): ' CONFIRM

    if [[ "$CONFIRM" == [yY] ]]; then
        TEMP_DEB="/tmp/${DEB_URL##*/}"  # Extract filename from URL
        echo -e "\nDownloading package..."
        wget -q --show-progress -O "$TEMP_DEB" "$DEB_URL"

        echo -e "\nInstalling package..."
        sudo dpkg -i "$TEMP_DEB"
        sudo apt-get install -f -y  # Fix missing dependencies

        rm -f "$TEMP_DEB"
        echo -e "\nInstallation complete."
    else
        echo -e "\nInstallation cancelled by user."
    fi
}

# ---------------------------------------------
# Function: Option 1 - Smart Install
# ---------------------------------------------
function smart_install() {
    # Ensure ffmpeg is installed
    ensure_ffmpeg

    # Check if package is already installed
    CURRENT_VERSION=$(dpkg -s "$PACKAGE_NAME" 2>/dev/null | grep '^Version:' | awk '{print $2}')

    if [ -n "$CURRENT_VERSION" ]; then
        echo -e "\nSMD is already installed (version $CURRENT_VERSION)."
        echo -e "Redirecting to update..."
        sleep 2
        update_smd
    else
        echo -e "\nSMD is not installed. Proceeding with fresh installation..."
        perform_install
    fi
}

# ---------------------------------------------
# Function: Option 2 - Update SMD
# ---------------------------------------------
function update_smd() {
    CURRENT_VERSION=$(dpkg -s "$PACKAGE_NAME" 2>/dev/null | grep '^Version:' | awk '{print $2}')
    LATEST_VERSION=$(get_latest_version)

    # If not installed
    if [ -z "$CURRENT_VERSION" ]; then
        echo -e "\nSMD is not installed. Use option 1 to install it first."
        return
    fi

    echo -e "\nCurrent version : $CURRENT_VERSION"
    echo -e "Latest version  : $LATEST_VERSION"

    if [[ "$CURRENT_VERSION" != "$LATEST_VERSION" ]]; then
        echo -e "\nA newer version is available. Updating..."
        perform_install
    else
        echo -e "\nYou already have the latest version."
    fi
}

# ---------------------------------------------
# Function: Option 3 - Uninstall SMD
# ---------------------------------------------
function uninstall_smd() {
    echo -e "\nUninstalling SMD..."
    sudo apt-get remove --purge -y "$PACKAGE_NAME"
    echo -e "\nUninstallation complete."
}

# ---------------------------------------------
# Main Menu Loop
# ---------------------------------------------
while true; do
    show_header
    echo "1. Install SMD"
    echo "2. Update SMD"
    echo "3. Uninstall SMD"
    echo "4. Exit"
    echo ""
    read -p "Enter your choice [1-4]: " CHOICE

    case $CHOICE in
        1) smart_install ;;
        2) update_smd ;;
        3) uninstall_smd ;;
        4) echo -e "\nExiting SMD Installer. Goodbye!"; exit 0 ;;
        *) echo -e "\nInvalid option. Please enter 1 to 4."; sleep 1 ;;
    esac

    read -p $'\nPress Enter to return to the menu...'
done
# ---------------------------------------------
# End of script
# ---------------------------------------------
# Note: This script is designed to be run on Debian-based systems.
# Ensure you have the necessary permissions to install packages.