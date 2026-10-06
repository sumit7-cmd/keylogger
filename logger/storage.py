from datetime import datetime, timezone
from pathlib import Path


class EventStore:
    def __init__(self, path: Path):
        self.path = path

    def append(self, event: str) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(f"{timestamp} | {event}\n")
