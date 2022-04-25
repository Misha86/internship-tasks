"""This module consists of group tasks."""
import inspect
import sys
import types

from tasks_86_a_b_330 import (task_86a, task_86b, task_330)


data_dict = locals()


def main(tasks_dict: dict) -> bool:
    """ Get result from function executions. """
    # get tasks list from locals() dict
    tasks_list = [task.lstrip('task_') for task in tasks_dict.keys() if task.startswith('task_')]

    print(f"\n{'*-'*5} Available tasks: {tasks_list} {'*-'*5}")
    print("*If you want to exit input 'exit'!")
    task_number_message = "Input task`s number: "
    task_args_message = "Input args: "

    while True:
        task_number = input(task_number_message)

        try:
            # key_func is name of our function or module with same name
            key_func = 'task_' + task_number if task_number != 'exit' else sys.exit()
            # get module or function from locals() dict
            module_data = data_dict[key_func]
            # check module_data and get function
            func = getattr(module_data, key_func) if isinstance(module_data, types.ModuleType) \
                else module_data
            # check that our function can take args, kwargs
            args_exist = inspect.getfullargspec(func)
        except KeyError:
            task_number_message = f"Input correct task`s number, task " \
                                  f"'{task_number}' does not exist: "
            continue

        while True:
            # if func can take args, input args else pass
            task_args = input(task_args_message) if any(list(args_exist)) else None
            if task_args.lower() == 'exit':
                sys.exit()
            try:
                # get result for func implementation with args or without
                result = func(*list(map(int, task_args.split(' ')))) if task_args else func()
                print(f"\n{'*' * 20} Result: {result} {'*' * 20}")
                return True
            except (TypeError, ValueError) as ex:
                task_args_message = f"Input correct args({type(ex).__name__}: {ex}): "
                continue


if __name__ == "__main__":
    main(data_dict)
