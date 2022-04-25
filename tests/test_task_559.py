""" Group tests for tasks. """
import unittest
from tasks_for_tests.task_559 import task_559, sieve_of_eratosthenes


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
