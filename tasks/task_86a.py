"""86a. Given a natural number n. Find digits length in the number n."""

from tasks.utils import is_natural_number


def task_86a(number: int) -> int:
    """Get digits length in the number."""
    assert is_natural_number(number), "The number should be natural"
    return len(str(number))


if __name__ == "__main__":
    NUMBER = 13456
    print(task_86a(NUMBER))
