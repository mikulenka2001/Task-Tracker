from argparse import ArgumentParser
from datetime import datetime
import json_manipulation
import json
# USER INPUTS INTO THE CLI #
# Task name
# Task description/notes
# Due date (if any)

# OTHER FEATURES ###
# Task status
# Date it was captured

parser = ArgumentParser(description="Task Tracker")
subparsers = parser.add_subparsers(dest="command") # This is where we specify the task we want to do, list, add a task etc...

# add command
add_parser = subparsers.add_parser("add", help="Add a new task")

add_parser.add_argument("description", help = "Name/Short description of the task you want to add")
add_parser.add_argument("-note", "--notes", help = "Any notes important for succesfull completion of the task")
add_parser.add_argument("-due", "--due_date", help= "Due date for the task in format YYYY-MM-DD")
add_parser.add_argument("-s", "--status", choices=["to-do", "in-progress", "done"],
                        default = "to-do", help="initial status of your task")

# list command
list_parser = subparsers.add_parser("list", help="lists all tasks")

list_parser.add_argument("-t", "--task_types",
                          choices = ["all", "done", "to-do", "in-progress"],
                          default= "all",
                            help="Which tasks do we want to list? Lists all if none specified, other options are done/to-do/in-progress")

# mark command
mark_parser = subparsers.add_parser("mark", help="Mark task as done, to-do, or in progress")

mark_parser.add_argument("id", help="task id")
mark_parser.add_argument("mark", choices = ["done", "to-do", "in-progress"],
                         help = "updates status of the task with specified id")

# delete command
delete_parser = subparsers.add_parser("delete", help = "delete a task with a given id")

delete_parser.add_argument("id", help="id of task to be deleted")


# Parse arguments
args = parser.parse_args()

if args.command == "add":

    # load the json file containing task database
    task_list = json_manipulation.load_tasks()

    # create the dictionary for the new task
    new_task = json_manipulation.create_task_dict(task_list, args)

    # add the task to the database
    task_list.append(new_task)

    json_manipulation.save_tasks(task_list, filename = "tasks.json")

elif args.command == "list":
    #print("task types to be listed: ", args.task_types)
    task_list = json_manipulation.load_tasks(filename="tasks.json")


    if args.task_types == "all":
        for task in task_list:
            print(task)
    else:
        filtered_tasks = [task for task in task_list if task["status"] == args.task_types]
        print(filtered_tasks)
        for task in filtered_tasks:
            print(task)

elif args.command == "delete":

    task_list = json_manipulation.load_tasks(filename="tasks.json")

    # conditionally delete the task dictionary with specified args.id
    target_id = args.id
    for index, task in enumerate(task_list):
        if task["id"] == target_id:
            target_index = index
        else:
            Exception("No task with specified ID found")
    
    task_list.pop(index = target_index)

elif args.command == "mark":
    print("task id to be updated:", args.id)
    print("mark of the updated task: ", args.mark )
else:
    parser.print_help()

# Store parsed arguments into a dictionary
