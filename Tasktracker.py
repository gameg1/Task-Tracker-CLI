# Goal - The application should run from the command line, accept user actions and inputs as arguments
# and store the tasks in a JSON flie. The user shoudl be able to:
# Add, Update and Delete tasks
# Mark a task as in progress or doen
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress



import json, os, argparse
from datetime import datetime

pars = argparse.ArgumentParser(
    description= "Manages taks via the command line",
    epilog= "Example usage: python Tasktracker.py filename.json -a 'New Task"
)
# Creating the arguments

pars.add_argument("-id", help = "The id of the task you want to access", type= int, default = -1)
pars.add_argument("-a","--add", help= "Adds a task to the list",type= str)
pars.add_argument("-l","--list", help="Type '-l todo/in-progress/done/all to show that cateory of tasks",choices= ["todo","in-progress","done","all"], default = "all")
pars.add_argument("-m","--mark",help="Changes the status of desired task to todo/in-progress/done",type=str, choices =["todo","in-progress","done"])
pars.add_argument("-d","--delete",help="Deletes the desired task", type = int, default= -1)
pars.add_argument("-u","--update",help="Changes the description of the desired task via id")

# Processing the argument
# Allows use to use the arguments and get the information to usterlize it.
args:argparse.Namespace = pars.parse_args()

file_path = "task_tracker.json"

time = datetime.now()
formatted_time = time.strftime('%H:%M %d %M %Y')
# Task Properties
# id: A unique identifier for the task
# description: A short description of hte task
# status: the status of the task (todo, in-progress, done)
# createdAt: The date and time when the task was created
# updatedAt: The date and time when the task was updated
def add_task():
    # add the add argument into task
    task = args.add
    if not os.path.exists(file_path):
        # Create a task as a dict because of a new json file
        tasks = [
            {
                "id":1,
                "description":args.add,
                "status": "todo",
                "createdAt": formatted_time,
                "updatedAt": formatted_time
            }
        ]
        with open(file_path,"w") as file:
            json.dump(tasks, file, indent= 4)
    # If the file exists, add into the json file
    else:
        with open(file_path,"r") as file:
            data = json.load(file)
            # get the last id from json file
            last_id = max(item["id"] for item in data) if data else 0
            new_task = {
                "id":last_id + 1,
                "description":args.add,
                "status": "todo",
                "createdAt": formatted_time,
                "updatedAt": formatted_time
            }

        with open(file_path, "w") as file:
            json.dump(data, file, indent = 4)


def update_task(id:int = -1):
    print(args.update, args.message)
def delete_task(id:int = -1):
    pass
def update_status(id:int = -1):
    print(id, args.mark)

def list_task():
    
    with open(file_path, "r") as file:
        data = json.load(file)
        for item in data:
            if item["status"] == args.list or args.list == "all": # If the task is the same as the status we are looking for or if we are looking for all the tasks
                print (f"id:{item["id"]}, desc: {item["description"]}, status: {item["status"]}")
            

def upadate_task_id():
    pass

if args.add:
    add_task()
if args.list:
    list_task()
if args.mark:
    update_status()
if args.delete:
    delete_task()
if args.update:
    update_task()