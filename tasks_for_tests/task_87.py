"""This module consists of task_87."""


# cut & sum the digit from tail of target number a given number of times
def task_87(target: int, tail_size: int) -> int:
    """
    Get last digits sum in the target
    :param target: int
    :param tail_size: int
    :return: int
    """
    if target == 0:
        raise ValueError("Zero is not natural number!")
    if tail_size == 1:
        return target % 10
    tail_size -= 1
    return target % 10 + task_87(target // 10, tail_size)
