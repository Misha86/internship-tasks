"""
226. Даны натуральные числа m, n. Получить все их
натуральные общие кратные, меньшие mn.
"""
import unittest


# return all natural common multiples less than first_arg * second_arg
def get_natural_common_multiples(first_arg: int, second_arg: int) -> list[int]:

    limit = first_arg * second_arg
    suspect = second_arg
    result = []
    while suspect < limit:
        if suspect % first_arg == 0:
            result.append(suspect)
        suspect += second_arg

    return result


class TestNaturalCommonMultiples(unittest.TestCase):

    def test_natural_common_multiples(self):
        self.assertListEqual(get_natural_common_multiples(5, 10), [10, 20, 30, 40])


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print(get_natural_common_multiples(50, 1000))
