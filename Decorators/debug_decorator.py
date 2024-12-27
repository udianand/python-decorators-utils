from typing import Callable, Any


def debug_decorator(func: Callable) -> Callable:

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(
            f"Function {func.__name__} called with arguments {args} and keywargs {kwargs}"
        )
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
    return wrapper
