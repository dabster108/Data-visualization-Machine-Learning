import subprocess
from help import commits_schedule  # import schedule from help.py

file_name = "topics.txt"

# Loop through dates
for date, topics in commits_schedule.items():
    for i, topic in enumerate(topics):
        # Append topic to the file
        with open(file_name, "a") as f:
            f.write(topic + "\n")
        
        # Set commit time (hour/minute just for variety)
        commit_time = f"{date} 12:{i:02d}:00"
        
        # Stage the file
        subprocess.run(["git", "add", file_name])
        
        # Commit with custom date
        subprocess.run([
            "git", "commit",
            "--date", commit_time,
            "-m", f"Commit {i+1} on {date}: {topic}"
        ])

print("All commits generated!")
