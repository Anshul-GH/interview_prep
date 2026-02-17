import time
from functools import wraps

def timer(func):
    @wraps(func)  # Best practice to avoid func.__name__ becoming 'wrapper'
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function(n):
    time.sleep(n / 10)  # Simulate work
    return n * 2

# Usage
for i in range(10):
    print(slow_function(i))
