import numpy as np

MISSING_VALUES = {"", "NA", "null", "None"}

def read_csv_manual(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    headers = lines[0].strip().split(",")
    rows = []

    for line in lines[1:]:
        values = line.strip().split(",")
        rows.append(values)

    return headers, rows


def extract_numeric_column(rows, column_index):
    numbers = []
    missing_count = 0

    for row in rows:
        value = row[column_index]

        if value in MISSING_VALUES:
            missing_count += 1
        else:
            try:
                numbers.append(float(value))
            except:
                missing_count += 1

    return numbers, missing_count


def frequency_analysis(rows, column_index):
    frequency = {}

    for row in rows:
        value = row[column_index]

        if value in MISSING_VALUES:
            continue

        frequency[value] = frequency.get(value, 0) + 1

    return sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:5]


def main():
    headers, rows = read_csv_manual("data.csv")

    age_index = headers.index("Age")
    city_index = headers.index("City")

    ages, missing_values = extract_numeric_column(rows, age_index)

    mean_age = np.mean(ages)
    median_age = np.median(ages)
    std_age = np.std(ages)

    top_cities = frequency_analysis(rows, city_index)

    report = open("summary_report.txt", "w")

    report.write("Column Analyzed: Age\n")
    report.write(f"Total Records: {len(rows)}\n")
    report.write(f"Missing Values: {missing_values}\n")
    report.write(f"Mean: {mean_age:.2f}\n")
    report.write(f"Median: {median_age:.2f}\n")
    report.write(f"Standard Deviation: {std_age:.2f}\n")
    report.write("Top 5 Cities:\n")

    for city, count in top_cities:
        report.write(f"{city} - {count}\n")

    report.close()


main()
