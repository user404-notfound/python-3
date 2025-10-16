# Custom Exception Class
class ValidationException(Exception):
    pass

# Function to validate file contents
def validate_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split by space or comma depending on format (you can adjust)
                parts = line.strip().split()
                for part in parts:
                    # Check if the part looks like a number (mileage)
                    if part.replace('.', '', 1).isdigit():
                        # If mileage has a decimal point, raise exception
                        if '.' in part:
                            raise ValidationException(f"Invalid mileage:  {part}")
                    # If not a number, skip (it may be a car name, etc.)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Example usage
def ex1():
    try:
        validate_file("input.txt")
    except ValidationException as ve:
        print(ve)

# Run example
ex1()
