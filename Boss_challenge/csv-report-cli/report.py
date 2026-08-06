def generate_report(rows):
    report = []
    report.append("CSV REPORT")
    report.append("====================")
    report.append(f"Total Rows: {len(rows)}")
    return "\n".join(report)