from sqlmodel import SQLModel
from todo_app.models import Todo


def test_todo_model():
    todo = Todo(title="Test Todo")

    assert isinstance(todo, SQLModel)

    assert todo.title == "Test Todo"

    assert hasattr(todo, 'id')

    expected_attrs = {'id', 'title'}
    actual_attrs = set(todo.__dict__.keys()) - {'_sa_instance_state'}

    unexpected_attrs = actual_attrs - expected_attrs
    assert not unexpected_attrs, f"Unexpected attributes found: {unexpected_attrs}"

    todo_dict = todo.dict()
    expected_dict = {"id": None, "title": "Test Todo"}
    assert todo_dict == expected_dict, f"Expected {expected_dict}, but got {todo_dict}"

    todo.title = "Updated Todo"
    assert todo.title == "Updated Todo"