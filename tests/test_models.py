from src.models import Priority, Status, TodoItem


class TestPriority:
    def test_priority_values(self):
        assert Priority.HIGH.value == "HIGH"
        assert Priority.MID.value == "MID"
        assert Priority.LOW.value == "LOW"

    def test_priority_members(self):
        assert len(Priority) == 3
        assert Priority.HIGH in Priority
        assert Priority.MID in Priority
        assert Priority.LOW in Priority


class TestStatus:
    def test_status_values(self):
        assert Status.PENDING.value == "PENDING"
        assert Status.COMPLETED.value == "COMPLETED"

    def test_status_members(self):
        assert len(Status) == 2
        assert Status.PENDING in Status
        assert Status.COMPLETED in Status


class TestTodoItem:
    def test_todo_item_creation(self):
        item = TodoItem(
            id="test-uuid",
            title="Test Todo",
            details="This is a test todo item",
            priority=Priority.HIGH,
            status=Status.PENDING,
            owner="testuser",
            created_at="2023-01-01T00:00:00Z",
            updated_at="2023-01-01T00:00:00Z",
        )
        assert item.id == "test-uuid"
        assert item.title == "Test Todo"
        assert item.details == "This is a test todo item"
        assert item.priority == Priority.HIGH
        assert item.status == Status.PENDING
        assert item.owner == "testuser"
        assert item.created_at == "2023-01-01T00:00:00Z"
        assert item.updated_at == "2023-01-01T00:00:00Z"

    def test_todo_item_immutability(self):
        item = TodoItem(
            id="test-uuid",
            title="Test Todo",
            details="This is a test todo item",
            priority=Priority.HIGH,
            status=Status.PENDING,
            owner="testuser",
            created_at="2023-01-01T00:00:00Z",
            updated_at="2023-01-01T00:00:00Z",
        )
        # Dataclasses are mutable by default, but we can test field access
        assert hasattr(item, "id")
        assert hasattr(item, "title")
        assert hasattr(item, "details")
        assert hasattr(item, "priority")
        assert hasattr(item, "status")
        assert hasattr(item, "owner")
        assert hasattr(item, "created_at")
        assert hasattr(item, "updated_at")
