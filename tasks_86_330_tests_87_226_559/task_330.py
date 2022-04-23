"""This module provides function to get perfect numbers."""
import time


def check_simple_number(number: int) -> bool:
    """ Check that number is simple. """
    counter = 0
    for i in range(1, int(number / 2) + 1):
        if counter > 2:
            break
        if number % i == 0:
            counter += 1
    return True if counter == 1 else False


def task_330(number: int) -> list[int]:
    """ Get perfect numbers in range(1, number). """
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
    start = time.time()
    print(task_330(NUMBER))
    print(time.time() - start)
