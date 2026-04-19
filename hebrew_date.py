from pyluach import dates

HEBREW_MONTHS = {
    "ניסן": 1, "אייר": 2, "סיוון": 3, "תמוז": 4,
    "אב": 5, "אלול": 6, "תשרי": 7, "חשוון": 8,
    "כסלו": 9, "טבת": 10, "שבט": 11, "אדר": 12,
    "אדר א": 12, "אדר ב": 13,
}

HEBREW_NUMERALS = {
    "א": 1, "ב": 2, "ג": 3, "ד": 4, "ה": 5,
    "ו": 6, "ז": 7, "ח": 8, "ט": 9, "י": 10,
    "כ": 20, "ל": 30,
}

LOOKBACK_DAYS = 7


def _parse_hebrew_day(day_str: str) -> int:
    day_str = day_str.replace('"', "").replace("'", "").strip()
    return sum(HEBREW_NUMERALS.get(ch, 0) for ch in day_str)


def parse_hebrew_date(date_str: str) -> tuple[int, int]:
    """Parses a Hebrew date string like 'כ"ה ניסן' and returns (day, month)."""
    parts = date_str.strip().split()
    day = _parse_hebrew_day(parts[0])
    month_name = " ".join(parts[1:])
    month = HEBREW_MONTHS[month_name]
    return day, month


def get_today_hebrew() -> tuple[int, int]:
    """Returns today's Hebrew date as (day, month)."""
    today = dates.HebrewDate.today()
    return today.day, today.month


def get_recent_hebrew_dates() -> list[tuple[int, int]]:
    """Returns Hebrew dates for today and the last 7 days."""
    today = dates.HebrewDate.today()
    return [
        ((today - i).day, (today - i).month)
        for i in range(LOOKBACK_DAYS + 1)
    ]
