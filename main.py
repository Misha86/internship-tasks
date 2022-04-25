""" This module consists of one function that run my tasks. """
import inspect
import sys
import types

from tasks_86_a_b_330 import (task_86a, task_86b, task_330)

data_dict = locals()


def main(tasks_dict: dict):
    """ Get result from function executions. """
    # get tasks list from locals() dict
    tasks_list = [task.lstrip('task_') for task in tasks_dict.keys() if task.startswith('task_')]

    task_number_message = "Input task`s number: "
    task_args_message = "Input args: "

    while True:
        print(f"\n{'-'*80}\n {f'Available tasks: {tasks_list}':^80}\n{'-'*80}")
        print(f"*** If you want to exit input 'E'!\n{'-'*80}")
        task_number = input(task_number_message)

        try:
            # key_func is name of our function or module with same name
            key_func = sys.exit() if task_number.lower() == 'e' else 'task_' + task_number
            # get module or function from locals() dict
            module_data = data_dict[key_func]
            # check module_data and get function
            func = getattr(module_data, key_func) if isinstance(module_data, types.ModuleType) \
                else module_data
            # check that our function can take args, kwargs
            args_exist = inspect.getfullargspec(func)
            print(f"{'-'*80}\n --{func.__doc__}\n{'-'*80}")
        except KeyError:
            task_number_message = f"Input correct task`s number, task " \
                                  f"'{task_number}' does not exist: "
            continue

        while True:
            # if func can take args, input args else pass
            task_args = input(task_args_message) if any(list(args_exist)) else None
            if task_args and task_args.lower() == 'e':
                sys.exit()
            try:
                # get result for func implementation with args or without
                result = func(*list(map(int, task_args.split(' ')))) if task_args else func()
                print("\n" + f" Result of task {task_number}: {result} ".center(80, "*"))
                return main(tasks_dict)
            except (TypeError, ValueError) as ex:
                task_args_message = f"Input correct args({type(ex).__name__}: {ex}): "
                continue


if __name__ == "__main__":
    main(data_dict)
