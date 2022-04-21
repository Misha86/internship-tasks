"""
87. Даны натуральное n, m. Получить сумму m последних цифр
числа n.
"""
import unittest


# cut & sum the digit from tail of target number a given number of times
def get_sum_of_lasts_few(target: int, tail_size: int) -> int:
    """
    Get last digits sum in the target
    :param target: int
    :param tail_size: int
    :return: int
    """
    if target == 0:
        raise ValueError("Zero is not natural number!")
    if tail_size == 1:
        return target % 10
    tail_size -= 1
    return target % 10 + get_sum_of_lasts_few(target // 10, tail_size)


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


if __name__ == "__main__":
    print(get_sum_of_lasts_few(66888, 5))
    print(get_sum_of_lasts_few(1, 5))
    unittest.main(verbosity=2)
