from reader import read_csv
from report import generate_report
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("csv_file")
parser.add_argument("output_file")

args = parser.parse_args()
filename = args.csv_file
output_file = args.output_file

try:
    rows = read_csv(filename)

    if not rows:
        print("Error: The CSV file is empty.")
        exit()

    report = generate_report(rows)
    print(report)

    with open(output_file, "w") as file:
        file.write(report)
        
except FileNotFoundError:
    print(f"Error: '{filename}' was not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print(f"Unexpected error: {e}")