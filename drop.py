import subprocess

# Date range
start_date = "2025-03-27"
end_date = "2025-05-14"

# Get all commits in the date range (ignore file)
result = subprocess.run(
    ["git", "log", "--pretty=format:%H", "--since="+start_date, "--until="+end_date],
    capture_output=True,
    text=True
)

commits_to_drop = result.stdout.splitlines()

print(f"Found {len(commits_to_drop)} commits to drop:")
for commit in commits_to_drop:
    print(commit)
