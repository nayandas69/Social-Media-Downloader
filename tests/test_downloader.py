"""
Unit tests for the Social Media Downloader package.

This module contains comprehensive tests for the core functionality of the SMD package,
including configuration management, network utilities, URL validation, and file operations.
"""

import unittest
import os
import csv
import tempfile
import json
from unittest.mock import patch, mock_open, MagicMock
from typing import Any, Dict

from smd import (
    load_config,
    check_internet_connection,
    is_valid_platform_url,
    get_unique_filename,
    log_download,
)


class TestDownloader(unittest.TestCase):
    """Test cases for the downloader module functionality."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.test_config = {
            "default_format": "720p",
            "download_directory": "test_media",
            "history_file": "test_history.csv",
            "mp3_quality": "192",
        }

    def test_config_loads_with_defaults(self) -> None:
        """Test that configuration loads with all required default values."""
        config = load_config()

        # Check that all required keys are present
        required_keys = [
            "default_format",
            "download_directory",
            "mp3_quality",
            "history_file",
        ]
        for key in required_keys:
            self.assertIn(key, config, f"Missing required config key: {key}")

        # Check that values are of expected types
        self.assertIsInstance(config["default_format"], str)
        self.assertIsInstance(config["download_directory"], str)
        self.assertIsInstance(config["mp3_quality"], str)
        self.assertIsInstance(config["history_file"], str)

    @patch("smd.downloader.requests.head")
    def test_check_internet_connection_success(self, mock_head: MagicMock) -> None:
        """Test successful internet connection check."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_head.return_value = mock_response

        result = check_internet_connection()
        self.assertTrue(result)
        mock_head.assert_called_once()

    @patch("smd.downloader.requests.head")
    def test_check_internet_connection_failure(self, mock_head: MagicMock) -> None:
        """Test internet connection check failure."""
        mock_head.side_effect = Exception("Connection error")

        result = check_internet_connection()
        self.assertFalse(result)

    def test_is_valid_platform_url_valid(self) -> None:
        """Test URL validation with valid platform URLs."""
        test_cases = [
            ("https://youtube.com/watch?v=abc123", ["youtube.com"]),
            ("https://www.tiktok.com/@user/video/123", ["tiktok.com"]),
            ("https://instagram.com/p/abc123/", ["instagram.com"]),
        ]

        for url, domains in test_cases:
            with self.subTest(url=url):
                self.assertTrue(is_valid_platform_url(url, domains))

    def test_is_valid_platform_url_invalid(self) -> None:
        """Test URL validation with invalid platform URLs."""
        test_cases = [
            ("https://example.com/video", ["youtube.com"]),
            ("https://malicious-site.com", ["tiktok.com"]),
            ("", ["instagram.com"]),
        ]

        for url, domains in test_cases:
            with self.subTest(url=url):
                self.assertFalse(is_valid_platform_url(url, domains))

    @patch("os.path.exists")
    def test_get_unique_filename_no_conflict(self, mock_exists: MagicMock) -> None:
        """Test unique filename generation when no conflict exists."""
        mock_exists.return_value = False

        filename = get_unique_filename("test.mp4")
        self.assertEqual(filename, "test.mp4")

    @patch("os.path.exists")
    def test_get_unique_filename_with_conflict(self, mock_exists: MagicMock) -> None:
        """Test unique filename generation when conflicts exist."""
        # Simulate file exists for original and first increment, but not second
        mock_exists.side_effect = [True, True, False]

        filename = get_unique_filename("test.mp4")
        self.assertEqual(filename, "test (2).mp4")

    def test_log_download_creates_csv_entry(self) -> None:
        """Test that download logging creates proper CSV entries."""
        with tempfile.NamedTemporaryFile(
            mode="w+", delete=False, suffix=".csv"
        ) as tmp_file:
            tmp_filename = tmp_file.name

        try:
            # Patch the history_file to use our temporary file
            with patch("smd.downloader.history_file", tmp_filename):
                log_download("https://example.com/video", "Success")

                # Verify the CSV entry was created
                with open(tmp_filename, "r", newline="", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    rows = list(reader)

                    self.assertEqual(len(rows), 1)
                    self.assertEqual(rows[0][0], "https://example.com/video")
                    self.assertEqual(rows[0][1], "Success")
                    # Third column should be timestamp - just check it exists
                    self.assertTrue(len(rows[0][2]) > 0)
        finally:
            # Clean up temporary file
            if os.path.exists(tmp_filename):
                os.unlink(tmp_filename)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_config_file_creation(
        self, mock_exists: MagicMock, mock_file: MagicMock
    ) -> None:
        """Test that config file is created when it doesn't exist."""
        mock_exists.return_value = False

        # Mock json.dump to avoid actual file operations
        with patch("json.dump") as mock_json_dump:
            config = load_config()

            # Verify file was opened for writing
            mock_file.assert_called()
            mock_json_dump.assert_called_once()

            # Should return default config
            self.assertIn("default_format", config)

    def test_url_validation_edge_cases(self) -> None:
        """Test URL validation with edge cases."""
        edge_cases = [
            ("", []),  # Empty URL and domains
            ("https://youtube.com", []),  # Empty domains list
            ("", ["youtube.com"]),  # Empty URL
            ("not-a-url", ["youtube.com"]),  # Invalid URL format
        ]

        for url, domains in edge_cases:
            with self.subTest(url=url, domains=domains):
                result = is_valid_platform_url(url, domains)
                self.assertIsInstance(result, bool)


class TestConfigValidation(unittest.TestCase):
    """Test cases for configuration validation functionality."""

    def test_invalid_mp3_quality_correction(self) -> None:
        """Test that invalid MP3 quality values are corrected."""
        invalid_config = {
            "default_format": "720p",
            "download_directory": "media",
            "history_file": "history.csv",
            "mp3_quality": "999",  # Invalid quality
        }

        with patch("os.path.exists", return_value=True):
            with patch(
                "builtins.open", mock_open(read_data=json.dumps(invalid_config))
            ):
                with patch("json.dump"):  # Mock the save operation
                    config = load_config()

                    # Should be corrected to default
                    self.assertEqual(config["mp3_quality"], "192")

    def test_invalid_default_format_correction(self) -> None:
        """Test that invalid default format values are corrected."""
        invalid_config = {
            "default_format": "invalid_format",
            "download_directory": "media",
            "history_file": "history.csv",
            "mp3_quality": "192",
        }

        with patch("os.path.exists", return_value=True):
            with patch(
                "builtins.open", mock_open(read_data=json.dumps(invalid_config))
            ):
                with patch("json.dump"):  # Mock the save operation
                    config = load_config()

                    # Should be corrected to default
                    self.assertEqual(config["default_format"], "show_all")


if __name__ == "__main__":
    unittest.main(verbosity=2)
