import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from src.todo_app.models.task import TaskCollection


def test_task_collection_add_task():
    """Test adding a task to the collection."""
    collection = TaskCollection()
    task_id = collection.add_task("Test task")

    assert task_id == 1
    task = collection.get_task(task_id)
    assert task is not None
    assert task.id == 1
    assert task.description == "Test task"
    assert task.completed is False


def test_task_collection_get_all_tasks():
    """Test getting all tasks from the collection."""
    collection = TaskCollection()
    collection.add_task("Task 1")
    collection.add_task("Task 2")

    tasks = collection.get_all_tasks()
    assert len(tasks) == 2

    descriptions = [task.description for task in tasks]
    assert "Task 1" in descriptions
    assert "Task 2" in descriptions


def test_task_collection_get_task_by_id():
    """Test getting a specific task by ID."""
    collection = TaskCollection()
    task_id = collection.add_task("Test task")

    task = collection.get_task(task_id)
    assert task is not None
    assert task.id == task_id
    assert task.description == "Test task"


def test_task_collection_get_nonexistent_task():
    """Test getting a task that doesn't exist."""
    collection = TaskCollection()
    task = collection.get_task(999)
    assert task is None


def test_task_collection_update_task():
    """Test updating a task description."""
    collection = TaskCollection()
    task_id = collection.add_task("Old description")

    success = collection.update_task(task_id, "New description")
    assert success is True

    task = collection.get_task(task_id)
    assert task.description == "New description"


def test_task_collection_update_nonexistent_task():
    """Test updating a task that doesn't exist."""
    collection = TaskCollection()
    success = collection.update_task(999, "New description")
    assert success is False


def test_task_collection_toggle_completion():
    """Test toggling a task's completion status."""
    collection = TaskCollection()
    task_id = collection.add_task("Test task")

    # Initially should be False
    task = collection.get_task(task_id)
    assert task.completed is False

    # Toggle to True
    success = collection.toggle_completion(task_id)
    assert success is True

    task = collection.get_task(task_id)
    assert task.completed is True

    # Toggle back to False
    success = collection.toggle_completion(task_id)
    assert success is True

    task = collection.get_task(task_id)
    assert task.completed is False


def test_task_collection_toggle_nonexistent_task():
    """Test toggling completion for a task that doesn't exist."""
    collection = TaskCollection()
    success = collection.toggle_completion(999)
    assert success is False


def test_task_collection_delete_task():
    """Test deleting a task."""
    collection = TaskCollection()
    task_id = collection.add_task("Test task")

    # Verify task exists
    assert collection.get_task(task_id) is not None

    # Delete the task
    success = collection.delete_task(task_id)
    assert success is True

    # Verify task no longer exists
    assert collection.get_task(task_id) is None


def test_task_collection_delete_nonexistent_task():
    """Test deleting a task that doesn't exist."""
    collection = TaskCollection()
    success = collection.delete_task(999)
    assert success is False


def test_task_collection_unique_ids():
    """Test that task IDs are unique."""
    collection = TaskCollection()
    id1 = collection.add_task("Task 1")
    id2 = collection.add_task("Task 2")
    id3 = collection.add_task("Task 3")

    assert id1 != id2
    assert id2 != id3
    assert id1 != id3

    # IDs should be sequential starting from 1
    assert id1 == 1
    assert id2 == 2
    assert id3 == 3


def test_task_collection_empty_description_validation():
    """Test that adding a task with empty description raises an error."""
    collection = TaskCollection()
    with pytest.raises(ValueError):
        collection.add_task("")

    with pytest.raises(ValueError):
        collection.add_task("   ")


def test_task_collection_update_empty_description_validation():
    """Test that updating a task with empty description raises an error."""
    collection = TaskCollection()
    task_id = collection.add_task("Original description")

    with pytest.raises(ValueError):
        collection.update_task(task_id, "")

    with pytest.raises(ValueError):
        collection.update_task(task_id, "   ")