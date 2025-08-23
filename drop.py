import subprocess

# File containing all commits
commits_file = "commits_list.txt"

# Date range to drop (YYYY-MM-DD)
start_date = "2025-03-27"
end_date = "2025-05-14"

# Read commits
with open(commits_file, "r") as f:
    lines = f.readlines()

# Extract commit hashes and dates
commits_to_drop = []
for line in lines:
    parts = line.strip().split()
    if len(parts) < 3:
        continue
    commit_hash = parts[0]
    commit_date = parts[1]
    if start_date <= commit_date <= end_date:
        commits_to_drop.append(commit_hash)

print(f"Found {len(commits_to_drop)} commits to drop:")
for commit in commits_to_drop:
    print(commit)

# Warning: dropping commits will rewrite history
confirm = input("Proceed with dropping these commits? [y/N]: ")
if confirm.lower() != 'y':
    print("Aborted.")
    exit()

# Drop commits one by one
for commit in commits_to_drop:
    print(f"Dropping commit {commit} ...")
    subprocess.run(["git", "rebase", "--onto", commit + "^", commit, "main"])
    
print("All specified commits dropped!")
