#!/usr/bin/env python3
# Decorator Example
def timer_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time: {end - start:.4f}s")
        return result
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    print("Done!")

def main():
    slow_function()

if __name__ == "__main__":
    main()
