"""
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
"""

import time
from datetime import datetime

# Define the file name to store the last run time
filename = "last_run_time.txt"


# Function to write the current time to the file
def write_current_time():
    with open(filename, 'w') as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M"))


# Function to read the last run time from the file
def read_last_run_time():
    try:
        with open(filename, 'r') as file:
            last_run_str = file.read().strip()
            return datetime.strptime(last_run_str, "%Y-%m-%d %H:%M")
    except (FileNotFoundError, ValueError):
        # If the file does not exist or is malformed, return None
        return None


# Get the last run time and the current time
last_run_time = read_last_run_time()
current_time = datetime.now()

# Calculate the number of minutes since the last run
if last_run_time:
    time_difference = current_time - last_run_time
    minutes_difference = int(time_difference.total_seconds() / 60)
    print(f"{minutes_difference} minute(s) have passed since the script was last run.")

    # Print "hello world" for each missed minute
    for _ in range(minutes_difference):
        print("hello world")
else:
    print("This is the first time the code is being run or no valid time is recorded.")

# Update the last run time to the current time
write_current_time()

# Store the last checked minute for ongoing monitoring
last_minute = current_time.strftime("%Y-%m-%d %H:%M")

print("Continuing to monitor. 'hello world' will print at the start of each new minute.")

# Continuous loop to print "hello world" at the start of each new minute
while True:
    # Get the current time
    current_time = datetime.now()
    current_minute = current_time.strftime("%Y-%m-%d %H:%M")

    # Check if the minute has changed
    if current_minute != last_minute:
        print("hello world")
        last_minute = current_minute
        # Update the last run time in the file for future reference
        write_current_time()

    # Wait for a few seconds before checking again to avoid high CPU usage
    time.sleep(1)