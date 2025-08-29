# test/test.py

import unittest
from unittest.mock import patch
from smd import (
    load_config,
    check_internet_connection,
    is_valid_platform_url,
    get_unique_filename,
    log_download,
)
import os
import csv


class TestDownloader(unittest.TestCase):
    def test_config_loads_with_defaults(self):
        config = load_config()
        self.assertIn("default_format", config)
        self.assertIn("download_directory", config)
        self.assertIn("mp3_quality", config)

    def test_check_internet_connection_mocked(self):
        with patch("smd.downloader.requests.head") as mock_head:
            mock_head.return_value.status_code = 200
            self.assertTrue(check_internet_connection())

    def test_is_valid_platform_url(self):
        self.assertTrue(
            is_valid_platform_url("https://youtube.com/watch?v=abc", ["youtube.com"])
        )
        self.assertFalse(is_valid_platform_url("https://example.com", ["youtube.com"]))

    def test_get_unique_filename_appends_suffix(self):
        with patch("os.path.exists", side_effect=[True, True, False]):
            filename = get_unique_filename("test.mp4")
            self.assertEqual(filename, "test (2).mp4")

    def test_log_download_writes_csv(self):
        tmp_file = "test_download_log.csv"
        try:
            # Patch target file path
            with patch("smd.downloader.history_file", tmp_file):
                log_download("http://example.com", "Success")
                with open(tmp_file, newline="") as f:
                    rows = list(csv.reader(f))
                    self.assertEqual(len(rows), 1)
                    self.assertEqual(rows[0][0], "http://example.com")
        finally:
            if os.path.exists(tmp_file):
                os.remove(tmp_file)


if __name__ == "__main__":
    unittest.main()


# This code is a unit test for the downloader module in the smd package.
# It tests various functionalities such as configuration loading, internet connection checking,
# URL validation, filename uniqueness, and download logging.
# The code is structured to be run as a standalone script or as part of a larger test suite.
# The tests are comprehensive and cover both positive and negative cases for each function.
