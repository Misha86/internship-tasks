"""86b. Given a natural number n. Find digits sum in the number n."""

from tasks.utils import is_natural_number


# task 86b
def task_86b(number: int) -> int:
    """Get digits sum in the number."""
    assert is_natural_number(number), "The number should be natural"
    return sum([int(num) for num in str(number)])


if __name__ == "__main__":
    NUMBER = 13456
    print(task_86b(NUMBER))
