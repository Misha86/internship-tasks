"""
226. Даны натуральные числа m, n. Получить все их
натуральные общие кратные, меньшие mn.
"""
import unittest


# return all natural common multiples less than first_arg * second_arg
def get_natural_common_multiples(first_arg: int, second_arg: int) -> list[int]:
    """
    Get natural common multiples
    :param first_arg: int
    :param second_arg: int
    :return: list[int]
    """
    limit = first_arg * second_arg
    suspect = second_arg
    result = []
    while suspect < limit:
        if suspect % first_arg == 0:
            result.append(suspect)
        suspect += second_arg

    return result


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


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print(get_natural_common_multiples(1, 10))
