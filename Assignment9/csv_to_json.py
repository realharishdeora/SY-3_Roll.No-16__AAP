import csv
import json

csv_file = input("Enter CSV file name: ")
json_file = input("Enter JSON file name: ")

data = []

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data.append(row)

with open(json_file, "w") as file:
    json.dump(data, file, indent=4)

print("CSV file converted to JSON successfully.")