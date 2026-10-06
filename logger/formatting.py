from pynput import keyboard


def format_key(key):
    if isinstance(key, keyboard.KeyCode) and key.char is not None:
        return key.char
    return f"[{key}]"
