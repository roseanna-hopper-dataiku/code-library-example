import re
from datetime import datetime

# Supported formats
FORMATS = [
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d",
    "%m/%d/%Y %H:%M",
    "%m/%d/%Y",
    "%d/%m/%Y %H:%M",
    "%d/%m/%Y",
]

# Regular expression to find date/time patterns
DATETIME_PATTERN = re.compile(
    r"\b\d{4}-\d{2}-\d{2}(?: \d{2}:\d{2}(?::\d{2})?)?\b"
    r"|\b\d{1,2}/\d{1,2}/\d{4}(?: \d{2}:\d{2})?\b"
)

def extract_datetimes(text):
    results = []

    for match in DATETIME_PATTERN.findall(text):
        for fmt in FORMATS:
            try:
                results.append(datetime.strptime(match, fmt))
                break
            except ValueError:
                continue

    return results


# Example usage
text = """
Meeting: 2026-06-18 14:30
Deadline: 06/20/2026
Reminder: 18/06/2026 09:15
"""

for dt in extract_datetimes(text):
    print(dt)
