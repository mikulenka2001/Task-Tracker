import json
import os
from datetime import datetime

def load_tasks(filename="tasks.json"):
    if not os.path.exists(filename):
        # Create an empty file
        with open(filename, "w") as f:
            json.dump([], f, indent=4)
        return []
    
    # Otherwise, load existing tasks
    with open(filename, "r") as f:
        try:
            tasks_list = json.load(f)
            return tasks_list
        except json.JSONDecodeError:
            # Handle corrupted file gracefully
            print("Error: tasks.json is corrupted. Starting fresh.")
            return []

def save_tasks(task_list, filename = "tasks.json"):
    with open(filename, "w") as f:
        json.dump(task_list, f, indent=4)

def create_task_dict(task_list, args):
    
    if not task_list:
        current_id = 1
    else:
        last_id = max(task["id"] for task in task_list)
        current_id = last_id + 1

    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task_dict = {"id": current_id,
             "description": args.description,
             "status": args.status,
             "dueDate": args.due_date,
             "notes": args.notes,
             "createdAt": time_stamp,
             "updatedAt": time_stamp}
    return(task_dict)

def print_task(task_dict):
    separator = f"\n" + "-"*37
    print(separator)
    print("id: ", task_dict["id"])
    print("description: ", task_dict["description"])
    print("status: ", task_dict["status"])
    print("dueDate: ", task_dict["dueDate"])
    print("createdAt: ", task_dict["createdAt"])
    print("updatedAt:", task_dict["updatedAt"])
    print("notes: ", task_dict["notes"], separator)

def print_task(task_dict):
    separator = f"\n" + "-"*37
    print(separator)
    print("id: ", task_dict["id"])
    print("description: ", task_dict["description"])
    print("status: ", task_dict["status"])
    print("dueDate: ", task_dict["dueDate"])
    print("createdAt: ", task_dict["createdAt"])
    print("updatedAt:", task_dict["updatedAt"])
    print("notes: ", task_dict["notes"], separator)