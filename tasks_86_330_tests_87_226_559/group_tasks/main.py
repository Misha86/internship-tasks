"""This module consists of group tasks."""


# task 86a
def task_86a(number: int) -> int:
    """
    Get digits length in the number
    :param number: int
    :return: int
    """
    if not isinstance(number, int):
        raise TypeError("Argument should be integer!")
    if number <= 0:
        raise ValueError("Argument is not natural number!")
    return len(str(number))


# task 86b
def task_86b(number: int) -> int:
    """
    Get digits sum in the number
    :param number: int
    :return: int
    """
    if not isinstance(number, int):
        raise TypeError("Argument should be integer!")
    if number <= 0:
        raise ValueError("Argument is not natural number!")
    return sum([int(num) for num in str(number)])


def check_simple_number(number: int) -> bool:
    """
    Check that number is simple
    :param number: int
    :return: bool
    """
    counter = 0
    for i in range(1, int(number / 2) + 1):
        if counter > 2:
            break
        if number % i == 0:
            counter += 1
    return counter == 1


# task 330
def task_330(number: int) -> list[int]:
    """
    Get perfect numbers in range(1, number)
    :param number: int
    :return: list[int]
    """
    if number <= 0:
        raise ValueError("Argument is not natural number!")

    if number <= 6:
        return []

    result = [6, ]

    for index in range(3, 100, 2):
        expect_simple_num = pow(2, index) - 1
        is_simple = check_simple_number(expect_simple_num)
        if is_simple:
            value = pow(2, index - 1) * (pow(2, index) - 1)
            if value >= number:
                break
            result.append(value)
    return result


# cut & sum the digit from tail of target number a given number of times
def get_sum_of_lasts_few(target: int, tail_size: int) -> int:
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
    return target % 10 + get_sum_of_lasts_few(target // 10, tail_size)


# return all natural common multiples less than first_arg * second_arg
def get_natural_common_multiples(first_arg: int, second_arg: int) -> list[int]:
    """
    Get natural common multiples
    :param first_arg: int
    :param second_arg: int
    :return: list[int]
    """
    limit = first_arg * second_arg
    suspect = second_arg
    result = []
    while suspect < limit:
        if suspect % first_arg == 0:
            result.append(suspect)
        suspect += second_arg

    return result


def sieve_of_eratosthenes(target: int) -> list[int]:
    """
    Get sieve for Mersen sequence
    :param target: int
    :return: list[int]
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
def get_mersen_sequence_limited_by_natural_number(limit: int) -> list[int]:
    """
    Get Mersen sequence limited by natural number
    :param limit: int
    :return: list[int]
    """
    result = []

    sieve = sieve_of_eratosthenes(limit)

    for natural_number in sieve:
        mermen_candidate = pow(2, natural_number) - 1
        if mermen_candidate >= limit:
            break
        result.append(mermen_candidate)

    return result


data_dict = {"86a": {"func": task_86a, "args_count": 1},
             "86b": {"func": task_86b, "args_count": 1},
             "330": {"func": task_330, "args_count": 1},
             }


def main(tasks_dict: dict) -> bool:
    """
    Get result from function executions
    :param tasks_dict: dict
    :return: bool
    """
    task_number_message = "Input task`s number: "
    task_args_message = "Input args: "

    while True:
        task_number = input(task_number_message)

        try:
            func_data = tasks_dict[task_number]
            args_count = func_data['args_count']
        except KeyError:
            task_number_message = "Input correct task`s number: "
            continue

        while True:
            task_args = input(task_args_message)
            args = task_args.split(' ')

            try:
                func = func_data["func"]
                args = list(map(int, args))
                print(f"\n{'*' * 20} Result: {func(*args)} {'*' * 20}")
                return True
            except (KeyError, ValueError, TypeError):
                task_args_message = f"Input correct args. Count of args {args_count}: "
                continue


if __name__ == "__main__":
    main(data_dict)
