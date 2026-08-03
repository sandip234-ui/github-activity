from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent
ACTIVITY_FILE = REPO / "activity.txt"

india = ZoneInfo("Asia/Kolkata")
now = datetime.now(timezone.utc).astimezone(india)

with ACTIVITY_FILE.open("a") as file:
    file.write(
        f"\nActivity recorded: {now:%Y-%m-%d %H:%M:%S} IST"
    )

print(f"Activity recorded successfully: {now:%Y-%m-%d %H:%M:%S} IST")
