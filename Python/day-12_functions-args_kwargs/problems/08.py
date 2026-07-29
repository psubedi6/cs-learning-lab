def add_task(task, task_list=None):
    task_list = []
    task_list = task_list.append()

add_task("Study Python")
add_task("Practice functions")
my_tasks = ["Finish assignment"]
add_task("Push to GitHub", my_tasks)
add_task("Review notes", my_tasks)

"""Exercise 8 — Mutable Default Argument Bug

Problem:

Create a function named add_task.

The function should have:
- A required parameter named task.
- A default parameter named task_list.
- The default value for task_list must be None (not an empty list []).

Function definition:

def add_task(task, task_list=None):

Requirements:

1. Check whether task_list is None.
2. If task_list is None, create a new empty list.
3. Add task to the list using the .append() method.
4. Print the updated list.

Call the function with the following:

add_task("Study Python")
add_task("Practice functions")

my_tasks = ["Finish assignment"]

add_task("Push to GitHub", my_tasks)
add_task("Review notes", my_tasks)

Expected Output:

['Study Python']
['Practice functions']
['Finish assignment', 'Push to GitHub']
['Finish assignment', 'Push to GitHub', 'Review notes']

Concepts Being Tested:
- Required parameters
- Default parameters
- None
- Lists
- .append()
- Mutable default argument bug"""