# Code Summary

The `task` class in `taskModel.py` contains methods to create a new task and retrieve task information in the form of a dictionary.

## `task` class

### `__init__` method

The constructor method for the `task` class.

Parameters:
- `cursor`: The database cursor object.
- `id=''`: The ID of the task.
- `name=''`: The name of the task.
- `point_value=''`: The point value of the task.
- `category_id=''`: The category ID of the task.
- `estimated_time=''`: The estimated time to complete the task.
- `description=''`: The description of the task.
- `start_time=''`: The start time of the task.
- `estimated_completion_time=''`: The estimated time of task completion.
- `status=''`: The status of the task.
- `completion_time=''`: The completion time of the task.
- `image_path=''`: The path of the image for the task.
- `assigned_user_id=-1`: The ID of the user assigned to the task.
- `created_user_id=-1`: The ID of the user who created the task.
- `history=''`: The history of the task.
- `repeat=''`: The repeat information of the task.
- `completed=''`: The completion status of the task.
- `active=1`: The activity status of the task.
- `steps=''`: The steps information of the task.

### `createTask` method

This method creates a new task in the database using the values provided in the constructor.

Example usage:

```
cursor = db.cursor()
new_task = task(cursor, name='New Task', point_value=10)
new_task.createTask()
```

### `dict` method

This method returns a dictionary containing the task information.

Example usage:

```
task_info = new_task.dict()
print(task_info['name']) # Output: 'New Task'
```

# Class Summaries

N/A

# Method Summaries

## `__init__(self, cursor, id='',name='', point_value='', category_id='', estimated_time='', description='', start_time='', estimated_completion_time='', status='', completion_time='', image_path='', assigned_user_id=-1, created_user_id=-1,history='',repeat='',completed='',active=1,steps='')`

The constructor method for the `task` class.

## `createTask(self)`

This method creates a new task in the database using the values provided in the constructor.

## `dict()`

This method returns a dictionary containing the task information.

# Example Usage

```
import mysql.connector as mysql

# connect to the database
db = mysql.connect(
    host = "localhost",
    user = "user",
    password = "password",
    database = "tasks"
)

# create a task
cursor = db.cursor()
new_task = task(cursor, name='New Task', point_value=10)
new_task.createTask()

# get task information
task_info = new_task.dict()
print(task_info['name']) # Output: 'New Task'

db.close()
```