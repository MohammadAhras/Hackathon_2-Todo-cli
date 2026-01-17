# Quickstart Guide: In-Memory Todo CLI Application

## Prerequisites
- Python 3.13+ installed
- UV package manager installed

## Setup
1. Initialize the project:
   ```bash
   uv init
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

## Usage
1. Run the application:
   ```bash
   uv run src/todo_app/cli/main.py
   ```

2. Available commands:
   - `add "task description"` - Add a new task
   - `view` - View all tasks with status
   - `update <id> "new description"` - Update task description
   - `complete <id>` - Mark task as complete
   - `delete <id>` - Delete a task
   - `help` - Show available commands

## Example Workflow
```bash
# Add tasks
uv run src/todo_app/cli/main.py add "Learn Python"
uv run src/todo_app/cli/main.py add "Build CLI app"

# View tasks
uv run src/todo_app/cli/main.py view

# Complete a task
uv run src/todo_app/cli/main.py complete 1

# Update a task
uv run src/todo_app/cli/main.py update 2 "Build CLI app with Claude Code"

# Delete a task
uv run src/todo_app/cli/main.py delete 2
```

## Development
- Source code located in `src/todo_app/`
- Tests located in `tests/`
- Run tests with: `uv run pytest`