#  AramsPyProject will show some basic uses of loops under differing circumstances.
#     Created by Aram Asman
#        Creation Date: 05/09/2025
#        Last Edit: 04/15/2025

# import to use python's built in modules for csv
import csv
import matplotlib.pyplot as plt

filename = "data11Oct21.csv"
# Opens downloaded file, reads lines, then counts/prints number of lines
with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()

line_count = len(lines)

print(f"The number of lines in the file is: {line_count}")

# Prints out column headers in alphabetical order
def print_sorted_headers(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        for _ in range(2):
            next(reader)

        headers = next(reader)
        sorted_headers = sorted(headers)

        print("Column headers in alphabetical order:")
        for header in sorted_headers:
            print(header)
print_sorted_headers("data11Oct21.csv")

# Function that will take headers as arguments, and gives back a list of all the values
def get_column_values(column_name):
    # Reload the data using the correct header row
    df_corrected = pd.read_csv(file_path, header=1)

    # Check if the column exists
    if column_name not in df_corrected.columns:
        raise ValueError(f"Column '{column_name}' not found.")

    return df_corrected[column_name].dropna().tolist()

# Two functions that will give the max and min values
column_name = "Exhaust Press(Torr)"
column_values = []

with open("data11Oct21.csv", "r") as file:
    for _ in range(2):  # skip the junk
        next(file)
    reader = csv.DictReader(file)
    for row in reader:
        value = row.get(column_name)
        if value:
            column_values.append(value)

print(f"Max value in {column_name}: {max(column_values)}")
print(f"Min value in {column_name}: {min(column_values)}")

# Temperature vs time pyplot using TC1
time_col = "Run-Time(min)"
temp_col = "Chamber TC1(C)"
time_values = []
temp_values = []

with open("data11Oct21.csv", "r") as file:
    for _ in range(2):
        next(file)
    reader = csv.DictReader(file)
    for row in reader:
        t = row.get(time_col)
        temp = row.get(temp_col)
        if t and temp:
            try:
                time_values.append(float(t))
                temp_values.append(float(temp))
            except ValueError:
                continue

plt.plot(time_values, temp_values, c='maroon')
plt.xlabel("Run-Time (min)")
plt.ylabel("Chamber TC1 (°C)")
plt.title("Chamber Temperature vs Run-Time")
plt.grid(True)
plt.tight_layout()
plt.show()

# Alt temperature vs time pyplot using TC2
temp2_col = "Chamber TC2(C)"
time2_values = []
temp2_values = []

with open("data11Oct21.csv", "r") as file:
    for _ in range(2):
        next(file)
    reader = csv.DictReader(file)
    for row in reader:
        t2 = row.get(time_col)
        temp2 = row.get(temp2_col)
        if t2 and temp2:
            try:
                time2_values.append(float(t2))
                temp2_values.append(float(temp2))
            except ValueError:
                continue

plt.plot(time2_values, temp2_values, c='indigo')
plt.xlabel("Run-Time (min)")
plt.ylabel("Chamber TC2 (°C)")
plt.title("Chamber Temperature vs Run-Time")
plt.grid(True)
plt.tight_layout()
plt.show()

# Pyplot for temp vs time w/TC1, but normalized
max_temp = max(temp_values)
normalized_temp = [t / max_temp for t in temp_values]

plt.plot(time_values, normalized_temp, c='pink')
plt.xlabel("Run-Time (min)")
plt.ylabel("Normalized Temperature (0 to 1)")
plt.title("Normalized Chamber TC1 Temperature vs Time")
plt.grid(True)
plt.tight_layout()
plt.show()

# Pyplot of the correlation between TC1 vs TC2
max_temp1 = max(temp_values)
max_temp2 = max(temp2_values)

normalized_temp1 = [t / max_temp1 for t in temp_values]
normalized_temp2 = [t / max_temp2 for t in temp2_values]

plt.scatter(normalized_temp1, normalized_temp2, alpha=0.6, edgecolors='black')
plt.xlabel("Normalized TC1")
plt.ylabel("Normalized TC2")
plt.title("Correlation Plot: Normalized TC1 vs TC2")
plt.grid(True)
plt.tight_layout()
plt.show()
print("The shape formed by comparing TC1 vs TC2 is a linear function, or diagonal line, showing strong correlation between the two")

# Pyplot of difference, TC1 - TC2, for temp vs time
min_length = min(len(time_values), len(temp_values), len(temp2_values))
temp_differences = [
    abs(temp_values[i] - temp2_values[i])
    for i in range(min_length)
]
time_trimmed = time_values[:min_length]

plt.plot(time_trimmed, temp_differences, c='gold')
plt.xlabel("Run-Time (min)")
plt.ylabel("Temperature Difference (°C)")
plt.title("Difference Between TC1 and TC2 vs Time")
plt.grid(True)
plt.tight_layout()
plt.show()

# Correlation pyplot for Vaporizer heater vs Run-time
x_col = "Run-Time(min)"
y_col = "Vaporizer Heater(%)"
x_values = []
y_values = []

with open("data11Oct21.csv", "r") as file:
    for _ in range(2):
        next(file)
    reader = csv.DictReader(file)
    for row in reader:
        x_values.append(float(row[x_col]))
        y_values.append(float(row[y_col]))

x_norm = [x / max(x_values) for x in x_values]
y_norm = [y / max(y_values) for y in y_values]

plt.scatter(x_norm, y_norm, alpha=0.6, edgecolors='purple')
plt.xlabel("Normalized Run-Time (min)")
plt.ylabel("Normalized Vaporizer Heater (%)")
plt.title("Correlation Plot: Heater vs Vaporizer Temp (Step Behavior)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Not sure if this part should be just a comment or a part of the actual sequence, so why not both!

print("""I chose this plot mostly for the shape, a weird long L, aka how I felt most this semester in chem class.
My theory is that the flat lines on the far ends are the steady start up and the steady power down, the spike being 
the initial burst of power, before settling at a mostly steady power for the rest til it stops.""")
#I chose this plot mostly for the shape, a weird long L, aka how I felt most this semester in chem class.
#My theory is that the flat lines on the far ends are the steady start up and the steady power down, the spike being
#the initial burst of power, before settling at a mostly steady power for the rest til it stops.










