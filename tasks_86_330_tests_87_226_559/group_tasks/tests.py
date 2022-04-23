"""Group tests for tasks"""
import unittest
from main import (get_mersen_sequence_limited_by_natural_number,
                  get_natural_common_multiples,
                  get_sum_of_lasts_few,
                  sieve_of_eratosthenes)


class TestSumOfLastsFew(unittest.TestCase):

    """Tests for function get_sum_of_lasts_few."""

    def test_target_arg_zero(self):
        """Test that number is zero a ValueError exception is called."""
        with self.assertRaises(ValueError):
            get_sum_of_lasts_few(0, 1)

    def test_tail_size_one(self):
        """Test that tail size equal 1 returns last digit."""
        self.assertEqual(get_sum_of_lasts_few(112, 1), 2)

    def test_sum_of_lasts_few(self):
        """Test that get_sum_of_lasts_few function returns correct result."""
        self.assertEqual(get_sum_of_lasts_few(112, 2), 3)


class TestNaturalCommonMultiples(unittest.TestCase):
    """Tests for function get_sum_of_lasts_few."""

    def test_natural_common_multiples(self):
        """Test that get_natural_common_multiples function returns correct result."""
        self.assertListEqual(get_natural_common_multiples(5, 10), [10, 20, 30, 40])

    def test_one_of_args_is_zero(self):
        """Test when one of args is zero result is empty list."""
        self.assertListEqual(get_natural_common_multiples(0, 10), [])
        self.assertListEqual(get_natural_common_multiples(10, 0), [])

    def test_one_of_args_has_incorrect_type(self):
        """Test when one of args is incorrect data type a TypeError exception is called."""
        self.assertRaises(TypeError, get_natural_common_multiples, "5", 10)
        self.assertRaises(TypeError, get_natural_common_multiples, 5, "10")


class TestMersenSequenceLimited(unittest.TestCase):

    """Tests for function get_mersen_sequence_limited_by_natural_number."""

    def test_sieve_of_eratosthenes(self):
        """Test that sieve_of_eratosthenes function returns correct result."""
        self.assertListEqual(sieve_of_eratosthenes(10), [1, 2, 3, 5, 7])

    def test_mersen_sequence_limited_by_natural_number(self):
        """
        Test that get_mersen_sequence_limited_by_natural_number function returns correct result.
        """
        self.assertListEqual(get_mersen_sequence_limited_by_natural_number(10), [1, 3, 7])

    def test_sieve_of_eratosthenes_arg_has_incorrect_type(self):
        """Test that the arg has incorrect data type a TypeError exception is called."""
        self.assertRaises(TypeError, sieve_of_eratosthenes, "10")

    def test_get_mersen_sequence_limited_by_natural_number_arg_has_incorrect_type(self):
        """Test that the arg has incorrect data type a TypeError exception is called."""
        self.assertRaises(TypeError, get_mersen_sequence_limited_by_natural_number, "10")

    def test_sieve_of_eratosthenesone_arg_is_zero(self):
        """Test when one of args is 0 result is empty list."""
        self.assertListEqual(sieve_of_eratosthenes(0), [])

    def test_get_mersen_sequence_limited_by_natural_number_arg_is_zero(self):
        """Test when one of args is 0 result is empty list."""
        self.assertListEqual(get_mersen_sequence_limited_by_natural_number(0), [])

    def test_sieve_of_eratosthenesone_arg_is_one(self):
        """Test when one of args is 1 result is [1, ]."""
        self.assertListEqual(sieve_of_eratosthenes(1), [1])

    def test_get_mersen_sequence_limited_by_natural_number_arg_is_one(self):
        """Test when one of args is 1 result is empty list."""
        self.assertListEqual(get_mersen_sequence_limited_by_natural_number(1), [])


def suite():
    """Add all test to TestSuite"""
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromName('__main__')
    suite = unittest.TestSuite()
    suite.addTests(tests)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())


