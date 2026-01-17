"""
Task Manager service for the Todo CLI Application.

Handles business logic for task operations.
"""

from typing import List, Optional
from ..models.task import TaskCollection, TodoTask


class TaskManager:
    """
    Service class that manages task operations using TaskCollection.
    """

    def __init__(self):
        self.task_collection = TaskCollection()

    def add_task(self, description: str) -> int:
        """
        Adds a new task with the given description.

        Args:
            description: The task description

        Returns:
            The ID of the newly created task
        """
        return self.task_collection.add_task(description)

    def get_task(self, task_id: int) -> Optional[TodoTask]:
        """
        Gets a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The task if found, None otherwise
        """
        return self.task_collection.get_task(task_id)

    def get_all_tasks(self) -> List[TodoTask]:
        """
        Gets all tasks.

        Returns:
            A list of all tasks
        """
        return self.task_collection.get_all_tasks()

    def update_task(self, task_id: int, description: str) -> bool:
        """
        Updates the description of a task.

        Args:
            task_id: The ID of the task to update
            description: The new description

        Returns:
            True if the task was updated successfully, False otherwise
        """
        return self.task_collection.update_task(task_id, description)

    def toggle_completion(self, task_id: int) -> bool:
        """
        Toggles the completion status of a task.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            True if the task status was toggled successfully, False otherwise
        """
        return self.task_collection.toggle_completion(task_id)

    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted successfully, False otherwise
        """
        return self.task_collection.delete_task(task_id)