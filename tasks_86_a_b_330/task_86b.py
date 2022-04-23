"""This module provides function to get digits sum in the number."""


# task 86b
def task_86b(number: int) -> int:
    """ Get digits sum in the number. """
    if not isinstance(number, int):
        raise TypeError("Argument should be integer!")
    return sum([int(num) for num in str(number)])


if __name__ == "__main__":
    NUMBER = 13456
    print(task_86b(NUMBER))
