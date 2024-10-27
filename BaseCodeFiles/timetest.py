import csv
from datetime import datetime

# Define the file name
filename = "time_log.csv"

# Get the current time
current_time = datetime.now()

# Function to write the current time to the CSV file
def write_current_time():
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["last_run"])
        writer.writerow([current_time.isoformat()])

# Function to read the last run time from the CSV file
def read_last_run_time():
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                last_run = datetime.fromisoformat(row["last_run"])
                return last_run
    except (FileNotFoundError, KeyError, ValueError):
        # If the file does not exist or is malformed, return None
        return None

# Read the last run time
last_run_time = read_last_run_time()

# If there is a previous run time, calculate the time difference in seconds
if last_run_time:
    time_difference = current_time - last_run_time
    seconds_difference = time_difference.total_seconds()
    print(f"It has been {seconds_difference:.2f} seconds since the last run.")
else:
    print("This is the first time the code is being run or no valid time is recorded.")

# Write the current time to the CSV file
write_current_time()