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
    prog= "Tasktracker.py"
)


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