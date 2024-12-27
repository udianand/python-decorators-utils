from typing import Callable

def cache_decorator(func:Callable)->Callable:
  cache = {}
  
  def wrapper(*args, **kwargs):
    
    if args in cache: 
      print(f"Cache hit for {args}")
      return cache[args]
    
    result = func(*args,**kwargs)
    cache[args] = result
    return result
    
  return wrapper

