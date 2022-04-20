"""
87. Даны натуральное n, m. Получить сумму m последних цифр
числа n.
"""
import unittest


# cut & sum the digit from tail of target number a given number of times
def get_sum_of_lasts_few(target: int, tail_size: int) -> int:
    if tail_size > len(str(target)):
        raise ValueError("Number tail size > number!")
    if target == 0:
        raise ValueError("Zero is not natural number!")
    if tail_size == 1:
        return target % 10
    else:
        tail_size -= 1
        return target % 10 + get_sum_of_lasts_few(target // 10, tail_size)


class TestSumOfLastsFew(unittest.TestCase):

    def test_target_arg_zero(self):
        with self.assertRaises(ValueError):
            get_sum_of_lasts_few(0, 1)

    def test_tail_size(self):
        with self.assertRaises(ValueError):
            get_sum_of_lasts_few(1, 5)

    def test_tail_size_one(self):
        self.assertEqual(get_sum_of_lasts_few(112, 1), 2)

    def test_get_sum_of_lasts_few(self):
        self.assertEqual(get_sum_of_lasts_few(112, 2), 3)


"""
to run from console try: python3 task_87.py n m
where n is natural number, 
m - number of digits to count the sum (from the end)
"""
if __name__ == "__main__":
    print(get_sum_of_lasts_few(66888, 5))
    unittest.main(verbosity=2)
