import re
from datetime import datetime
from typing import List, Optional


class DateTimeExtractor:
    """
    Extract datetime values from text.

    Supported formats:
    - YYYY-MM-DD
    - YYYY-MM-DD HH:MM
    - YYYY-MM-DD HH:MM:SS
    - MM/DD/YYYY
    - MM/DD/YYYY HH:MM
    - DD/MM/YYYY
    - DD/MM/YYYY HH:MM
    """

    DEFAULT_FORMATS = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d",
        "%m/%d/%Y %H:%M",
        "%m/%d/%Y",
        "%d/%m/%Y %H:%M",
        "%d/%m/%Y",
    ]

    DATETIME_PATTERN = re.compile(
        r"\b\d{4}-\d{2}-\d{2}(?: \d{2}:\d{2}(?::\d{2})?)?\b"
        r"|\b\d{1,2}/\d{1,2}/\d{4}(?: \d{2}:\d{2})?\b"
    )

    def __init__(self, formats: Optional[List[str]] = None):
        self.formats = formats or self.DEFAULT_FORMATS

    def extract(self, text: str) -> List[datetime]:
        """
        Extract all datetime values from a string.

        Args:
            text: Input text to search.

        Returns:
            A list of datetime objects.
        """
        results = []

        for match in self.DATETIME_PATTERN.findall(text):
            parsed = self._parse(match)

            if parsed is not None:
                results.append(parsed)

        return results

    def extract_first(self, text: str) -> Optional[datetime]:
        """
        Extract the first datetime found in a string.

        Args:
            text: Input text to search.

        Returns:
            A datetime object or None if no match is found.
        """
        matches = self.extract(text)
        return matches[0] if matches else None

    def _parse(self, value: str) -> Optional[datetime]:
        """Attempt to parse a date string using configured formats."""
        for fmt in self.formats:
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                continue

        return None
