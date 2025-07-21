# Goal - The application should run from the command line, accept user actions and inputs as arguments
# and store the tasks in a JSON flie. The user shoudl be able to:
# Add, Update and Delete tasks
# Mark a task as in progress or doen
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress



import json, os, argparse,sys
from datetime import datetime


def main():
    arguments = sys.argv
    #print(arguments)

    match arguments[1]:
        case "add":
            add_task(arguments[2])
        case "update":
            update_task(arguments[2],arguments[3])
        case "delete":
            delete_task(arguments[2])
        case "mark":
            update_status(arguments[2], arguments[3])
        case"list":
            try:
                if arguments[2] == ("done" or "todo" or "in-progress"):
                    list_task([arguments[2]])
            except IndexError:
                list_task()
        case _:
            EOFError("Error: Command Not Recocnized")
file_path = "task_tracker.json"

time = datetime.now()
formatted_time = time.strftime('%H:%M %d %m %Y')
# Task Properties
# id: A unique identifier for the task
# description: A short description of hte task
# status: the status of the task (todo, in-progress, done)
# createdAt: The date and time when the task was created
# updatedAt: The date and time when the task was updated
def add_task(message:str):
    # add the add argument into task

    if os.path.exists(file_path):
        with open(file_path,"r") as file:
                data = json.load(file)

                last_id = max(item["id"] for item in data) if data else 0
                tasks = {
                "id": last_id + 1,
                "description":message,
                "status": "todo",
                "createdAt": formatted_time,
                "updatedAt": formatted_time
                }
                data.append(tasks)
        with open(file_path,"w") as file:
                json.dump(data, file, indent = 4)
    else:
        tasks = [
            {
                "id":1,
                "description":message,
                "status": "todo",
                "createdAt": formatted_time,
                "updatedAt": formatted_time
            }
            ]
        with open(file_path,"w") as file:
            json.dump(tasks, file, indent = 4)



def update_task():
    print(args.update, args.message)
def delete_task():
    pass
def update_status(id:int = -1):
    print(id, args.mark)

def list_task(mode:str = ""):
    
    with open(file_path, "r") as file:
        data = json.load(file)
        for item in data:
            if item["status"] == mode or mode == "": # If the task is the same as the status we are looking for or if we are looking for all the tasks
                print (f"id:{item["id"]}, desc: {item["description"]}, status: {item["status"]}")
            

def upadate_task_id():
    pass


if __name__ == "__main__":
    main()