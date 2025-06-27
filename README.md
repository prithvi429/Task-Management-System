# Task Management System

A simple Python-based Task Management System that allows users to create, manage, and track tasks. The system uses custom data structures (Queue, Stack, Graph) to demonstrate core computer science concepts in a practical application.

## Features

- Add and manage users
- Create and queue tasks
- Mark tasks as complete
- Track completed tasks using a stack (history)
- Modular code structure for easy extension

## Project Structure

```
Task-Management-System/
│
├── model/
│   ├── Graph.py
│   ├── Queue.py
│   ├── Stack.py
│   ├── Task.py
│   └── main.py
│
├── Service/
│   ├── Task_service.py
│   └── User_service.py
│
└── README.md
```

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Task-Management-System
   ```

2. **Ensure Python 3.x is installed.**

3. **Run the main program:**
   ```bash
   python -m model.main
   ```

## Usage

- The system allows you to add users and tasks.
- Tasks are enqueued and can be completed in order.
- Completed tasks are stored in a stack for history tracking.
- The main script demonstrates creating users, adding tasks, completing them, and printing completed task titles.

## Example

```
Task_service module is running!
<Task object at ...>
<Task object at ...>
<Task object at ...>
None
Do a project
Teach Data Science basice
Teach Data struchere basice
```

## Use Cases

- **Educational Tool:** Demonstrates data structures (Queue, Stack, Graph) in a real-world scenario for students learning Python and algorithms.
- **Personal Task Management:** Can be extended for personal use to manage daily tasks and track completion history.
- **Team Task Tracking:** With further development, can be adapted for small teams to assign and monitor tasks.
- **Prototype for Workflow Automation:** Serves as a base for building more complex workflow or project management tools.

## Extending the System

- Add persistence (database or file storage)
- Implement user authentication
- Add deadlines and priorities to tasks
- Integrate with web frameworks for a web interface

---

*Developed as a learning project to demonstrate core programming and data structure concepts in Python.*