""" Test runner for tests from tasks/tests/ dir. """
import os
import unittest


# def suite():
#     """ Add all test from current file to TestSuite. """
#     loader = unittest.TestLoader()
#     tests = loader.loadTestsFromName('__main__')
#     suite_tests = unittest.TestSuite()
#     suite_tests.addTests(tests)
#     return suite_tests


def suite(tests_dir='tests', pattern='tests_task_*.py'):
    """ Add all test from tasks/tests/ dir to TestSuite. """
    this_dir = os.path.join(os.path.dirname(__file__), tests_dir)
    loader = unittest.TestLoader()
    suite_tests = unittest.TestSuite()
    package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
    suite_tests.addTests(package_tests)
    return suite_tests


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())