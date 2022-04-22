"""This module provides function to get digits length in the number."""


def count_digits(number: int) -> int:
    """
    Get digits length in the number
    :param number: int
    :return: int
    """
    if not isinstance(number, int):
        raise TypeError("Argument should be integer!")
    return len(str(number))


if __name__ == "__main__":
    NUMBER = 13456
    print(count_digits(NUMBER))
