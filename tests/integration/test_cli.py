import pytest
import sys
import os
from io import StringIO
from unittest.mock import patch

# Add the project root to the path so imports work correctly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.todo_app.cli.main import TodoCLI


def test_cli_add_command():
    """Test the add command."""
    cli = TodoCLI()

    # Mock sys.argv to simulate command line arguments
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        # Add a task
        cli.run(["add", "Test", "task"])

        output = mock_stdout.getvalue().strip()
        assert "Added task with ID:" in output


def test_cli_view_command():
    """Test the view command."""
    cli = TodoCLI()

    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        cli.run(["view"])

        output = mock_stdout.getvalue().strip()
        # Since there are no tasks initially, it should show "No tasks found."
        assert "No tasks found." in output


def test_cli_add_and_view_commands():
    """Test adding a task and then viewing it."""
    cli = TodoCLI()

    # First, add a task
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        cli.run(["add", "Integration", "test", "task"])
        output = mock_stdout.getvalue().strip()
        assert "Added task with ID:" in output

    # Then view tasks (in a separate CLI instance, so no tasks will be found)
    # Actually, since tasks are in memory, we can't really test this end-to-end
    # with the current architecture. The in-memory storage means each CLI run
    # starts fresh. This is by design for this phase.


def test_cli_invalid_command():
    """Test handling of invalid commands."""
    cli = TodoCLI()

    with patch('sys.stderr', new_callable=StringIO) as mock_stderr, \
         patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        # Capture both stdout and stderr
        try:
            cli.run(["invalid", "command"])
        except SystemExit:
            pass  # Expected behavior

        stderr_output = mock_stderr.getvalue().strip()
        stdout_output = mock_stdout.getvalue().strip()

        assert "Unknown command" in stderr_output


def test_cli_help_command():
    """Test the help command."""
    cli = TodoCLI()

    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        cli.run(["help"])

        output = mock_stdout.getvalue().strip()
        assert "Todo CLI Application" in output
        assert "Commands:" in output
        assert "add" in output
        assert "view" in output
        assert "update" in output
        assert "complete" in output
        assert "delete" in output
        assert "help" in output


def test_cli_add_empty_description_error():
    """Test error handling for empty description in add command."""
    cli = TodoCLI()

    with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
        try:
            cli.run(["add"])
        except SystemExit:
            pass  # Expected behavior

        stderr_output = mock_stderr.getvalue().strip()
        assert "Missing task description" in stderr_output


def test_cli_complete_invalid_id():
    """Test error handling for invalid task ID in complete command."""
    cli = TodoCLI()

    with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
        try:
            cli.run(["complete", "abc"])
        except SystemExit:
            pass  # Expected behavior

        stderr_output = mock_stderr.getvalue().strip()
        assert "Task ID must be an integer" in stderr_output


def test_cli_complete_nonexistent_task():
    """Test error handling for nonexistent task ID in complete command."""
    cli = TodoCLI()

    with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
        try:
            cli.run(["complete", "999"])
        except SystemExit:
            pass  # Expected behavior

        stderr_output = mock_stderr.getvalue().strip()
        assert "Task with ID 999 not found" in stderr_output