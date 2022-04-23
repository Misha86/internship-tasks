"""This module provides function to get digits length in the number."""


def task_86a(number: int) -> int:
    """ Get digits length in the number. """
    if not isinstance(number, int):
        raise TypeError("Argument should be integer!")
    return len(str(number))


if __name__ == "__main__":
    NUMBER = 13456
    print(task_86a(NUMBER))
