import time
import os


def disk_io_test(file_size=3000000000):  # File size in bytes
    # Generate random bytes
    data = os.urandom(file_size)

    # Write to disk
    write_start_time = time.time()
    with open("data/temp_file", "wb") as f:
        f.write(data)
    write_end_time = time.time()

    write_time = write_end_time - write_start_time

    # Read from disk
    read_start_time = time.time()
    with open("data/temp_file", "rb") as f:
        read_data = f.read()
    read_end_time = time.time()

    read_time = read_end_time - read_start_time

    os.remove("data/temp_file")

    return write_time, read_time


# Run the test and get the time taken for write and read operations
disk_write_time, disk_read_time = disk_io_test()
disk_write_time, disk_read_time
print(f"#### Disk IO test finished")
