""" Group tests for tasks. """
import unittest
from tasks_for_tests.task_226 import task_226


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
