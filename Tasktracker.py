# Goal - The application should run from the command line, accept user actions and inputs as arguments
# and store the tasks in a JSON flie. The user shoudl be able to:
# Add, Update and Delete tasks
# Mark a task as in progress or doen
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

# Task Properties
# id: A unique identifier for the task
# description: A short description of hte task
# status: the status of the task (todo, in-progress, done)
# createdAt: The date and time when the task was created
# updatedAt: The date and time when the task was updated

import json, os, argparse
from datetime import datetime

pars = argparse.ArgumentParser(
    description= "Manages taks via the command line",
    epilog= "Example usage: python Tasktracker.py filename.json -a 'New Task"
)
# Creating the arguments
pars.add_argument("-a","--add", help= "Adds a task to the list",required= False)
pars.add_argument("-l","--list", help="Type '-l todo/in-progress/done/all to show that cateory of tasks",requierd= False)
pars.add_argument("-m","--mark",help="Changes the status of desired task to todo/in-progress/done",requierd= False)
pars.add_argument("-d","--delete",help="Deletes the desired task",requierd= False)
pars.add_argument("-u","--update",help="Changes the description of the desired task",requierd= False)

#Processing the argument

args = pars.parse_args()

file_path = "task_tracker.json"

time = datetime.now()
formatted_time = time.strftime('%H:%M %d %M %Y')

def add_task():
    pass

def update_task(id):
    pass
def delete_task(id):
    pass
def update_status(id, status):
    pass

def list_task ():
    pass

def upadate_task_it():
    pass