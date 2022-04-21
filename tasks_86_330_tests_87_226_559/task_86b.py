"""This module provides function to get digits sum in the number."""


# task 86b
def sum_digits(number: int) -> int:
    """
    Get digits sum in the number
    :param number: int
    :return: int
    """
    return sum([int(num) for num in str(number)])


if __name__ == "__main__":
    NUMBER = 13456
    print(sum_digits(NUMBER))
