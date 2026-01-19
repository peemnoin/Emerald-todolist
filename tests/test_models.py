from models import Priority, Status, TodoItem


def test_priority_enum_values():
    assert Priority.HIGH.value == "HIGH"
    assert Priority.MID.value == "MID"
    assert Priority.LOW.value == "LOW"


def test_status_enum_values():
    assert Status.PENDING.value == "PENDING"
    assert Status.COMPLETED.value == "COMPLETED"


def test_todo_item_dataclass_equality():
    item_1 = TodoItem(
        id="1",
        title="Title",
        details="Details",
        priority=Priority.HIGH,
        status=Status.PENDING,
        owner="owner",
        created_at="2026-01-01",
        updated_at="2026-01-01",
    )
    item_2 = TodoItem(
        id="1",
        title="Title",
        details="Details",
        priority=Priority.HIGH,
        status=Status.PENDING,
        owner="owner",
        created_at="2026-01-01",
        updated_at="2026-01-01",
    )

    assert item_1 == item_2
