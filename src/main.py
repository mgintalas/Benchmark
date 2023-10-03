# Import the 'csv' module for writing results to a CSV file
import csv
from csv_test_ import csv_test
from disk_io_test_ import disk_io_test
from hardware_info_ import get_hardware_info
from multi_threading_test_ import multi_threading_test_adjustable
from python_benchmarks_ import python_benchmarks
from sql_test_ import sql_test
from datetime import datetime
import os


def main():
    # Define test functions and initial results dictionary
    tests = [
        ("CSV Test", csv_test),
        ("SQL Test", sql_test),
        (
            "Python Benchmarks - List Comprehension",
            lambda: python_benchmarks()["List Comprehension"],
        ),
        (
            "Python Benchmarks - String Concatenation",
            lambda: python_benchmarks()["String Concatenation"],
        ),
        (
            "Python Benchmarks - Dictionary Operations",
            lambda: python_benchmarks()["Dictionary Operations"],
        ),
        ("Multi-threading Test", multi_threading_test_adjustable),
        ("Disk Write", lambda: disk_io_test()[0]),
        ("Disk Read", lambda: disk_io_test()[1]),
        ("CPU Logical Cores", lambda: get_hardware_info()["CPU Logical Cores"]),
        ("CPU Physical Cores", lambda: get_hardware_info()["CPU Physical Cores"]),
        ("Total RAM (GB)", lambda: get_hardware_info()["Total RAM (GB)"]),
        ("Available RAM (GB)", lambda: get_hardware_info()["Available RAM (GB)"]),
    ]

    # Create a new column name based on the current timestamp
    new_col_name = f"Run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # Initialize or read existing rows
    rows = []
    if os.path.exists("data/results.csv"):
        with open("data/results.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)
    else:
        rows.append(["Test", new_col_name])
        for test_name, _ in tests:
            rows.append([test_name])

    # Append new results
    rows[0].append(new_col_name)
    for i, (test_name, test_func) in enumerate(tests, start=1):
        new_result = test_func()
        rows[i].append(str(new_result))

    # Write back to CSV
    with open("data/results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


if __name__ == "__main__":
    for i in range(10):
        print(f"Running iteration {i + 1}...")
        main()
        print(f"Completed iteration {i + 1}\n")

