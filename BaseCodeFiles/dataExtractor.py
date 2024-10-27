import csv
import os

class DataHandler:
    def __init__(self, file_path='data.csv'):
        self.file_path = file_path
        if not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0:
            self._initialize_file()

    def _initialize_file(self):
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Item', 'Data'])
            writer.writerow(['currentBalance', 100])
            writer.writerow(['currentRent', 40])
            writer.writerow(['savingsBalance', 50])
            writer.writerow(['healthLevel', 100])
            writer.writerow(['hungerLevel', 100])
            writer.writerow(['happinessLevel', 100])

    def replace_value(self, dataType, new_value):
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row[0] == dataType:
                row[1] = str(new_value)

        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    def read_value(self, dataType):
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row[0] == dataType:
                return row[1]

        raise ValueError(f"{dataType} not found in {self.file_path}")


data_handler = DataHandler()

'''
#Example of how to use the functions for read and write data
value = data_handler.read_value('currentBalance')
print(f"The current balance is: {value}")
data_handler.replace_value('currentBalance', '50')
'''