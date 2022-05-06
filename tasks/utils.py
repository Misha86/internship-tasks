"""This module with help functions."""


def is_natural_number(number: int) -> bool:
    """Returns True if the number is natural."""
    return isinstance(number, int) and number > 0

def has_int_in_list(array: list[int]) -> bool:
    """Returns True if the list has integer elements."""
    tmp: bool
    for i in array:
        if not isinstance(i, int):
            return False
        tmp = True

    return tmp
  