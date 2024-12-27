from typing import Callable

def cache_decorator(func: Callable) -> Callable:
  cache = {}

  def wrapper(*args: int) -> int:

    if args in cache:
      print(f"Cache hit for {args}")
      return cache[args]

    result = func(*args)
    cache[args] = result
    return result

  return wrapper
