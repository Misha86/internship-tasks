"""559. Given a natural number n. Find all Mersenne numbers less than n.

(A prime number is called a Mersenne number if it can
be represented as 2^p - 1, where p is also a prime number.)
"""

from tasks.utils import is_natural_number


def sieve_of_eratosthenes(target: int) -> list[int]:
    """Return list of prime numbers (Eratosthenes Algorithm), less than target argument."""
    assert is_natural_number(target), "The number should be natural"
    # an list of Bool vales to index numbers 2 to n (0 to n-2)
    sieve = [True]*(target-1)
    # limit for loop
    limit = round(pow(target, 1/2))
    # sieve numbers
    for number in range(2, limit+1):
        if sieve[number-2]:
            for suspect in range(pow(number, 2), target+1, number):
                sieve[suspect-2] = False
    # get list of natural numbers
    result = [1]
    for pos, cell in enumerate(sieve):
        if cell:
            result.append(pos+2)
    return result


def task_559(limit: int) -> list[int]:
    """Return list of Mersenne numbers, less than limit argument."""
    assert is_natural_number(limit), "The number should be natural"
    result = []
    # get natural numbers list
    sieve = sieve_of_eratosthenes(limit)
    # form list of Mersenne numbers limited by given argument
    for natural_number in sieve:
        mersenne_candidate = pow(2, natural_number) - 1
        if mersenne_candidate >= limit:
            break
        else:
            result.append(mersenne_candidate)
    return result
