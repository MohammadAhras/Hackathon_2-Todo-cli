"""
Utility functions for formatting output in the Todo CLI Application.
"""


def format_task_list(tasks):
    """
    Formats a list of tasks for display.

    Args:
        tasks: List of TodoTask objects to format

    Returns:
        Formatted string representation of the tasks
    """
    if not tasks:
        return "No tasks found."

    header = "ID\tStatus\t\tDescription"
    separator = "--\t------\t\t-------------"
    lines = [header, separator]

    for task in tasks:
        status = "✓" if task.completed else "○"
        line = f"{task.id}\t{status}\t\t{task.description}"
        lines.append(line)

    return "\n".join(lines)


def format_task(task):
    """
    Formats a single task for display.

    Args:
        task: A TodoTask object to format

    Returns:
        Formatted string representation of the task
    """
    status = "✓" if task.completed else "○"
    return f"{task.id}\t{status}\t{task.description}"