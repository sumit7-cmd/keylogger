from logger.formatting import format_key


class FakeCharacterKey:
    char = "x"


class FakeSpecialKey:
    char = None

    def __str__(self):
        return "Key.space"


def test_formats_character_key():
    assert format_key(FakeCharacterKey()) == "x"


def test_formats_special_key():
    assert format_key(FakeSpecialKey()) == "[Key.space]"
