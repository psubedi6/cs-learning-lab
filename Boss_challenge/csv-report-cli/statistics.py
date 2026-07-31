import statistics

def count(items):
    print(f"There are {len(items)} items.")
    return len(items)

def average(numbers):
    return statistics.mean(numbers)

def minimum(numbers):
    mini = min(numbers)
    return mini

def maximum(numbers):
    maxi = max(numbers)
    return maxi

def group_by(rows, column):
    groups = {}
    for row in rows:
        key = row[column]
        if key not in groups:
            groups[key]= []
        groups[key].append(row)