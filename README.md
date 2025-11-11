# 🧠 Task Tracker CLI

A simple **Command Line Interface (CLI) task manager** written in **Python**, which allows you to add, update, delete, and change the status of your tasks, storing them in a local JSON file.

---

## 🌐 Project URL

Repository: [https://github.com/MikeRider27/task_tracker](https://github.com/MikeRider27/task_tracker)
Roadmap.sh Project Page:  [https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)
---

## 🚀 Features

✅ Add new tasks  
✅ Update task descriptions  
✅ Delete tasks  
✅ Mark tasks as **todo**, **in-progress**, or **done**  
✅ List tasks (all or filtered by status)  
✅ Automatic persistence in a `tasks.json` file

---

## 🧩 Requirements

- Python **3.8 or higher**
- No external libraries required (standard modules only)

---

## ⚙️ Installation

1. Clone this repository or copy the `task_cli.py` file:
   ```bash
   git clone https://github.com/MikeRider27/task_tracker.git
   cd task_tracker
   ```

2. Make sure the file has execution permissions:
   ```bash
   chmod +x task_cli.py
   ```

3. (Optional) Add the script to your PATH to use it as a global command:
   ```bash
   sudo cp task_cli.py /usr/local/bin/task-cli
   ```

   Then you can run it like this:
   ```bash
   task-cli add "My new task"
   ```

---

## 🧠 Usage

The program uses **subcommands** for different operations.

### 🟢 Add a new task
```bash
python task_cli.py add "Buy milk"
```
📤 **Output:**
```
Task added successfully (ID: 1)
```

---

### 🟡 Update a task
```bash
python task_cli.py update 1 "Buy milk and bread"
```
📤 **Output:**
```
Task 1 updated successfully
```

---

### 🔴 Delete a task
```bash
python task_cli.py delete 1
```
📤 **Output:**
```
Task 1 deleted successfully
```

---

### 🔵 Mark a task as "in progress"
```bash
python task_cli.py mark-in-progress 2
```

### 🟣 Mark a task as "done"
```bash
python task_cli.py mark-done 2
```

---

### 📋 List tasks
#### All tasks:
```bash
python task_cli.py list
```

#### Only completed tasks:
```bash
python task_cli.py list done
```

#### Only pending tasks:
```bash
python task_cli.py list todo
```

#### Only tasks in progress:
```bash
python task_cli.py list in-progress
```

📤 **Example output:**
```
ID: 2, Description: Buy milk and bread, Status: done, Created: 2025-11-11T10:23:41, Updated: 2025-11-11T10:30:10
```

---

## 📁 Project Structure

```
task-tracker-cli/
│
├── task_cli.py       # Main script
├── tasks.json        # Data file (automatically created)
└── README.md         # Documentation
```

---

## 💾 Example of `tasks.json`

```json
[
  {
    "id": 1,
    "description": "Buy milk",
    "status": "done",
    "createdAt": "2025-11-11T10:23:41.123456",
    "updatedAt": "2025-11-11T10:30:10.789012"
  }
]
```

---

## ⚠️ Notes

- If the `tasks.json` file does not exist, it will be created automatically.
- If the file is corrupted or empty, the system will reset it to an empty list.
- All data is stored in the same directory where you run the script.

---

## 🧑‍💻 Author

**Miguel Villalba**  
💻 Educational project inspired by CLI Task Tracker exercises
