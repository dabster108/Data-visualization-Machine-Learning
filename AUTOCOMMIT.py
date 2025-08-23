# auto_commits.py
import subprocess
from datetime import datetime

# File to update
file_name = "helo.py"

# List of commits with their messages and dates
commits = [
    ("Extra commit March 29", "2025-03-29 12:00:00"),
    ("Extra commit April 5", "2025-04-05 12:00:00"),
    ("Extra commit April 4", "2025-04-04 12:00:00"),
    ("Extra commit April 3", "2025-04-03 12:00:00"),
    ("Extra commit April 2", "2025-04-02 12:00:00"),
    ("Extra commit April 1", "2025-04-01 12:00:00"),
    ("Extra commit March 31", "2025-03-31 12:00:00"),
    ("Extra commit March 30", "2025-03-30 12:00:00"),
]

for i, (msg, date) in enumerate(commits, 1):
    # Update the file with some content to make a new commit
    with open(file_name, "a") as f:
        f.write(f"# Commit {i}: {msg} on {date}\n")
    
    # Stage the file
    subprocess.run(["git", "add", file_name])
    
    # Commit with the specific date
    subprocess.run(["git", "commit", "-m", msg, f"--date={date}"])

print("All 4 commits created successfully!")
