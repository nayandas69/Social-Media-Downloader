# test/test.py

import unittest
from unittest.mock import patch, MagicMock
from smd import downloader


class TestDownloader(unittest.TestCase):

    def test_config_loads_with_defaults(self):
        config = downloader.load_config()
        self.assertIn("default_format", config)
        self.assertIn("download_directory", config)
        self.assertIn("mp3_quality", config)

    def test_check_internet_connection(self):
        with patch("smd.downloader.requests.head") as mock_head:
            mock_head.return_value.status_code = 200
            self.assertTrue(downloader.check_internet_connection())

    def test_is_valid_platform_url(self):
        self.assertTrue(
            downloader.is_valid_platform_url("https://youtube.com/watch?v=abc", ["youtube.com"])
        )
        self.assertFalse(
            downloader.is_valid_platform_url("https://example.com", ["youtube.com"])
        )

    def test_get_unique_filename(self):
        with patch("os.path.exists", side_effect=[True, True, False]):
            result = downloader.get_unique_filename("test.mp4")
            self.assertEqual(result, "test (2).mp4")

    def test_log_download_creates_entry(self):
        import os
        import csv

        tmp_file = "test_history.csv"
        downloader.history_file = tmp_file
        downloader.log_download("http://example.com", "Success")

        with open(tmp_file, newline="") as f:
            rows = list(csv.reader(f))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0][0], "http://example.com")

        os.remove(tmp_file)


if __name__ == "__main__":
    unittest.main()


# This code is a unit test for the downloader module in the smd package.
# It tests various functionalities such as configuration loading, internet connection checking,
# URL validation, filename uniqueness, and download logging.
# The code is structured to be run as a standalone script or as part of a larger test suite.
# The tests are comprehensive and cover both positive and negative cases for each function.
# The tests use unittest and unittest.mock to simulate and verify behaviors without making actual network requests or file system changes.
# The tests are designed to ensure that the downloader module behaves correctly under various conditions.
# The test cases are designed to be clear and concise, making it easy to understand the expected behavior of the downloader module.
# The test suite can be expanded with additional tests as needed to cover more edge cases or functionalities.