import time
import threading


def simple_task():
    total = 0
    for i in range(20000000):
        total += i


def multi_threading_test_adjustable(num_threads=12):
    """
    num_threads: Set this to the number of logical processors or physical cores
                 based on your CPU for optimal performance.
    """
    # Start timer
    start_time = time.time()

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=simple_task)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Stop timer
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time

    return elapsed_time


# Example usage: If your CPU has 4 logical processors, set num_threads=4
multi_threading_time_adjustable = multi_threading_test_adjustable(num_threads=12)
multi_threading_time_adjustable
print(f"#### Multi thread test finished")
