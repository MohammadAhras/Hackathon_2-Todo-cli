"""
Main CLI entry point for the Todo CLI Application.
"""

import argparse
import sys
import os
from typing import List

# Add the src directory to the path so imports work correctly when run directly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    from src.todo_app.services.task_manager import TaskManager
    from src.todo_app.utils.validators import validate_task_description, validate_task_id
    from src.todo_app.utils.formatters import format_task_list
except ImportError:
    # Fallback for when the package is installed
    from ..services.task_manager import TaskManager
    from ..utils.validators import validate_task_description, validate_task_id
    from ..utils.formatters import format_task_list


class TodoCLI:
    """
    Command Line Interface handler for the Todo application.
    """

    def __init__(self):
        self.manager = TaskManager()

    def run(self, args: List[str] = None):
        """
        Runs the CLI application with the given arguments.

        Args:
            args: Command line arguments (defaults to sys.argv[1:])
        """
        if args is None:
            args = sys.argv[1:]

        if not args:
            self.interactive_mode()
        else:
            command = args[0].lower()

            if command == "add":
                self.handle_add(args[1:])
            elif command == "view":
                self.handle_view()
            elif command == "update":
                self.handle_update(args[1:])
            elif command == "complete":
                self.handle_complete(args[1:])
            elif command == "delete":
                self.handle_delete(args[1:])
            elif command == "help":
                self.show_help()
            else:
                print(f"Error: Unknown command '{command}'", file=sys.stderr)
                self.show_help()
                sys.exit(1)

    def interactive_mode(self):
        """
        Runs the CLI application in interactive mode with a menu.
        """
        while True:
            print("\n--- Todo Application ---")
            print("1. Add Task")
            print("2. View All Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Mark Task Complete")
            print("6. Mark Task Incomplete")
            print("7. Exit")
            print("-----------------------")

            try:
                choice = int(input("Select an option (1-7): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 7.")
                continue

            if choice == 1:
                self.interactive_add()
            elif choice == 2:
                self.handle_view()
            elif choice == 3:
                self.interactive_update()
            elif choice == 4:
                self.interactive_delete()
            elif choice == 5:
                self.interactive_mark_complete()
            elif choice == 6:
                self.interactive_mark_incomplete()
            elif choice == 7:
                print("Exiting Todo Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1-7.")

    def interactive_add(self):
        """
        Interactive version of the add command.
        """
        title = input("Enter task title: ").strip()
        if not title:
            print("Task title cannot be empty!")
            return

        description = input("Enter task description: ").strip()
        # Combine title and description for the task
        combined_desc = f"{title}: {description}" if description else title

        try:
            task_id = self.manager.add_task(combined_desc)
            print(f"Task added with ID: {task_id}")
        except ValueError as e:
            print(f"Error: {str(e)}", file=sys.stderr)

    def interactive_update(self):
        """
        Interactive version of the update command.
        """
        if not self.manager.get_all_tasks():
            print("No tasks to update.")
            return

        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        task = self.manager.get_task(task_id)
        if not task:
            print(f"No task found with ID {task_id}.")
            return

        # Show current task details
        print(f"Current task: {task.description}")

        new_description = input(f"Enter new description (current: {task.description}): ").strip()
        if new_description:
            success = self.manager.update_task(task_id, new_description)
            if success:
                print("Task updated successfully.")
            else:
                print(f"Failed to update task {task_id}.")
        else:
            print("No changes made.")

    def interactive_delete(self):
        """
        Interactive version of the delete command.
        """
        if not self.manager.get_all_tasks():
            print("No tasks to delete.")
            return

        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        task = self.manager.get_task(task_id)
        if not task:
            print(f"No task found with ID {task_id}.")
            return

        success = self.manager.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Failed to delete task {task_id}.")

    def interactive_mark_complete(self):
        """
        Interactive version of the complete command.
        """
        if not self.manager.get_all_tasks():
            print("No tasks available.")
            return

        try:
            task_id = int(input("Enter task ID to mark complete: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        task = self.manager.get_task(task_id)
        if not task:
            print(f"No task found with ID {task_id}.")
            return

        success = self.manager.toggle_completion(task_id)
        if success:
            print("Task marked as complete.")
        else:
            print(f"Failed to mark task {task_id} as complete.")

    def interactive_mark_incomplete(self):
        """
        Interactive version of the incomplete command.
        """
        if not self.manager.get_all_tasks():
            print("No tasks available.")
            return

        try:
            task_id = int(input("Enter task ID to mark incomplete: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        task = self.manager.get_task(task_id)
        if not task:
            print(f"No task found with ID {task_id}.")
            return

        # If the task is currently completed, toggle it to make it incomplete
        if task.completed:
            success = self.manager.toggle_completion(task_id)
            if success:
                print("Task marked as incomplete.")
            else:
                print(f"Failed to mark task {task_id} as incomplete.")
        else:
            print("Task is already marked as incomplete.")

    def handle_add(self, args: List[str]):
        """
        Handles the add command.

        Args:
            args: Arguments for the add command
        """
        if len(args) < 1:
            print("Error: Missing task description for add command", file=sys.stderr)
            print("Usage: todo add \"task description\"")
            sys.exit(2)

        description = " ".join(args)
        if not validate_task_description(description):
            print("Error: Task description cannot be empty", file=sys.stderr)
            sys.exit(1)

        try:
            task_id = self.manager.add_task(description)
            print(f"Added task with ID: {task_id}")
        except ValueError as e:
            print(f"Error: {str(e)}", file=sys.stderr)
            sys.exit(1)

    def handle_view(self):
        """
        Handles the view command.
        """
        tasks = self.manager.get_all_tasks()
        formatted_output = format_task_list(tasks)
        print(formatted_output)

    def handle_update(self, args: List[str]):
        """
        Handles the update command.

        Args:
            args: Arguments for the update command
        """
        if len(args) < 2:
            print("Error: Missing task ID or description for update command", file=sys.stderr)
            print("Usage: todo update <id> \"new description\"")
            sys.exit(2)

        try:
            task_id_str = args[0]
            task_id = int(task_id_str)
        except ValueError:
            print(f"Error: Task ID must be an integer, got '{task_id_str}'", file=sys.stderr)
            sys.exit(1)

        if not validate_task_id(task_id):
            print(f"Error: Task ID must be a positive integer, got {task_id}", file=sys.stderr)
            sys.exit(1)

        description = " ".join(args[1:])
        if not validate_task_description(description):
            print("Error: Task description cannot be empty", file=sys.stderr)
            sys.exit(1)

        success = self.manager.update_task(task_id, description)
        if success:
            print(f"Updated task {task_id}")
        else:
            print(f"Error: Task with ID {task_id} not found", file=sys.stderr)
            sys.exit(1)

    def handle_complete(self, args: List[str]):
        """
        Handles the complete command.

        Args:
            args: Arguments for the complete command
        """
        if len(args) < 1:
            print("Error: Missing task ID for complete command", file=sys.stderr)
            print("Usage: todo complete <id>")
            sys.exit(2)

        try:
            task_id_str = args[0]
            task_id = int(task_id_str)
        except ValueError:
            print(f"Error: Task ID must be an integer, got '{task_id_str}'", file=sys.stderr)
            sys.exit(1)

        if not validate_task_id(task_id):
            print(f"Error: Task ID must be a positive integer, got {task_id}", file=sys.stderr)
            sys.exit(1)

        success = self.manager.toggle_completion(task_id)
        if success:
            task = self.manager.get_task(task_id)
            if task and task.completed:
                print(f"Completed task {task_id}")
            else:
                print(f"Uncompleted task {task_id}")
        else:
            print(f"Error: Task with ID {task_id} not found", file=sys.stderr)
            sys.exit(1)

    def handle_delete(self, args: List[str]):
        """
        Handles the delete command.

        Args:
            args: Arguments for the delete command
        """
        if len(args) < 1:
            print("Error: Missing task ID for delete command", file=sys.stderr)
            print("Usage: todo delete <id>")
            sys.exit(2)

        try:
            task_id_str = args[0]
            task_id = int(task_id_str)
        except ValueError:
            print(f"Error: Task ID must be an integer, got '{task_id_str}'", file=sys.stderr)
            sys.exit(1)

        if not validate_task_id(task_id):
            print(f"Error: Task ID must be a positive integer, got {task_id}", file=sys.stderr)
            sys.exit(1)

        success = self.manager.delete_task(task_id)
        if success:
            print(f"Deleted task {task_id}")
        else:
            print(f"Error: Task with ID {task_id} not found", file=sys.stderr)
            sys.exit(1)

    def show_help(self):
        """
        Shows help information about available commands.
        """
        print("Todo CLI Application")
        print("Usage: todo [command] [arguments]")
        print()
        print("Commands:")
        print("  add \"task description\"    - Add a new task")
        print("  view                     - View all tasks with status")
        print("  update <id> \"desc\"       - Update task description")
        print("  complete <id>            - Mark task as complete")
        print("  delete <id>              - Delete a task")
        print("  help                     - Show this help")


def main():
    """
    Main entry point for the application.
    """
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()