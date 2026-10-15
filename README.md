# Use pre-existing components (ICTPRG439)

---

## Overview

This activity requires you to:

- Investigate and incorporate reusable components into an existing application.
- Debug and improve the provided **Task Management CLI App**.
- Use **GitHub Issues** for tracking bugs and improvements.
- Write unit tests to verify issues and fixes.
- Open and update **Pull Requests (PRs)**.
- Update and maintain project documentation.
- Demonstrate effective use of Git and GitHub workflows.

---

## Workflow

### 1. Familiarise Yourself with the Project

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd pin_civ_assessment_ipos_portfolio_2
   ```

2. **Use a Virtual Environment**

   Activate a virtual environment in Python. The command varies depending on your operating system and terminal.

### 2. Create a Virtual Environment

Create the virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

**Windows (Command Prompt):**

```cmd
.venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

**Windows (Git Bash):**

```bash
source .venv/Scripts/activate
```

Install the project:

```bash
python -m pip install -e .
```

Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Run the application:

```bash
python main.py
```

Explore the current functionality by adding, deleting, and listing tasks.

Review the `onboarding.md`, `README.md`, and inline comments.

---

### 3. Debugging and Identifying Enhancement Issues

Use debugging tools such as breakpoints, print statements, and IDE tools to identify **two issues** or areas where reusable components can improve the application.

#### Suggested Components

1. `click` — Improve CLI usability and interactivity.
2. `python-dateutil` — Ensure robust date validation.
3. `rich` — Format task outputs with tables and colours.
4. `colorama` — Add terminal colours for task statuses.
5. `tabulate` — Format task lists as clean tables.
6. `SQLAlchemy` — Use SQLite for structured storage.
7. `loguru` — Add detailed logging for debugging.
8. `mock` — Mock file handling and inputs for testing.
9. `schedule` — Automate task reminders.

#### Example Component Uses

- **User-Friendly CLI:** Combine `click` and `rich` for improved commands and task displays.
- **Database-Driven Storage:** Use `SQLAlchemy` for structured task management.
- **Robust Testing:** Use `mock` to test operations without modifying real data.
- **Automated Reminders:** Use `schedule` to remind users about upcoming tasks.

Record your findings and raise two GitHub Issues.

---

### 4. Raise Two GitHub Issues

1. Open the repository's **Issues** tab.
2. Create a separate Issue for each improvement using the provided template.
3. Include:
   - A clear title.
   - A description of the problem.
   - Reasoning for the enhancement and selected component.

---

### 5. Create Local and Remote Branches

Create a branch for each Issue:

```bash
git checkout -b issue-<issue_number>
```

Push the branch:

```bash
git push -u origin issue-<issue_number>
```

---

### 6. Add and Test Reusable Components

Select appropriate Python libraries and write unit tests using `unittest`, `mock`, and `patch`.

Tests should cover relevant scenarios such as:

- Invalid dates.
- Duplicate task prevention.
- New CLI behaviour.

Run the tests before implementing the fix to confirm that the new tests fail:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

### 7. Fix the Code

1. Integrate the selected reusable components.
2. Address the issues on their respective branches.
3. Rerun the unit tests:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

Confirm the tests pass.

---

### 8. Update the Documentation

1. Add or update inline comments explaining changes.
2. Update the `README.md` with:
   - New dependencies.
   - Instructions for running and testing the application.
3. Update `requirements-dev.txt` with any new libraries.

To export installed dependencies when required:

```bash
python -m pip freeze > requirements.txt
```

---

### 9. Run Workflows Locally

Before pushing changes, run Flake8 to check code quality.

```bash
python -m flake8 src tests
```

Optional detailed report:

```bash
python -m flake8 . --statistics --show-source
```

Fix all reported errors before submitting a Pull Request.

Common errors include:

- Unused imports or variables.
- Lines exceeding the configured length.
- Functions that are too complex.
- Debugging print statements.

---

### 10. Submit a Pull Request

Use the provided Pull Request template.

