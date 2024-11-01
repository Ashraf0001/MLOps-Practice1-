import csv
import random
import string

# Define the file path
file_path = '/Users/ashraf96/Desktop/mldemo/project-name/data/raw/sample_raw_data.csv'

# Define the number of rows
num_rows = 500

# Define the header
header = ['ID', 'Name', 'Age', 'City']

# Generate random data
def generate_random_data(num_rows):
    data = []
    for i in range(num_rows):
        row = [
            i + 1,
            ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5)),
            random.randint(18, 70),
            ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=7))
        ]
        data.append(row)
    return data

# Write data to CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(generate_random_data(num_rows))