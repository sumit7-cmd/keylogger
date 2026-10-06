from logger.storage import EventStore


def test_event_store_writes_timestamped_event(tmp_path):
    path = tmp_path / "logs" / "events.log"
    EventStore(path).append("a")
    content = path.read_text(encoding="utf-8")
    assert " | a" in content
    assert "T" in content
