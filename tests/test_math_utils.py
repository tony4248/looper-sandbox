import unittest

from utils.math_utils import factorial, fibonacci, is_prime


class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            factorial(-1)


class TestFibonacci(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_nth(self):
        self.assertEqual(fibonacci(10), 55)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)


class TestIsPrime(unittest.TestCase):
    def test_zero(self):
        self.assertFalse(is_prime(0))

    def test_one(self):
        self.assertFalse(is_prime(1))

    def test_two(self):
        self.assertTrue(is_prime(2))

    def test_prime(self):
        self.assertTrue(is_prime(13))

    def test_composite(self):
        self.assertFalse(is_prime(15))

    def test_negative(self):
        self.assertFalse(is_prime(-7))


if __name__ == "__main__":
    unittest.main()
