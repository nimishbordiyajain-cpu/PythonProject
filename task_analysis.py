import pandas as pd
import matplotlib.pyplot as plt

# Read log file
log_file = "task_log.txt"

# Lists to store extracted dates
dates = []

# Read log file line by line
with open(log_file, "r") as file:
    for line in file:
        # Extract date (YYYY-MM-DD)
        date = line.split(" ")[0]
        dates.append(date)

# Create DataFrame
df = pd.DataFrame(dates, columns=["Date"])

# Count tasks per day
task_count = df["Date"].value_counts().sort_index()

# Plot bar graph
plt.figure()
task_count.plot(kind="bar")
plt.xlabel("Date")
plt.ylabel("Number of Tasks Executed")
plt.title("Task Execution Count Per Day")
plt.show()