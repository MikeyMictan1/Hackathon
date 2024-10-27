import time
from datetime import datetime

class Savings:
    def __init__(self, player):
    # Define the file name to store the last run time
        self.filename = "last_run_time.txt"
        self.minutes_difference = 0
        self.player = player

    # Function to write the current time to the file
    def write_current_time(self):
        with open(self.filename, 'w') as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M"))


    # Function to read the last run time from the file
    def read_last_run_time(self):
        try:
            with open(self.filename, 'r') as file:
                last_run_str = file.read().strip()
                return datetime.strptime(last_run_str, "%Y-%m-%d %H:%M")
        except (FileNotFoundError, ValueError):
            # If the file does not exist or is malformed, return None
            return None

    def run(self):
        # Get the last run time and the current time
        last_run_time = self.read_last_run_time()
        current_time = datetime.now()

        # Calculate the number of minutes since the last run
        if last_run_time:
            time_difference = current_time - last_run_time
            self.minutes_difference = int(time_difference.total_seconds() / 60)
            if self.minutes_difference > 0:
                self.player.savings_balance = self.player.savings_balance * 1.025 * self.minutes_difference

        # Update the last run time to the current time
        self.write_current_time()

        # Store the last checked minute for ongoing monitoring
        last_minute = current_time.strftime("%Y-%m-%d %H:%M")


        # Continuous loop to print "hello world" at the start of each new minute

            # Get the current time
        current_time = datetime.now()
        current_minute = current_time.strftime("%Y-%m-%d %H:%M")

            # Check if the minute has changed
        if current_minute != last_minute:
            self.player.savings_balance = 1.025*self.player.savings_balance


                # Update the last run time in the file for future reference
            self.write_current_time()

            # Wait for a few seconds before checking again to avoid high CPU usage
