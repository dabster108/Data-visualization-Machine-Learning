import os
import subprocess
from datetime import datetime, timedelta

# File to update
FILENAME = "help.md"

# Topics per day (make sure at least as many as days between start & end)
topics = [
    "Introduction to Tableau",
    "Connecting Tableau to Data Sources",
    "Data Cleaning in Tableau",
    "Creating Bar Charts",
    "Line Charts and Time Series",
    "Pie Charts and Tree Maps",
    "Filters and Parameters",
    "Calculated Fields",
    "Joins and Blends",
    "Dashboard Basics",
    "Interactive Dashboards",
    "Publishing to Tableau Server",
    "Storytelling with Tableau",
    "Advanced Analytics in Tableau",
    "Using R and Python with Tableau",
    "Case Study: Sales Dashboard",
    "Optimizing Performance",
    "Final Thoughts on Tableau"
]

# Date range
start_date = datetime(2024, 7, 30)
end_date = datetime(2024, 8, 16)

# Ensure file exists
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        f.write("# Help File\n\n")

# Iterate through days
current_date = start_date
idx = 0
while current_date <= end_date and idx < len(topics):
    # Append to help.md
    with open(FILENAME, "a") as f:
        f.write(f"## {current_date.strftime('%Y-%m-%d')}\n")
        f.write(f"- {topics[idx]}\n\n")

    # Stage the file
    subprocess.run(["git", "add", FILENAME])

    # Commit with specific date
    commit_msg = f"Update help.md: {topics[idx]}"
    commit_date = current_date.strftime("%Y-%m-%dT12:00:00")
    subprocess.run([
        "git", "commit",
        "--date", commit_date,
        "--author", "Your Name <your.email@example.com>",
        "-m", commit_msg
    ])

    # Next day
    current_date += timedelta(days=1)
    idx += 1

# Finally push all commits
subprocess.run(["git", "push", "origin", "main"])
## 2024-07-30
- Introduction to Tableau

## 2024-07-31
- Connecting Tableau to Data Sources

## 2024-08-01
- Data Cleaning in Tableau

## 2024-08-02
- Creating Bar Charts

## 2024-08-03
- Line Charts and Time Series

## 2024-08-04
- Pie Charts and Tree Maps

## 2024-08-05
- Filters and Parameters

## 2024-08-06
- Calculated Fields

