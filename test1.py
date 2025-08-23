import os
import subprocess
from datetime import datetime, timedelta

# Target directory (same as before)
target_dir = "/Users/dikshanta/Documents/Data-visualization-Machine-Learning/Notes"

# Dates for commits (Feb 16, 18, 20, 22, 24, 26, 2025)
commit_dates = [
    datetime(2025, 2, 16),
    datetime(2025, 2, 18),
    datetime(2025, 2, 20),
    datetime(2025, 2, 22),
    datetime(2025, 2, 24),
    datetime(2025, 2, 26),
]

# Files to modify (same 10 files)
filenames = [
    "numpy.md",
    "pandas.md",
    "seaborn.md",
    "matplotlib.md",
    "data_cleaning.md",
    "data_transformation.md",
    "eda.md",
    "feature_engineering.md",
    "data_integration.md",
    "data_export.md",
]

for commit_date in commit_dates:
    date_str = commit_date.strftime("%Y-%m-%dT12:00:00")
    
    for filename in filenames:
        file_path = os.path.join(target_dir, filename)
        
        # Append " - new" to the file
        with open(file_path, "a") as f:
            f.write(" - new")
    
    # Stage all files for this commit
    subprocess.run(["git", "-C", target_dir, "add"] + filenames)
    
    # Commit with the specific date
    subprocess.run(
        ["git", "-C", target_dir, "commit", "-m", f"Append ' - new' on {commit_date.strftime('%b %d')}"],
        env={**os.environ, "GIT_AUTHOR_DATE": date_str, "GIT_COMMITTER_DATE": date_str}
    )

print("✅ Updated files and committed 6 times on specified dates.")
