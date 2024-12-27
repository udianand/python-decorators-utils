
from typing import Callable, Dict, TypeVar, Any, Tuple

T = TypeVar('T')

def cache_decorator(func: Callable[..., T]) -> Callable[..., T]:
  cache: Dict[Tuple[Any, ...], T] = {}

  def wrapper(*args: Any) -> T:
    if args in cache:
      print(f"Cache hit for {args}")
      return cache[args]

    result = func(*args)
    cache[args] = result
    return result

  return wrapper
