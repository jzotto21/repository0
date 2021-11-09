"""Example reading CSV files."""

from csv import DictReader

#"r" means to read file, "utf8" is like emojis, "data/weather.csv" is folder/file
file_handle = open("data/weather.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)

# A "table" can be modeled as a list of rows, where a row
# is a dictionary with the column title as the key
table: list[dict[str, str]] = []

# Add each row of data to our table
for row in csv_reader:
    table.append(row)
    
# When we're done reading / working with a file, we should close it!
file_handle.close()

# Let's calculate the average high temp
# Process the table by a specific column
high_temps: list[float] = []
for row in table:
    high_temps.append(float(row["high"]))
print(high_temps)

print("The average high temp was: ")
avg_high: float = sum(high_temps) / len(high_temps)
print(avg_high)
