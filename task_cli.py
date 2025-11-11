#!/usr/bin/env python3
import json
import sys
import argparse
from datetime import datetime
from pathlib import Path

class TaskTracker:
    def __init__(self, file_path="tasks.json"):
        self.file_path = Path(file_path)
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Carga las tareas desde el archivo JSON"""
        if self.file_path.exists():
            try:
                with open(self.file_path, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, Exception):
                return []
        return []
    
    def save_tasks(self):
        """Guarda las tareas en el archivo JSON"""
        try:
            with open(self.file_path, 'w') as f:
                json.dump(self.tasks, f, indent=2)
            return True
        except Exception:
            return False
    
    def get_next_id(self):
        """Genera el próximo ID único"""
        if not self.tasks:
            return 1
        return max(task['id'] for task in self.tasks) + 1
    
    def add_task(self, description):
        """Añade una nueva tarea"""
        task = {
            'id': self.get_next_id(),
            'description': description,
            'status': 'todo',
            'createdAt': datetime.now().isoformat(),
            'updatedAt': datetime.now().isoformat()
        }
        self.tasks.append(task)
        if self.save_tasks():
            print(f"Task added successfully (ID: {task['id']})")
        else:
            print("Error: Could not save task")
    
    def update_task(self, task_id, new_description):
        """Actualiza la descripción de una tarea"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['description'] = new_description
                task['updatedAt'] = datetime.now().isoformat()
                if self.save_tasks():
                    print(f"Task {task_id} updated successfully")
                else:
                    print("Error: Could not save task")
                return
        print(f"Error: Task with ID {task_id} not found")
    
    def delete_task(self, task_id):
        """Elimina una tarea"""
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        if self.save_tasks():
            print(f"Task {task_id} deleted successfully")
        else:
            print("Error: Could not save tasks")
    
    def mark_task_status(self, task_id, status):
        """Cambia el estado de una tarea"""
        valid_statuses = ['todo', 'in-progress', 'done']
        if status not in valid_statuses:
            print(f"Error: Invalid status. Must be one of {valid_statuses}")
            return
        
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = status
                task['updatedAt'] = datetime.now().isoformat()
                if self.save_tasks():
                    print(f"Task {task_id} marked as {status}")
                else:
                    print("Error: Could not save task")
                return
        print(f"Error: Task with ID {task_id} not found")
    
    def list_tasks(self, status_filter=None):
        """Lista tareas, opcionalmente filtradas por estado"""
        if status_filter:
            filtered_tasks = [task for task in self.tasks if task['status'] == status_filter]
        else:
            filtered_tasks = self.tasks
        
        if not filtered_tasks:
            if status_filter:
                print(f"No tasks with status '{status_filter}'")
            else:
                print("No tasks found")
            return
        
        for task in filtered_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, "
                  f"Status: {task['status']}, Created: {task['createdAt']}, "
                  f"Updated: {task['updatedAt']}")

def main():
    tracker = TaskTracker()
    
    parser = argparse.ArgumentParser(description='Task Tracker CLI')
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    # Comando add
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', help='Task description')
    
    # Comando update
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('id', type=int, help='Task ID')
    update_parser.add_argument('description', help='New task description')
    
    # Comando delete
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID')
    
    # Comando mark-in-progress
    mark_ip_parser = subparsers.add_parser('mark-in-progress', help='Mark task as in progress')
    mark_ip_parser.add_argument('id', type=int, help='Task ID')
    
    # Comando mark-done
    mark_done_parser = subparsers.add_parser('mark-done', help='Mark task as done')
    mark_done_parser.add_argument('id', type=int, help='Task ID')
    
    # Comando list
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('status', nargs='?', choices=['todo', 'in-progress', 'done'], 
                           help='Filter by status')
    
    args = parser.parse_args()
    
    try:
        if args.command == 'add':
            tracker.add_task(args.description)
        elif args.command == 'update':
            tracker.update_task(args.id, args.description)
        elif args.command == 'delete':
            tracker.delete_task(args.id)
        elif args.command == 'mark-in-progress':
            tracker.mark_task_status(args.id, 'in-progress')
        elif args.command == 'mark-done':
            tracker.mark_task_status(args.id, 'done')
        elif args.command == 'list':
            tracker.list_tasks(args.status)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()