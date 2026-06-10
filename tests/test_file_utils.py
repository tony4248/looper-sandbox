import os
import tempfile
import unittest

from utils.file_utils import file_exists, read_lines, write_lines


class TestWriteAndReadLines(unittest.TestCase):
    def test_round_trip(self):
        lines = ["alpha", "beta", "gamma"]
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "data.txt")
            write_lines(path, lines)
            self.assertEqual(read_lines(path), lines)

    def test_read_strips_lines(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "data.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write("  alpha  \n\tbeta\t\n")
            self.assertEqual(read_lines(path), ["alpha", "beta"])

    def test_write_empty_list(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "empty.txt")
            write_lines(path, [])
            self.assertEqual(read_lines(path), [])


class TestFileExists(unittest.TestCase):
    def test_true_for_existing_file(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "data.txt")
            write_lines(path, ["x"])
            self.assertTrue(file_exists(path))

    def test_false_for_missing_path(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertFalse(file_exists(os.path.join(d, "nope.txt")))

    def test_false_for_directory(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertFalse(file_exists(d))


if __name__ == "__main__":
    unittest.main()
