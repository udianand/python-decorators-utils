
from typing import Callable


def retry_decorator(max_retries: int) -> Callable:

  def decorator(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
      retries = 3
      while retries > 0:
        try:
          return func(*args, **kwargs)
        except Exception as e:
          retries -= 1
          if retries == 0:
            raise e
    return wrapper
  return decorator
