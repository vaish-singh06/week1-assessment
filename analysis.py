file = open("data.csv", "r")
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines]

header = lines[0].split(",")
rows = lines[1:]
total_records = len(rows)

print(header)
print(rows[:2])
print(total_records)
