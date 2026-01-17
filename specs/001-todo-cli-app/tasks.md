---
description: "Task list for In-Memory Todo CLI Application implementation"
---

# Tasks: In-Memory Todo CLI Application (Phase I)

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included as specified in the feature requirements for educational purposes.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in root directory
- [X] T002 Initialize Python 3.13+ project with uv and pyproject.toml
- [X] T003 [P] Create src/todo_app/__init__.py file
- [X] T004 [P] Create src/todo_app/models/ directory
- [X] T005 [P] Create src/todo_app/services/ directory
- [X] T006 [P] Create src/todo_app/cli/ directory
- [X] T007 [P] Create src/todo_app/utils/ directory
- [X] T008 [P] Create tests/ directory structure

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T009 Create base TodoTask model in src/todo_app/models/task.py
- [X] T010 Create TaskCollection model in src/todo_app/models/task.py
- [X] T011 Create validators utility in src/todo_app/utils/validators.py
- [X] T012 Setup pytest configuration in pyproject.toml and create tests/conftest.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Todo Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo tasks to the application with unique identifiers

**Independent Test**: Can be fully tested by adding a task via the CLI and verifying it appears in the task list with a unique ID and "incomplete" status.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T013 [P] [US1] Unit test for TodoTask model in tests/unit/models/test_task.py
- [X] T014 [P] [US1] Unit test for TaskCollection add_task operation in tests/unit/services/test_task_manager.py
- [X] T015 [P] [US1] Integration test for add command in tests/integration/test_cli.py

### Implementation for User Story 1

- [X] T016 [P] [US1] Implement TaskManager service in src/todo_app/services/task_manager.py
- [X] T017 [US1] Implement add_task functionality in TaskManager service
- [X] T018 [US1] Create CLI argument parser in src/todo_app/cli/main.py
- [X] T019 [US1] Implement add command in CLI handler
- [X] T020 [US1] Add validation for task description in validators.py
- [X] T021 [US1] Add error handling for empty descriptions

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Todo Tasks (Priority: P1)

**Goal**: Enable users to view all their todo tasks in a clear format showing their status (complete/incomplete)

**Independent Test**: Can be fully tested by adding some tasks and then viewing them to confirm they display correctly with their status indicators.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T022 [P] [US2] Unit test for get_all_tasks operation in tests/unit/services/test_task_manager.py
- [X] T023 [P] [US2] Integration test for view command in tests/integration/test_cli.py

### Implementation for User Story 2

- [X] T024 [US2] Implement get_all_tasks functionality in TaskManager service
- [X] T025 [US2] Implement get_task functionality in TaskManager service
- [X] T026 [US2] Implement view command in CLI handler
- [X] T027 [US2] Create task display formatter in src/todo_app/utils/formatters.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update and Complete Todo Tasks (Priority: P2)

**Goal**: Enable users to update their todo tasks and mark them as complete when finished

**Independent Test**: Can be fully tested by adding tasks, updating their content, and marking them complete to verify status changes persist.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T028 [P] [US3] Unit test for update_task operation in tests/unit/services/test_task_manager.py
- [X] T029 [P] [US3] Unit test for toggle_completion operation in tests/unit/services/test_task_manager.py
- [X] T030 [P] [US3] Integration test for update and complete commands in tests/integration/test_cli.py

### Implementation for User Story 3

- [X] T031 [US3] Implement update_task functionality in TaskManager service
- [X] T032 [US3] Implement toggle_completion functionality in TaskManager service
- [X] T033 [US3] Implement update command in CLI handler
- [X] T034 [US3] Implement complete command in CLI handler
- [X] T035 [US3] Add validation for task ID existence

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Unwanted Todo Tasks (Priority: P2)

**Goal**: Enable users to delete tasks they no longer need to keep their todo list clean and organized

**Independent Test**: Can be fully tested by adding tasks and then deleting specific ones to verify they no longer appear in the list.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T036 [P] [US4] Unit test for delete_task operation in tests/unit/services/test_task_manager.py
- [X] T037 [P] [US4] Integration test for delete command in tests/integration/test_cli.py

### Implementation for User Story 4

- [X] T038 [US4] Implement delete_task functionality in TaskManager service
- [X] T039 [US4] Implement delete command in CLI handler
- [X] T040 [US4] Add validation for task ID existence in delete operations

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Interactive CLI Experience (Priority: P3)

**Goal**: Provide a clean, intuitive command-line interface that guides users through operations

**Independent Test**: Can be fully tested by verifying the CLI provides clear prompts, helpful error messages, and intuitive command structure.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T041 [P] [US5] Unit test for error handling in tests/unit/services/test_task_manager.py
- [X] T042 [P] [US5] Integration test for help command in tests/integration/test_cli.py
- [X] T043 [P] [US5] Integration test for error scenarios in tests/integration/test_cli.py

### Implementation for User Story 5

- [X] T044 [US5] Implement help command in CLI handler
- [X] T045 [US5] Improve error messages for all CLI operations
- [X] T046 [US5] Add comprehensive error handling throughout CLI
- [X] T047 [US5] Implement graceful error recovery

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T048 [P] Documentation updates in README.md
- [X] T049 Code cleanup and refactoring across all modules
- [X] T050 [P] Additional unit tests in tests/unit/
- [X] T051 Run quickstart.md validation
- [X] T052 Final integration testing of all features

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May use components from other stories but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for TodoTask model in tests/unit/models/test_task.py"
Task: "Unit test for TaskCollection add_task operation in tests/unit/services/test_task_manager.py"
Task: "Integration test for add command in tests/integration/test_cli.py"

# Launch all implementation for User Story 1 together:
Task: "Implement TaskManager service in src/todo_app/services/task_manager.py"
Task: "Create CLI argument parser in src/todo_app/cli/main.py"
Task: "Create validators utility in src/todo_app/utils/validators.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence