import sqlite3
import random
import time


def sql_test(table_size=5000000):
    # Connect to SQLite database in memory
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Create table
    cursor.execute(
        """CREATE TABLE users (name TEXT, age INTEGER, email TEXT, rand1 INTEGER)"""
    )

    # Start timer
    start_time = time.time()

    # Populate table
    for i in range(table_size):
        cursor.execute(
            "INSERT INTO users VALUES (?, ?, ?, ?)",
            (
                f"Name_{i}",
                random.randint(18, 65),
                f"email_{i}@example.com",
                random.randint(0, 99999),
            ),
        )

    # Create an index on the 'age' column for more complexity
    cursor.execute("CREATE INDEX age_index ON users (age)")

    # Perform some queries to add complexity
    cursor.execute("SELECT * FROM users WHERE age > 30")
    cursor.execute("SELECT * FROM users WHERE age < 30 AND name LIKE 'Name_1%'")

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Stop timer
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time

    return elapsed_time


# Run the test and get the time taken
sql_time = sql_test()
sql_time
print(f"#### SQL test finished")
