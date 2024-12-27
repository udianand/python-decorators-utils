from typing import Callable, Any
import time


def retry_decorator(max_retries: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = max_retries
            while retries > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries -= 1
                    print(f"Retrying {retries} retries left")
                    time.sleep(1)
                    if retries == 0:
                        raise e

        return wrapper

    return decorator
