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
    # print(arguments)

    match arguments[1]:
        case "add":
            add_task(arguments[2])
        case "update":
            update_task(int(arguments[2]),arguments[3])
        case "delete":
            delete_task(int(arguments[2]))
        case "mark":
            update_status(arguments[2], arguments[3])
        case"list":
            try:
                if arguments[2] == "done" or "todo" or "in-progress":
                    list_task(arguments[2])
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



def update_task(id:int = -1, message = ""):
    print(id)
    update = False
    item_to_update = None
    with open(file_path,"r") as file:
        data = json.load(file)
        for item in data:
            if int(item["id"]) == id:
                update = True
                item_to_update = item
                data.remove(item)
                break
        if update == True:
            item_to_update["description"] = message
            item_to_update["updatedAt"] = formatted_time
            data.append(item_to_update)
            with open(file_path,"w") as file:
                json.dump(data, file, indent = 4)
        else:
            print("not working")

def delete_task(id:int = -1):
    removetask = False
    task_to_remove = None
    with open(file_path, "r") as file:
        data = json.load(file)
        for item in data:
            if int(item["id"]) == id:
                removetask = True
                task_to_remove = item
                break
        if removetask == True:
            data.remove(task_to_remove)
            with open(file_path, "w") as file:
                json.dump(data,file, indent = 4)
            upadate_task_id(id)
            print(f"Task status from id: {id}")
            print(f"has been deleted")
        else:
            pass

def update_status(imessage:str,d:int = -1):
    pass

def list_task(mode:str = ""):
    with open(file_path, "r") as file:
        data = json.load(file)
        for item in data:
            if item["status"] == mode or mode == "": # If the task is the same as the status we are looking for or if we are looking for all the tasks
                print (f"id:{item["id"]}, desc: {item["description"]}, status: {item["status"]}")



def upadate_task_id(id:int = -1):
    task = None
    with open(file_path,"r") as file:
        data = json.load(file)
        for index,item in enumerate(data):
            if int(item["id"]) > id:
                data.remove(item)
                item["id"] = int(item["id"]) - 1
                data.append(item)
        with open(file_path,"w") as file:
            json.dump(data,file, indent = 4)


if __name__ == "__main__":
    main()