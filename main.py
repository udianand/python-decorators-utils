
from Decorators import timing_decorator, cache_decorator
from Decorators.execution_counter import execution_counter

import time

@timing_decorator
def example_timing():
    time.sleep(1)
    return "Timing decorator test complete"

@cache_decorator
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@execution_counter
def greet(name):
    print(f"Hello, {name}")

if __name__ == "__main__":
    # Test timing decorator
    print("\nTesting timing decorator:")
    example_timing()
    
    # Test cache decorator
    print("\nTesting cache decorator with Fibonacci:")
    print(f"fibonacci(5) = {fibonacci(5)}")
    print("Calling again (should hit cache):")
    print(f"fibonacci(5) = {fibonacci(5)}")

    # Test function execution decorator
    print("\nTesting function execution decorator:")
    greet("Alice")
    greet("Bob")
    
