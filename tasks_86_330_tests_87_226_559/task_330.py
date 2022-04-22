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
    NUMBER = 100000000000
    start = time.time()
    print(perfect_numbers(NUMBER))
    print(time.time() - start)


# def perfect_numbers(number: int) -> list[int]:
#     """
#     Get perfect numbers in range(1, number)
#     :param number: int
#     :return: list[int]
#     """
#     numbers = []
#     for num in range(0, number, 2):
#         dividers = [div for div in range(1, int(num / 2) + 1) if num % div == 0]
#         if sum(dividers) == num:
#             numbers.append(num)
#     return numbers[1:]


# def perfect_numbers1(number: int) -> list[int]:
#     """
#     Get perfect numbers in range(1, number)
#     :param number: int
#     :return: list[int]
#     """
#     if number < 7:
#         return []
#     # d = n(2n - 1)
#     d = []
#     for i in range(number):
#         v = i*(2*i - 1)
#         if v >= number:
#             break
#         d.append(v)
#     # print(d)
#     numbers_variants = [0, ]
#     for i in range(1, int(pow(number, 0.33)), 2):
#         b = numbers_variants[-1] + i ** 3
#         numbers_variants.append(b)
#
#     # numbers = [6, ]
#     # for num in numbers_variants[1:]:
#     #     dividers = [div for div in range(1, int(num / 2) + 1) if num % div == 0]
#     #     if sum(dividers) == num:
#     #         numbers.append(num)
#     def d(arg):
#         bin_arg = bin(arg).replace('0b', '')
#         len_arg = len(bin_arg)
#         len_1 = int(len_arg / 2) + 1
#         len_0 = len_arg - len_1
#         count_1 = bin_arg[0:len_1].count('1')
#         count_0 = bin_arg[len_1:].count('0')
#         return len_1 == count_1 and count_0 == len_0
#
#     a = [i for i in numbers_variants if
#          i % 9 == 1 and i % 2 == 0 and (str(i)[-2:] in ("16", "28", "36", "56", "76", "96"))]
#
#     def b(arg):
#         if arg == 1:
#             return 1
#         elif len(str(arg)) == 1 and arg != 1:
#             return False
#         else:
#             sum_digit = sum([int(i) for i in str(arg)])
#         return b(sum_digit)
#
#     v = list(filter(b, filter(d, a)))
#     print(b(8589869056))
#     print(v)
#     numbers = [6, ]
#     for num in v:
#         dividers = [div for div in range(1, int(num / 2) + 1) if num % div == 0]
#         if sum(dividers) == num:
#             numbers.append(num)
#     print(numbers)
#     # print([bin(i) for i in numbers_variants if i%9 == 1 and i%2 == 0 and (str(i)[-2:] in ("16", "28", "36", "56", "76", "96"))])
#     # print([i for i in numbers_variants if i%9 == 1 and i%2 == 0])
