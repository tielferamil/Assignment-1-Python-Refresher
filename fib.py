import functools
import time
import matplotlib.pyplot as plt

timing_data = []


def timer(func):
    @functools.wraps(func)
    def wrapper(n):
        start_time = time.perf_counter()
        result = func(n)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        timing_data.append((n, elapsed_time))
        print(f"Finished in {elapsed_time:.10f}s: f({n}) -> {result}")
        return result

    return wrapper


@functools.lru_cache(maxsize=None)
@timer
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    max_n = 100
    fib(max_n)

    x_values = [n for n, _ in timing_data]
    y_values = [time for _, time in timing_data]

    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values, linestyle="-")
    plt.xlabel("n (Fibonacci number index)")
    plt.ylabel("Execution Time in seconds")
    plt.grid(True)
    plt.savefig("fibonacci_timing_plot.png")
    plt.show()
