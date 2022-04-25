"""This module consists of task_559."""


def sieve_of_eratosthenes(target: int) -> list[int]:
    """
    Get sieve for Mersen sequence.
    """
    if target == 0:
        return []

    # an list of Bool vales to index numbers 2 to n (0 to n-2)
    sieve = [True] * (target - 1)
    # limit for loop
    limit = round(pow(target, 1 / 2))

    # sieve numbers
    for number in range(2, limit + 1):
        if sieve[number - 2]:
            for suspect in range(pow(number, 2), target + 1, number):
                sieve[suspect - 2] = False

    # get list of natural numbers
    result = [1]
    for pos, cell in enumerate(sieve):
        if cell:
            result.append(pos + 2)

    return result


# get (limited) Mersen sequence with simple indexes
def task_559(limit: int) -> list[int]:
    """
    Get Mersen sequence limited by natural number
    """
    result = []

    sieve = sieve_of_eratosthenes(limit)

    for natural_number in sieve:
        mermen_candidate = pow(2, natural_number) - 1
        if mermen_candidate >= limit:
            break
        result.append(mermen_candidate)

    return result