1. Open a Pull Request for each Issue against `main`.
2. Include:
   - A summary of changes.
   - The related Issue number using `Fixes #<issue_number>`.
   - Evidence of passing tests.

Push any updates:

```bash
git add .
git commit -m "feat: implement issue enhancement"
git push
```

---

### 11. Seek Pull Request Approval

**Do not merge the Pull Request before receiving lecturer approval.**

1. Request your lecturer as a reviewer.
2. Address any feedback provided.
3. Wait for approval before merging.

---

### 12. Close the Issue

When the Pull Request is merged, GitHub automatically closes the linked Issue if the PR description includes `Fixes #<issue_number>`.

---

### 13. Complete Reflection Questions

Complete the **KBA Testing Documentation & Reusability** assessment.

Reflect on:

- Which reusable components were selected and why.
- How the components improved the project.
- Challenges faced while debugging and integrating the components.

---

## Assessment Criteria

1. **Identification:** Appropriate issues and reusable components.
2. **GitHub Workflow:** Proper Issues, branches, and Pull Requests.
3. **Code Quality:** Correct fixes and reusable component integration.
4. **Testing:** Unit tests demonstrating failures and successful fixes.
5. **Documentation:** Updated comments, README, and dependencies.
6. **PR Workflow:** Evidence of testing and lecturer approval.
7. **Reflection:** Thoughtful responses to knowledge questions.

---

# Task Management CLI — Project Documentation

## Project Overview

The Task Management CLI is a Python application that allows users to add, delete, and list tasks.

Each task contains a title, description, due date, and status. Task information is stored locally in a binary file using Python's `pickle` module.

## Features

- Add tasks with a title, description, and due date.
- Validate due dates using the `DD-MM-YYYY` format.
- Prevent duplicate task titles.
- Delete existing tasks.
- List tasks in a formatted table.
- Display task statuses using colours.
- Save and load tasks from a binary file.

## Reusable Components

### Rich — Issue #1

The `rich` Python library was integrated to improve the readability of task information in the command-line interface.

Previously, tasks were displayed as plain text separated by pipe characters (`|`).

The updated `list_tasks()` function in `src/task_manager.py` uses Rich to display a table containing:

- Title
- Description
- Due Date
- Status

Pending tasks are displayed in yellow, while completed tasks are displayed in green.

The function also supports filtering by status and displays a message when no tasks are found.

## Installation

Clone the repository:

```bash
git clone https://github.com/samroberts-dev/civ-ipos-portfolio-part2-S2-2026.git
cd civ-ipos-portfolio-part2-S2-2026
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

**Windows (Git Bash):**

```bash
source .venv/Scripts/activate
```

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the project and development dependencies:

```bash
python -m pip install -e .
python -m pip install -r requirements-dev.txt
```

## Running the Application

Run the application:

```bash
python main.py
```

The application provides a menu for adding, deleting, and listing tasks.

## Unit Testing

Unit tests use Python's built-in `unittest` framework and `unittest.mock`.

Run all tests:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

The Rich functionality is tested in `tests/test_rich_display.py`.

The tests verify:

- Table headers are displayed correctly.
- Table borders are present.
- Task information is displayed accurately.
- Empty task lists are handled correctly.
- Status filtering continues to work.

During development, two new tests initially failed because Rich formatting had not been implemented.

After integrating Rich, all 11 unit tests passed.

## Code Quality

Flake8 is used to check Python code quality.

Run:

```bash
python -m flake8 src tests
```

Resolve any reported issues before submitting a Pull Request.

## Dependencies

### Runtime

- `rich` — Formats task information into terminal tables and displays coloured statuses.

### Development

- `flake8` — Checks Python code quality.
- `unittest` — Python's built-in unit testing framework.
- `unittest.mock` — Python's built-in mocking utilities.

The `unittest` modules are included with Python and do not require separate installation.

## GitHub Issues

- **Issue #1:** Improve Task List Display Using Rich — implemented on `issue-1`.
- **Issue #2:** Implement Task Operation Logging Using Loguru — planned.
