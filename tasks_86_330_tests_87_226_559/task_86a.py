"""This module provides function to get digits length in the number."""


def count_digits(number: int) -> int:
    """
    Get digits length in the number
    :param number: int
    :return: int
    """
    return len(str(number))


if __name__ == "__main__":
    NUMBER = 13456
    print(count_digits(NUMBER))
