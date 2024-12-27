
# Python Decorators Utils

A collection of useful Python decorators including:
- Timing decorator: Measures function execution time
- Cache decorator: Implements function result caching
- Debug decorator: Logs function calls and returns
- Execution counter: Counts function calls
- Retry decorator: Retries failed function calls

## Installation
```bash
pip install python-decorators-utils
```

## Usage

```python
from python_decorators_utils import timing_decorator, cache_decorator
from python_decorators_utils import debug_decorator, execution_counter
from python_decorators_utils import retry_decorator

# Timing Decorator - Measures execution time
@timing_decorator
def slow_function():
    time.sleep(1)
    return "done"

# Cache Decorator - Memoizes results
@cache_decorator
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

# Debug Decorator - Logs function calls
@debug_decorator
def greet(name):
    return f"Hello, {name}"

# Execution Counter - Tracks calls
@execution_counter
def counted_function():
    return "I'm being counted!"
print(counted_function.get_count())  # Get number of calls

# Retry Decorator - Handles failures
@retry_decorator(max_retries=3)
def may_fail():
    # Will retry up to 3 times if fails
    return risky_operation()
```

## Features
- All decorators preserve function metadata using `functools.wraps`
- Type hints supported
- Compatible with Python 3.11+
- Can be used individually or stacked together
- Uses closures for maintaining state (like in execution counter)

## Contributing
Pull requests are welcome. Please ensure tests pass before submitting.
