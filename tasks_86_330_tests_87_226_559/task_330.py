"""This module provides function to get perfect numbers."""
import time


def perfect_numbers(number: int) -> list[int]:
    """
    Get perfect numbers in range(1, number)

    :param number: int
    :return: list[int]
    """

    numbers = []
    for num in range(1, number):
        dividers = [div for div in range(1, int(num/2)+1) if num % div == 0]
        if sum(dividers) == num:
            numbers.append(num)
    return numbers


if __name__ == "__main__":
    NUMBER = 100000
    start = time.time()
    print(perfect_numbers(NUMBER))
    print(time.time() - start)
