"""Module with tests for task 87."""

import unittest
from tasks.task_87 import task_87


class TestTask87(unittest.TestCase):
    """Tests for function task_87."""

    def test_arg_is_zero(self):
        """Test that number is zero a AssertionError exception is called."""
        with self.assertRaises(AssertionError):
            task_87(0, 1)
            task_87(1, 0)

    def test_tail_size_one(self):
        """Test that tail size equal 1 returns last digit."""
        self.assertEqual(task_87(112, 1), 2)

    def test_valid(self):
        """Test that task_87 function returns correct result."""
        self.assertEqual(task_87(112, 2), 3)

    def test_one_of_args_has_incorrect_type(self):
        """Test when one of args is incorrect data type a TypeError exception is called."""
        with self.assertRaises(AssertionError):
            task_87("5", 10)
            task_87(5, "10")
