import csv
import random
import time
from datetime import datetime


def csv_test(file_size=1000000):
    # Generate header
    header = [
        "A1",
        "A2",
        "A3",
        "A4",
        "A5",
        "A6",
        "A7",
        "A8",
        "A9",
        "A10",
        "A11",
        "A12",
        "A13",
    ]

    # Open file to write data
    with open("data/csv_test.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write header
        writer.writerow(header)

        # Start timer
        start_time = time.time()

        for i in range(file_size):
            row = [
                f"Name_{i}",
                f"email_{i}@example.com",
                random.randint(3, 999999),
                random.randint(4, 999999),
                random.randint(5, 999999),
                random.randint(6, 999999),
                random.randint(7, 999999),
                random.randint(8, 999999),
                random.randint(9, 999999),
                random.randint(10, 999999),
                random.randint(11, 999999),
                random.randint(12, 999999),
                random.randint(13, 999999),
            ]
            writer.writerow(row)

        # Stop timer
        end_time = time.time()

        # Calculate elapsed time
        elapsed_time = end_time - start_time

    return elapsed_time


# Run the test and get the time taken
csv_time = csv_test()
csv_time
print(f"#### CSV test finished")
