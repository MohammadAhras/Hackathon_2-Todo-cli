# Data Model: In-Memory Todo CLI Application

## Todo Task Entity

**Name**: TodoTask
**Fields**:
- `id`: Integer (auto-generated unique identifier, positive integers starting from 1)
- `description`: String (required, non-empty text describing the task)
- `completed`: Boolean (default False, indicates whether task is completed)

**Validation Rules**:
- `id` must be a positive integer
- `description` must be non-empty string (length > 0)
- `completed` must be boolean value

**State Transitions**:
- `completed` can transition from False to True (via complete operation)
- `completed` can transition from True to False (via uncomplete operation)

## Task Collection

**Name**: TaskCollection
**Purpose**: In-memory storage and management of TodoTask entities

**Operations**:
- `add_task(description: str) -> int`: Creates new task with unique ID, returns the ID
- `get_task(task_id: int) -> TodoTask | None`: Retrieves task by ID or None if not found
- `get_all_tasks() -> List[TodoTask]`: Returns all tasks in collection
- `update_task(task_id: int, description: str) -> bool`: Updates task description, returns success status
- `toggle_completion(task_id: int) -> bool`: Toggles completion status, returns success status
- `delete_task(task_id: int) -> bool`: Removes task from collection, returns success status

**Constraints**:
- All operations must be thread-safe (though not required for CLI-only application)
- Collection maintains uniqueness of task IDs
- Operations return appropriate success/failure indicators