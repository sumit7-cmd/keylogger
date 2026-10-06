import os
from pathlib import Path

LOG_FILE = Path(os.getenv("KEYLOGGER_LOG_FILE", "logs/keystrokes.log"))
