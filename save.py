import subprocess

# File where we will save commits
output_file = "commits_list.txt"

# Run git log and capture output
result = subprocess.run(
    ["git", "log", "--oneline", "--pretty=format:%H %ad %s", "--date=short"],
    capture_output=True,
    text=True
)

# Save output to a text file
with open(output_file, "w") as f:
    f.write(result.stdout)

print(f"Saved {len(result.stdout.splitlines())} commits to {output_file}")
