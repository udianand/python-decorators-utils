from timing_decorators import timing_decorator
import time

@timing_decorator
def slow_function():
  time.sleep(2)
  print("I am slow")

if __name__ == "__main__":
    slow_function()
