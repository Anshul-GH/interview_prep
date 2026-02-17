import time
from contextlib import contextmanager  # Generator-based (simpler than class)

@contextmanager
def timer(description):
    start = time.time()
    yield  # Run the 'with' block code here
    elapsed = time.time() - start
    print(f"{description}: {elapsed:.2f}s")

# Usage
with timer("Slow computation"):
    total = sum(i * i for i in range(10_000_000))  # Simulate work
print("Result:", total)
