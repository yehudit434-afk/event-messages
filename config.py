import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).parent

EVENTS_FILE = BASE_DIR / "Events.xlsx"
ENV_FILE = BASE_DIR / ".env"
