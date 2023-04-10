# Code Summary

This file contains Flask API routes for user authentication, user and task actions. It includes the following Flask routes: 

- `/createUser`: Creates a new user in the database
- `/loginUser`: Retrieves an existing user object from the database based on email
- `/getUser`: Retrieves an existing user object from the database based on email
- `/getAllUsers`: Retrieves all the users from the database
- `/getDailyTasks`: Retrieves daily tasks for a provided user within a specified time range
- `/updateEmail`: Updates the user email in the database for a specified user
- `/updateFirstName`: Updates the user first name in the database for a specified user
- `/updateLastName`: Updates the user last name in the database for a specified user
- `/updatePoints`: Updates the user points value in the database for a specified user
- `/createTask`: Creates a new task object in the database

# Class Summaries

No classes are defined in this file.

# Method Summaries

## createUser()
```python
@app.route('/createUser', methods=['POST'])
def createUser():
    """
    Creates a new user in the database

    Returns:
    Returns a JSON string of the new user's dictionary representation.
    """
    data = request.get_json()
    addUser = user(cursor, first_name=data["first_name"], last_name=data["last_name"], account_type=data["account_type"],password=data["password"],email=data["email"])
    addUser.sync()
    return jsonify(str(addUser.dict()))
```

This is a Flask API route to create a new user in the database. It takes in form data as a JSON object that includes a user's first name, last name, account type, password, and email. It creates a new `user` object with the provided data using the `user` model and inserts it into the database. The output is a JSON string of the new user's dictionary representation.

## loginUser()
```python
@app.route('/loginUser', methods=['GET'])
def loginUser():
    """
    Retrieves an existing user object from the database based on email

    Returns:
    Returns a JSON string of the user's dictionary representation.
    """
    addUser = user.byEmail(cursor,request.args.get("email"))
    return jsonify(str(addUser.dict()))
```

This is a Flask API route to retrieve an existing user object from the database based on email. It takes in the email as a parameter via a GET request. It retrieves the `user` object from the database using the `byEmail` method on the `user` model and returns a JSON string of the user's dictionary representation.

## getUser()
```python
@app.route('/getUser', methods=['GET'])
def getUser():
    """
    Retrieves an existing user object from the database based on email

    Returns:
    Returns a JSON string of the user's dictionary representation.
    """
    addUser = user.byEmail(cursor, request.args.get("email"))
    return jsonify(str(addUser.dict()))
```

This is a Flask API route to retrieve an existing user object from the database based on email. It takes in the email as a parameter via a GET request. It retrieves the `user` object from the database using the `byEmail` method on the `user` model and returns a JSON string of the user's dictionary representation.

## getAllUsers()
```python
@app.route('/getAllUsers', methods=['GET'])
def getAllUsers():
    """
    Retrieves all the users from the database

    Returns:
    Returns a JSON string of an array of all the user's dictionary representations.
    """
    userList = user.getAll(cursor)
    return jsonify(str(userList))
```

This is a Flask API route to retrieve all the users from the database. It retrieves a list of all the `user` objects from the database using the `getAll` method on the `user` model and returns a JSON string of an array of all the user's dictionary representations.

## getDailyTasks()
```python
@app.route('/getDailyTasks', methods=['GET'])
def getDailyTasks():
    """
    Retrieves daily tasks for a provided user within a specified time range

    Returns:
    No return value
    """
    refUser = user.byEmail(cursor, request.args.get("email"))
    refUser.getDailyTasks(request.args.get("start_time"), request.args.get("end_time"))
    return 
```

This is a Flask API route to retrieve daily tasks for a provided user within a specified time range. It takes in the email, start time, and end time as parameters via a GET request. It retrieves the `user` object from the database using the `byEmail` method on the `user` model and calls the `getDailyTasks` method on that object using the start and end time parameters. The output of this method is not clearly defined as the method does not return any value but is likely used in some later part of the application. 

## updateEmail()
```python
@app.route('/updateEmail', methods=['POST'])
def updateEmail():
    """
    Updates the user email in the database for a specified user

    Returns:
    Returns a JSON string of the updated user's dictionary representation.
    """
    data = request.get_json()
    addUser = user.byEmail(cursor,data["oldEmail"])
    addUser.updateEmail(data["newEmail"])
    return jsonify(str(addUser.dict()))   
```

