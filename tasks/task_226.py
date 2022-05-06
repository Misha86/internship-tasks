"""226. Given natural numbers m, n. Get all natural common multiples, smaller m*n."""

from tasks.utils import is_natural_number


def task_226(first_arg: int, second_arg: int) -> list[int]:
    """Return all natural common multiples of first_arg & second_arg less than first_arg * second_arg."""
    assert is_natural_number(first_arg), "The number should be natural"
    assert is_natural_number(second_arg), "The number should be natural"
    limit = first_arg * second_arg
    suspect = second_arg
    result = []
    while suspect < limit:
        # Check whether the increment of the second number is divisible by the first
        if suspect % first_arg == 0:
            result.append(suspect)
        suspect += second_arg
    return result
