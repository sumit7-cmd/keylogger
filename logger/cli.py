from pynput import keyboard

from .config import LOG_FILE
from .formatting import format_key
from .storage import EventStore


def run() -> None:
    store = EventStore(LOG_FILE)
    print("Consent-based local keyboard event logger")
    print(f"Writing only to: {LOG_FILE.resolve()}")
    print("Use Ctrl+C to stop.")

    def on_press(key):
        store.append(format_key(key))

    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nStopped safely.")
