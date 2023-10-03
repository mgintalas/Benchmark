import timeit


def python_benchmarks():
    # Prepare result dictionary
    results = {}

    # List comprehension
    list_comprehension_time = timeit.timeit("[x*x for x in range(1000)]", number=500000)
    results["List Comprehension"] = list_comprehension_time

    # String concatenation
    string_concat_time = timeit.timeit(
        '"-".join(str(x) for x in range(100))', number=1000000
    )
    results["String Concatenation"] = string_concat_time

    # Dictionary operations
    dict_operations_time = timeit.timeit(
        "d = {x: x*x for x in range(1000)}", number=100000
    )
    results["Dictionary Operations"] = dict_operations_time

    return results


# Run the test and get the time taken for each operation
python_benchmarks_time = python_benchmarks()
python_benchmarks_time
print(f"#### Python benchmarks finished")
