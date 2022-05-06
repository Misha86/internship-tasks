"""Module with tests for task 559."""

import unittest
from tasks.task_559 import (task_559, sieve_of_eratosthenes)


class TestTask559(unittest.TestCase):
    """Tests for function task_559."""

    def test_sieve_of_eratosthenes(self):
        """Test that sieve_of_eratosthenes function returns correct result."""
        self.assertListEqual(sieve_of_eratosthenes(10), [1, 2, 3, 5, 7])

    def test_valid(self):
        """Test that task_559 function returns correct result."""
        self.assertListEqual(task_559(10), [1, 3, 7])

    def test_arg_incorrect_type(self):
        """Test that the arg has incorrect data type a AssertionError exception is called."""
        with self.assertRaises(AssertionError):
            sieve_of_eratosthenes("10")
            task_559("10")

    def test_sieve_of_eratosthenesone_arg_is_zero(self):
        """Test that number is zero a AssertionError exception is called."""
        with self.assertRaises(AssertionError):
            sieve_of_eratosthenes(0)

    def test_arg_is_zero(self):
        """Test that number is zero a AssertionError exception is called."""
        with self.assertRaises(AssertionError):
            task_559(0)


    def test_sieve_of_eratosthenesone_arg_is_one(self):
        """Test when one of args is 1 result is [1, ]."""
        self.assertListEqual(sieve_of_eratosthenes(1), [1])

    def test_is_one(self):
        """Test when one of args is 1 result is empty list."""
        self.assertListEqual(task_559(1), [])
