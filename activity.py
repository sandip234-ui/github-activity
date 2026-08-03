from datetime import datetime
from pathlib import Path
import subprocess

REPO = Path(__file__).resolve().parent
ACTIVITY_FILE = REPO / "activity.txt"

now = datetime.now()

with ACTIVITY_FILE.open("a") as file:
    file.write(f"\nActivity recorded: {now:%Y-%m-%d %H:%M:%S}")

subprocess.run(["git", "add", "activity.txt"], cwd=REPO, check=True)

subprocess.run(
    ["git", "commit", "-m", f"Activity update: {now:%Y-%m-%d %H:%M}"],
    cwd=REPO,
    check=True,
)

subprocess.run(
    ["git", "push", "origin", "main"],
    cwd=REPO,
    check=True,
)

print("GitHub activity updated successfully!")
