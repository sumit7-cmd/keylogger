from pynput import keyboard

from logger.formatting import format_key


def test_formats_character_key():
    assert format_key(keyboard.KeyCode.from_char("x")) == "x"


def test_formats_special_key():
    assert format_key(keyboard.Key.space) == "[Key.space]"
