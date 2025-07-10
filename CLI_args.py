from argparse import ArgumentParser

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

# list command
list_parser = subparsers.add_parser("list", help="lists all tasks")

list_parser.add_argument("-t", "--task_types",
                          choices = ["all", "done", "to-do", "in progress"],
                          default= "all",
                            help="Which tasks do we want to list? Lists all if none specified, other options are done/to-do/in progress")

# mark command
mark_parser = subparsers.add_parser("mark", help="Mark task as done, to-do, or in progress")

mark_parser.add_argument("id", help="task id")
mark_parser.add_argument("mark", choices = ["done", "to-do", "in progress"],
                         help = "updates status of the task with specified id")


# Parse arguments
args = parser.parse_args()

if args.command == "add":
    print("Description: ", args.description)
    print("Due date: ",args.due_date)
elif args.command == "list":
    print("task types to be listed: ", args.task_types)
elif args.command == "mark":
    print("task id to be updated:", args.id)
    print("mark of the updated task: ", args.mark )
else:
    parser.print_help()
