from typing import Callable


def execution_counter(func: Callable) -> Callable:
    count = 0

    def wrapper(*args: any, **kwargs: any) -> any:
        nonlocal count
        count += 1
        print(f"Function {func.__name__} called {count} times")
        return func(*args, **kwargs)

    return wrapper
