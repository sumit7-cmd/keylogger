def format_key(key) -> str:
    """Convert a keyboard event object to a readable string.

    This module deliberately does not import pynput so it can be tested
    on headless CI runners.
    """
    char = getattr(key, "char", None)
    if char is not None:
        return char
    return f"[{key}]"
