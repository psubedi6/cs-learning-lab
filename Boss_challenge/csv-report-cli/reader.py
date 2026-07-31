import csv
def read_csv(filename):
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)