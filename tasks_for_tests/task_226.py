"""This module consists of task_226."""


# return all natural common multiples less than first_arg * second_arg
def task_226(first_arg: int, second_arg: int) -> list[int]:
    """
    Get natural common multiples.
    """
    limit = first_arg * second_arg
    suspect = second_arg
    result = []
    while suspect < limit:
        if suspect % first_arg == 0:
            result.append(suspect)
        suspect += second_arg

    return result
