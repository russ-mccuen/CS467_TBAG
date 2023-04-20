import unittest
import json
from main import load_game


class TestLoadGame(unittest.TestCase):

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_game("nonexistent_file.JSON")


if __name__ == '__main__':
    unittest.main()
