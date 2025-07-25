# TaskTracker

This Project is a Task Tracker application that stores tasks in a JSON database.
---
Commands

**Add:** `add "Buy Tacos"`

> Adds the task to the database  
>All task's status are todo to start with

**Update** `update 3 "Buy Toilet Paper"`
> Updates the message of the task via its id

**Delete** `delete 2`
> Deletes the task from the data base using its id.  
>Once the task is deleted, the data base will update the ids to fill the gap that deleting a task will cause.

**Mark** `mark 4 in-progress`
> Changes the status of the task at the id's location to be changed.  
> The current options that you can choose from:
>
>* todo
>* in-progress
>* done

**list** `list all`
> Prints out a list of all the tasks currently in the JSON database. You can filter by the status.

---
This is a project for Roadmap:  
https://roadmap.sh/projects/task-tracker

