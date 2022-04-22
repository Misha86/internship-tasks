"""This module provides function to get perfect numbers."""
import time


def sieve_of_eratosthenes(number):
    """Create a boolean array "prime[0..n]" and initialize
     all entries it as true. A value in prime[i] will
     finally be false if i is Not a prime, else true."""
    prime = [True] * (number + 1)
    position = 2
    while position * position <= number:

        # If prime[position] is not changed, then it is a prime
        if prime[position] is True:

            # Update all multiples of position
            for i in range(position ** 2, number + 1, position):
                prime[i] = False
        position += 1
    prime[0] = False
    prime[1] = False
    if prime[number]:
        return True
    return False


def perfect_numbers(number: int) -> list[int]:
    """
    Get perfect numbers in range(1, number)
    :param number: int
    :return: list[int]
    """

    result = [6, ]

    for index in range(1, 100, 2):
        mermen_candidate = pow(2, index) - 1
        sieve = sieve_of_eratosthenes(mermen_candidate)
        if sieve:
            value = pow(2, index - 1) * (pow(2, index) - 1)
            if value >= number:
                break
            result.append(value)
    return result


if __name__ == "__main__":
    NUMBER = 1000000000000
    start = time.time()
    print(perfect_numbers(NUMBER))
    print(time.time() - start)
