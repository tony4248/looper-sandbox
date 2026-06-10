import unittest

from utils.date_utils import days_between, is_weekend, today_str


class TestTodayStr(unittest.TestCase):
    def test_matches_iso_shape(self):
        self.assertRegex(today_str(), r"^\d{4}-\d{2}-\d{2}$")


class TestDaysBetween(unittest.TestCase):
    def test_same_date_is_zero(self):
        self.assertEqual(days_between("2026-06-10", "2026-06-10"), 0)

    def test_positive_diff(self):
        self.assertEqual(days_between("2026-06-01", "2026-06-10"), 9)

    def test_symmetry(self):
        self.assertEqual(
            days_between("2026-06-01", "2026-06-10"),
            days_between("2026-06-10", "2026-06-01"),
        )

    def test_across_year(self):
        self.assertEqual(days_between("2025-12-31", "2026-01-01"), 1)


class TestIsWeekend(unittest.TestCase):
    def test_saturday(self):
        self.assertTrue(is_weekend("2026-06-13"))

    def test_sunday(self):
        self.assertTrue(is_weekend("2026-06-14"))

    def test_weekday(self):
        self.assertFalse(is_weekend("2026-06-10"))


if __name__ == "__main__":
    unittest.main()
