import subprocess

# Date range
start_date = "2025-03-27"
end_date = "2025-05-15"

# Get commit hashes in the range (oldest first)
result = subprocess.run(
    ["git", "log", "--reverse", "--since=" + start_date, "--until=" + end_date, "--pretty=format:%H"],
    capture_output=True, text=True
)

commits = result.stdout.splitlines()

print(f"Commits to remove: {len(commits)}")

# Drop each commit
for commit in commits:
    print(f"Dropping commit {commit}")
    subprocess.run(["git", "rebase", "--onto", commit + "^", commit, "--autostash"], check=True)

print("All commits in the specified date range have been removed.")
