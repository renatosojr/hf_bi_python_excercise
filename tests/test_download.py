import unittest
from unittest.mock import patch
import os
from data_processing.download import download_json


class TestDownload(unittest.TestCase):
    @patch('data_processing.download.requests.get')
    def test_download_json_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'{"key": "value"}'

        test_filename = 'test_file.json'
        download_json('http://example.com', test_filename)

        self.assertTrue(os.path.exists(test_filename))
        with open(test_filename, 'rb') as f:
            content = f.read()
            self.assertEqual(content, b'{"key": "value"}')

        # Clean
        os.remove(test_filename)

    @patch('data_processing.download.requests.get')
    def test_download_json_failure(self, mock_get):
        mock_get.return_value.status_code = 404

        with self.assertRaises(Exception):
            download_json('http://example.com', 'test_file.json')


if __name__ == '__main__':
    unittest.main()