This is a Flask API route to update the user email in the database for a specified user. It takes in a JSON object with keys 'oldEmail' and 'newEmail' as input. It fetches a `user` object from the database using the `byEmail` method on the `user` model, passing the cursor and 'oldEmail' data. Then, the `updateEmail` method of the fetched `user` object is called, passing the 'newEmail' data to update the user's email. Finally, the updated `user` object is returned in JSON format.

## updateFirstName()
```python
@app.route('/updateFirstName', methods=['POST'])
def updateFirstName():
    """
    Updates the user first name in the database for a specified user

    Returns:
    Returns a JSON string of the updated user's dictionary representation.
    """
    data = request.get_json()
    addUser = user.byEmail(cursor,data["email"])
    addUser.updateFirstName(data["first_name"])
    return jsonify(str(addUser.dict()))   
```

This is a Flask API route to update the user first name in the database for a specified user. It takes in JSON data parameter. It calls the `byEmail` method on the `user` model to identify a `user` object using the email from the 'data' parameter. It then updates the first name of the identified `user` with `addUser.updateFirstName` method using the first name from the 'data' parameter. It finally returns the updated dictionary of the `addUser` as a JSON response.

## updateLastName()
```python
@app.route('/updateLastName', methods=['POST'])
def updateLastName():
    """
    Updates the user last name in the database for a specified user

    Returns:
    Returns a JSON string of the updated user's dictionary representation.
    """
    data = request.get_json()
    addUser = user.byEmail(cursor,data["email"])
    addUser.updateLastName(data["last_name"])
    return jsonify(str(addUser.dict()))  
```

This is a Flask API route to update the user last name in the database for a specified user. It receives data in JSON format with email and last name of a user, and then updates the last name of the corresponding user in the database. Finally, it returns a JSON response with the updated user data. The subcall `user.byEmail` is used to query the database and retrieve the user, and the `updateLastName` method on the retrieved `user` object is called to update the last name.

## updatePoints()
```python
@app.route('/updatePoints', methods=['POST'])
def updatePoints():
    """
    Updates the user points value in the database for a specified user

    Returns:
    Returns a JSON string of the updated user's dictionary representation.
    """
    data = request.get_json()
    addUser = user.byEmail(cursor,data["email"])
    addUser.updatePoints(data["points"])
    return jsonify(str(addUser.dict()))   
```

This is a Flask API route to update the user points value in the database for a specified user. This method updates a user's points value by taking in a JSON payload through a POST request. It calls the `byEmail` function of the `user` object to retrieve user details based on the provided email address in the payload data. The user's points value is then updated using the `updatePoints` method of the returned `user` object. The updated user information is returned as a JSON response. The method has no parameters and returns a JSON formatted response containing the updated user information. The subcalls used in this method include `request.get_json()`, `user.byEmail()`, `addUser.updatePoints()`, and `jsonify()`.

## createTask()
```python
@app.route("/createTask", methods=['POST'])
def createTask():
    """
    Creates a new task object in the database

    Returns:
    Returns a JSON string of the new task's dictionary representation.
    """
    data = request.get_json()
    data = data['data']
    del_vals = []
    for each in data:
        if data[each] == None:
            del_vals.append(each)
    for each in del_vals:
        del data[each]
    if data['estimated_completion_time'] == None and data['start_time'] == None: 
        addTask = task(cursor, name=data['name'], point_value=data['point_value'], category_id=data['category_id'],
            estimated_time=data['estimated_time'], description=data['description'], status=data['status'], image_path=data['image_path'],
            assigned_user_id=data['assigned_user_id'], created_user_id=data['created_user_id'])
    elif data['estimated_completion_time'] == None and data['start_time'] != None:
        addTask = task(cursor, name=data['name'], point_value=data['point_value'], category_id=data['category_id'],
            estimated_time=data['estimated_time'], description=data['description'], start_time=data['start_time'], status=data['status'], image_path=data['image_path'],
            assigned_user_id=data['assigned_user_id'], created_user_id=data['created_user_id'])
    elif data['start_time'] == None and data['estimated_completion_time'] != None:
        addTask = task(cursor, name=data['name'], point_value=data['point_value'], category_id=data['category_id'],
            estimated_time=data['estimated_time'], description=data['description'], 
            estimated_completion_time=data['estimated_completion_time'], status=data['status'], image_path=data['image_path'],
            assigned_user_id=data['assigned_user_id'], created_user_id=data['created_user_id'])
    else:
        addTask = task(cursor, name=data['name'], point_value=data['point_value'], category_id=data['category_id'],
            estimated_time=data['estimated_time'], description=data['description'], start_time=data