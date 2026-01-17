import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from src.todo_app.models.task import TodoTask


def test_todo_task_creation():
    """Test creating a valid TodoTask."""
    task = TodoTask(id=1, description="Test task", completed=False)
    assert task.id == 1
    assert task.description == "Test task"
    assert task.completed is False


def test_todo_task_defaults():
    """Test TodoTask default values."""
    task = TodoTask(id=1, description="Test task")
    assert task.id == 1
    assert task.description == "Test task"
    assert task.completed is False  # Should default to False


def test_todo_task_validation_id_negative():
    """Test TodoTask validation with negative ID."""
    with pytest.raises(ValueError):
        TodoTask(id=-1, description="Test task")


def test_todo_task_validation_id_zero():
    """Test TodoTask validation with zero ID."""
    with pytest.raises(ValueError):
        TodoTask(id=0, description="Test task")


def test_todo_task_validation_empty_description():
    """Test TodoTask validation with empty description."""
    with pytest.raises(ValueError):
        TodoTask(id=1, description="")


def test_todo_task_validation_none_description():
    """Test TodoTask validation with None description."""
    with pytest.raises(ValueError):
        TodoTask(id=1, description=None)


def test_todo_task_validation_whitespace_description():
    """Test TodoTask validation with whitespace-only description."""
    with pytest.raises(ValueError):
        TodoTask(id=1, description="   ")


def test_todo_task_completed_non_boolean():
    """Test TodoTask validation with non-boolean completed value."""
    with pytest.raises(ValueError):
        TodoTask(id=1, description="Test task", completed="true")