"""This module consists of group tasks."""


# task 86a
def count_digits(number: int) -> int:
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
def sum_digits(number: int) -> int:
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
def perfect_numbers(number: int) -> list[int]:
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


data_dict = {"86a": {"func": count_digits, "args_count": 1},
             "86b": {"func": sum_digits, "args_count": 1},
             "330": {"func": perfect_numbers, "args_count": 1},
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
