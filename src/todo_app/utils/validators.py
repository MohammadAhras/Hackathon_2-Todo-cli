"""
Utility functions for validation in the Todo CLI Application.
"""


def validate_task_description(description: str) -> bool:
    """
    Validates that a task description is not empty.

    Args:
        description: The task description to validate

    Returns:
        True if the description is valid, False otherwise
    """
    if not description or not description.strip():
        return False
    return True


def validate_task_id(task_id: int) -> bool:
    """
    Validates that a task ID is a positive integer.

    Args:
        task_id: The task ID to validate

    Returns:
        True if the task ID is valid, False otherwise
    """
    if not isinstance(task_id, int) or task_id <= 0:
        return False
    return True