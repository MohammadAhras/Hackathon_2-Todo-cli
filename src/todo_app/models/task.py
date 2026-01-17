"""
Models for the Todo CLI Application.

Contains the TodoTask data model and TaskCollection for in-memory storage.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TodoTask:
    """
    Represents a single todo item with a unique identifier, description text,
    and completion status (boolean).
    """
    id: int
    description: str
    completed: bool = False

    def __post_init__(self):
        """Validate the task after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"Task ID must be a positive integer, got {self.id}")

        if not isinstance(self.description, str) or not self.description.strip():
            raise ValueError(f"Task description must be a non-empty string, got {self.description}")

        if not isinstance(self.completed, bool):
            raise ValueError(f"Task completion status must be boolean, got {self.completed}")


class TaskCollection:
    """
    In-memory data structure that holds all todo tasks and provides operations
    for adding, retrieving, updating, and deleting tasks.
    """

    def __init__(self):
        self._tasks = {}  # Dictionary mapping task ID to TodoTask
        self._next_id = 1  # Track the next available ID

    def add_task(self, description: str) -> int:
        """
        Creates new task with unique ID, returns the ID.

        Args:
            description: The task description

        Returns:
            The unique ID of the created task
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")

        task_id = self._next_id
        self._next_id += 1

        task = TodoTask(id=task_id, description=description.strip(), completed=False)
        self._tasks[task_id] = task

        return task_id

    def get_task(self, task_id: int) -> Optional[TodoTask]:
        """
        Retrieves task by ID or None if not found.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> List[TodoTask]:
        """
        Returns all tasks in collection.

        Returns:
            List of all tasks in the collection
        """
        return list(self._tasks.values())

    def update_task(self, task_id: int, description: str) -> bool:
        """
        Updates task description, returns success status.

        Args:
            task_id: The ID of the task to update
            description: The new description for the task

        Returns:
            True if the task was updated successfully, False otherwise
        """
        if task_id not in self._tasks:
            return False

        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")

        self._tasks[task_id].description = description.strip()
        return True

    def toggle_completion(self, task_id: int) -> bool:
        """
        Toggles completion status, returns success status.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            True if the task status was toggled successfully, False otherwise
        """
        if task_id not in self._tasks:
            return False

        task = self._tasks[task_id]
        task.completed = not task.completed
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Removes task from collection, returns success status.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted successfully, False otherwise
        """
        if task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        return True