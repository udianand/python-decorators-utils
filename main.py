from Decorators.timing_decorators import timing_decorator
from Decorators.cache_decorator import cache_decorator
import time


@timing_decorator
def slow_function()->str:
  time.sleep(2)
  return "finished"

@cache_decorator
def fibonacci(n):
  if n < 2: return n
  return fibonacci(n - 1) + fibonacci(n - 2)

@cache_decorator
def compute_square(n):
    print(f"Computing square of {n}")
    return n * n


if __name__ == "__main__":
    # Test it
    print(compute_square(4))
    print(compute_square(4))  # This should return the cached result

