import boto3

def calculate():
    log_entries = []
    student_id = "12345"   # ← replace with your actual student ID
    log_filename = f"calculator-log-{student_id}.txt"

    while True:
        first = input("Enter first number: ").strip()
        if first.lower() == "q":
            break
        second = input("Enter second number: ").strip()

        # Validate numeric inputs
        try:
            num1 = float(first)
            num2 = float(second)
        except ValueError:
            print("Please enter valid numbers.")
            continue

        result = num1 + num2
        entry = f"{num1} + {num2} = {result}"
        log_entries.append(entry)
        print(entry)

    # Write log file
    if log_entries:
        with open(log_filename, "w") as f:
            for line in log_entries:
                f.write(line + "\n")

        # Upload to S3 (optional – requires valid AWS credentials)
        try:
            s3 = boto3.client("s3")
            bucket_name = "your-bucket-name"   # ← replace with your actual S3 bucket
            s3.upload_file(log_filename, bucket_name, log_filename)
            print("*** Uploaded to S3 ***")
        except Exception as e:
            print(f"(Skipped upload) Error: {e}")
    else:
        print("No calculations to log.")


# Usage example
def ex4():
    calculate()


# Run
if __name__ == "__main__":
    ex4()
