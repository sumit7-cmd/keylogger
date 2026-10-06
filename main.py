"""Consent-based local keyboard event logger for security research.

Use only on systems you own or have explicit permission to test.
The program is intentionally transparent: it writes locally and does not
implement persistence, stealth, exfiltration, or evasion.
"""

from datetime import datetime, timezone
from pathlib import Path

from pynput import keyboard

LOG_FILE = Path("logs/keystrokes.log")


def format_key(key: keyboard.Key | keyboard.KeyCode) -> str:
    """Return a readable representation without crashing on special keys."""
    if isinstance(key, keyboard.KeyCode) and key.char is not None:
        return key.char
    return f"[{key}]"


def write_event(key: keyboard.Key | keyboard.KeyCode) -> None:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    LOG_FILE.open("a", encoding="utf-8").write(
        f"{timestamp} | {format_key(key)}\n"
    )


def on_press(key: keyboard.Key | keyboard.KeyCode) -> None:
    write_event(key)


def main() -> None:
    print("Consent-based local keyboard logger started.")
    print(f"Local log: {LOG_FILE.resolve()}")
    print("Press Ctrl+C to stop.")

    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nLogger stopped.")


if __name__ == "__main__":
    main()
