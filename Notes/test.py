import os
import subprocess
from datetime import datetime, timedelta

# Target directory
target_dir = "/Users/dikshanta/Documents/Data-visualization-Machine-Learning/Notes"
os.makedirs(target_dir, exist_ok=True)

# Base date: Feb 7, 2025
base_date = datetime(2025, 2, 7)

# File topics and basic plain text content (no markdown)
file_contents = [
    ("numpy.md", "NumPy basics including array creation, operations, slicing, reshaping, broadcasting, aggregation, and random module."),
    ("pandas.md", "Pandas basics including Series/DataFrame, file I/O, indexing, filtering, missing data, grouping, and merging."),
    ("seaborn.md", "Seaborn for data visualization with histograms, scatter plots, boxplots, heatmaps, and customization."),
    ("matplotlib.md", "Matplotlib for plotting: line plots, scatter plots, bar charts, subplots, and customizations."),
    ("data_cleaning.md", "Data cleaning techniques: missing values, duplicates, data types, and outlier handling."),
    ("data_transformation.md", "Transforming data: scaling, normalization, encoding, and binning."),
    ("eda.md", "Exploratory Data Analysis: descriptive stats, value counts, visual inspection, and correlations."),
    ("feature_engineering.md", "Feature Engineering: creating new features, extracting date parts, and polynomial features."),
    ("data_integration.md", "Data Integration: merging multiple datasets, handling keys, resolving mismatches."),
    ("data_export.md", "Data Exporting: saving cleaned data to CSV, Excel, and databases."),
]

# Write files and commit them with dated Git commits
for i, (filename, content) in enumerate(file_contents):
    file_path = os.path.join(target_dir, filename)
    
    # Write the file
    with open(file_path, "w") as f:
        f.write(content)
    
    # Commit date
    commit_date = base_date + timedelta(days=i)
    date_str = commit_date.strftime("%Y-%m-%dT12:00:00")

    # Git add + commit with author/committer date
    subprocess.run(["git", "-C", target_dir, "add", filename])
    subprocess.run(
        ["git", "-C", target_dir, "commit", "-m", f"Add {filename}", filename],
        env={**os.environ, "GIT_AUTHOR_DATE": date_str, "GIT_COMMITTER_DATE": date_str}
    )

print("✅ Files created and committed successfully.")
