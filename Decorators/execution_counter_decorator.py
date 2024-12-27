from typing import Callable, Any


def execution_counter(func: Callable) -> Callable:
    count = 0

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        nonlocal count
        count += 1
        print(f"Function {func.__name__} called {count} times")
        return func(*args, **kwargs)

    return wrapper
