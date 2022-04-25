""" Group tests for tasks. """
import unittest
from tasks_for_tests.task_87 import task_87


class TestTask87(unittest.TestCase):
    """ Tests for function task_87. """

    def test_target_arg_zero(self):
        """
        Test that number is zero a ValueError exception is called.
        """
        with self.assertRaises(ValueError):
            task_87(0, 1)

    def test_tail_size_one(self):
        """
        Test that tail size equal 1 returns last digit.
        """
        self.assertEqual(task_87(112, 1), 2)

    def test_task_87(self):
        """
        Test that task_87 function returns correct result.
        """
        self.assertEqual(task_87(112, 2), 3)

    def test_one_of_args_has_incorrect_type(self):
        """ Test when one of args is incorrect data type a TypeError exception is called. """
        self.assertRaises(TypeError, task_87, "5", 10)
        self.assertRaises(TypeError, task_87, 5, "10")
