"""330.

A natural number is call to be perfect if it is equal
to the sum of all its divisors except itself
The number 6 is perfect, since 6 = 1 + 2 + 3.
The number 8 is not perfect, since 8 ≠ 1 + 2 + 4.
A natural number n is given. Get all perfect numbers less than n.
"""

from time import time
from tasks.utils import is_natural_number


def check_simple_number(number: int) -> bool:
    """Check that number is simple."""
    assert is_natural_number(number), "The number should be natural"
    counter = 0
    for i in range(1, int(number / 2) + 1):
        if counter > 2:
            break
        if number % i == 0:
            counter += 1
    return counter == 1


def task_330(number: int) -> list[int]:
    """Get perfect numbers in range(1, number)."""
    assert is_natural_number(number), "The number should be natural"
    if number <= 6:
        return []

    result = [6, ]

    for index in range(3, 100, 2):
        expect_simple_num = pow(2, index) - 1
        is_simple = check_simple_number(expect_simple_num)
        if is_simple:
            value = pow(2, index - 1) * (pow(2, index) - 1)
            if value >= number:
                break
            result.append(value)
    return result


if __name__ == "__main__":
    NUMBER = 100000000000
    start = time()
    print(task_330(NUMBER))
    print(time() - start)
