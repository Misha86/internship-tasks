""" Group tests for tasks. """
import unittest
from main import (task_559,
                  task_226,
                  task_87,
                  sieve_of_eratosthenes)


class TestTask87(unittest.TestCase):

    """ Tests for function task_87. """

    def test_target_arg_zero(self):
        """ Test that number is zero a ValueError exception is called. """
        with self.assertRaises(ValueError):
            task_87(0, 1)

    def test_tail_size_one(self):
        """ Test that tail size equal 1 returns last digit. """
        self.assertEqual(task_87(112, 1), 2)

    def test_task_87(self):
        """ Test that task_87 function returns correct result. """
        self.assertEqual(task_87(112, 2), 3)

    def test_one_of_args_has_incorrect_type(self):
        """ Test when one of args is incorrect data type a TypeError exception is called. """
        self.assertRaises(TypeError, task_87, "5", 10)
        self.assertRaises(TypeError, task_87, 5, "10")


class TestTask226(unittest.TestCase):

    """ Tests for function task_226. """

    def test_task_226_valid(self):
        """ Test that task_226 function returns correct result. """
        self.assertListEqual(task_226(5, 10), [10, 20, 30, 40])

    def test_one_of_args_is_zero(self):
        """Test when one of args is zero result is empty list."""
        self.assertListEqual(task_226(0, 10), [])
        self.assertListEqual(task_226(10, 0), [])

    def test_one_of_args_has_incorrect_type(self):
        """ Test when one of args is incorrect data type a TypeError exception is called. """
        self.assertRaises(TypeError, task_226, "5", 10)
        self.assertRaises(TypeError, task_226, 5, "10")


class TestTask559(unittest.TestCase):

    """ Tests for function task_559. """

    def test_sieve_of_eratosthenes(self):
        """ Test that sieve_of_eratosthenes function returns correct result. """
        self.assertListEqual(sieve_of_eratosthenes(10), [1, 2, 3, 5, 7])

    def test_task_559_valid(self):
        """ Test that task_559 function returns correct result. """
        self.assertListEqual(task_559(10), [1, 3, 7])

    def test_sieve_of_eratosthenes_arg_incorrect_type(self):
        """ Test that the arg has incorrect data type a TypeError exception is called. """
        self.assertRaises(TypeError, sieve_of_eratosthenes, "10")

    def test_task_559_incorrect_type(self):
        """ Test that the arg has incorrect data type a TypeError exception is called. """
        self.assertRaises(TypeError, task_559, "10")

    def test_sieve_of_eratosthenesone_arg_is_zero(self):
        """ Test when one of args is 0 result is empty list. """
        self.assertListEqual(sieve_of_eratosthenes(0), [])

    def test_task_559_arg_is_zero(self):
        """ Test when one of args is 0 result is empty list. """
        self.assertListEqual(task_559(0), [])

    def test_sieve_of_eratosthenesone_arg_is_one(self):
        """ Test when one of args is 1 result is [1, ]. """
        self.assertListEqual(sieve_of_eratosthenes(1), [1])

    def test_task_559_arg_is_one(self):
        """ Test when one of args is 1 result is empty list. """
        self.assertListEqual(task_559(1), [])


def suite():
    """ Add all test from current file to TestSuite. """
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromName('__main__')
    suite_tests = unittest.TestSuite()
    suite_tests.addTests(tests)
    return suite_tests


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
