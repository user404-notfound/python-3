import csv

def find_total_visits():
    total_visits = 0
    # List of weekly CSV files
    files = ["week-1.csv", "week-2.csv", "week-3.csv"]

    for filename in files:
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header line

                for row in reader:
                    # Each row looks like: ["Alice", "1", "1", "0", "0", "1", "0", "1"]
                    # Convert the visit columns (skip name) to integers and sum them
                    visits = sum(int(x.strip()) for x in row[1:])
                    total_visits += visits

        except FileNotFoundError:
            print(f"File '{filename}' not found. Skipping...")

    return total_visits


def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

# Run example
ex2()
