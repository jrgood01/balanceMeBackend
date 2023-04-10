## Code Summary
`userModel.py` is a Python module that defines the user class with methods for CRUD operations (create, read, update, delete) and other functionality such as getting daily tasks and returning user information in dictionary format. The module contains a `user` class that is instantiated with attributes such as `id`, `first_name`, `last_name`, `account_type`, `password`, `email`, and `points`. The class methods allow for updating user information, syncing user data to the database, retrieving user data, and returning user information in a dictionary format.

## Class Summaries
### `user`
The `user` class represents a user object and has the following attributes:
- id: user's unique identifier
- first_name: user's first name
- last_name: user's last name
- account_type: integer that represents the user's account type (0 for standard user)
- password: user's password
- email: user's email address
- points: integer that represents the user's number of points
- cursor: database cursor object for executing SQL queries

The class methods include:
- `sync()`: adds user data to the database
- `updateEmail(newEmail)`: updates the user's email address in the database
- `updateFirstName(newFirstName)`: updates the user's first name in the database
- `updateLastName(newLastName)`: updates the user's last name in the database
- `updatePoints(newPoints)`: updates the user's points in the database
- `getDailyTasks(startTime, endTime)`: retrieves daily tasks for the user within a specified time range
- `dict()`: returns a dictionary representing the user object

## Method Summaries
### `sync()`
```python
def sync(self):
    add_user = ("INSERT INTO users "
           "(first_name, last_name, account_type, password, email, points)"
           "VALUES ('%s', '%s', %d, '%s', '%s', %d)" % (self.first_name, self.last_name, self.account_type, self.password, self.email, 0))
    self.cursor.execute(add_user)
    return 
```
Adds a new user to the database using instance variables `first_name`, `last_name`, `account_type`, `password`, `email`, and 0 for `points`. Executes an SQL query to add this data to the `users` table in the database. Returns `None`.

### `updateEmail(newEmail)`
```python
def updateEmail(self, newEmail):
    self.email = newEmail
    update_query = ("UPDATE users "
                "SET `email` = '%s' "
                "WHERE `id` = %d" % (self.email, self.id)
    )
    print(update_query)
    self.cursor.execute(update_query)
    return
```
Updates the user's email address to a new email address provided as an argument `newEmail`. Updates the `email` field in the `users` table in the database where `id` is the user's `id`. Returns `None`.

### `updateFirstName(newFirstName)`
```python
def updateFirstName(self, newFirstName):
    self.first_name = newFirstName
    update_query = ("UPDATE users "
                "SET `first_name` = '%s' "
                "WHERE `id` = %d" % (self.first_name, self.id)
    )
    print(update_query)
    self.cursor.execute(update_query)
    return
```
Updates the user's first name to a new first name provided as an argument `newFirstName`. Updates the `first_name` field in the `users` table in the database where `id` is the user's `id`. Returns `None`.

### `updateLastName(newLastName)`
```python
def updateLastName(self, newLastName):
    self.last_name = newLastName
    update_query = ("UPDATE users "
                "SET `last_name` = '%s' "
                "WHERE `id` = %d" % (self.last_name, self.id)
    )
    print(update_query)
    self.cursor.execute(update_query)
    return
```
Updates the user's last name to a new last name provided as an argument `newLastName`. Updates the `last_name` field in the `users` table in the database where `id` is the user's `id`. Returns `None`.

### `updatePoints(newPoints)`
```python
def updatePoints(self, newPoints):
    self.points = newPoints
    update_query = ("UPDATE users "
                "SET `points` = '%s' "
                "WHERE `id` = %d" % (self.points, self.id)
    )
    print(update_query)
    self.cursor.execute(update_query)
    return
```
Updates the user's points to a new point value provided as an argument `newPoints`. Updates the `points` field in the `users` table in the database where `id` is the user's `id`. Returns `None`.

### `getDailyTasks(startTime, endTime)`
```python
def getDailyTasks(self, startTime, endTime):
    sql = ("SELECT * FROM users" 
          "WHERE `start_time` >= '%s'"
          "AND `start_time` <= '%s'" % (startTime, endTime)
    )
    self.cursor.execute(sql)
```
Retrieves daily tasks for the user within a specified time range. Executes an SQL query to select all data from the `users` table where the `start_time` field is greater than or equal to the `startTime` argument and less than or equal to the `endTime` argument. Returns `None`.

### `getAll(cursor)`
```python
@staticmethod
def getAll(cursor):
    get_user = "SELECT * FROM users"
    cursor.execute(get_user)
    results = self.cursor.fetchall()
    usr_str = "{"
    for userData in results:
        usr_str += str(user(userData[0], userData[1], userData[2],
         userData[3], userData[4], userData[5], userData[6]).dict()) + ","
    return usr_str[:-1] + "}"
```
Returns all users in the database as a string in JSON format. Executes an SQL query to select all data from the `users` table, converts each row of data to a user object, and returns the user objects as a string in JSON format.

### `byEmail(cursor, email)`
```python
@staticmethod
def byEmail(cursor, email):
    get_user = ("SELECT * FROM users WHERE `email` = '%s'" % (email))
    cursor.execute(get_user)
    results = cursor.fetchall()
    try:
        retUser = user(cursor, results[0][0], results[0][1], results[0][2], results[0][3], results[0][4], results[0][5], results[0][6])
    except:
        return user(cursor)
    return retUser
```
Retrieves a user object by their email address. Executes an SQL query to select all data from the `users` table where the `email` field matches the `email` argument. Converts the resulting data to a user object and returns it. If no user exists with the specified email address, returns an empty user object.

### `dict()`
```python
def dict(self):
    return {"first_name": self.first_name, "last_name": self.last_name,
    "account_type": self.account_type, "password": self.password, "email": self.email, "id": self.id, "points": self.points}
```
Returns a dictionary representing the user object.


## Example Usage
```python
# create a new user
user1 = user(cursor, id=1, first_name="John", last_name="Doe", account_type=0, password="password", email="johndoe@example.com", points=0)

# add user data to the database
user1.sync()

# update user email address
user1.updateEmail("newemail@example.com")

# update user first name
user1.updateFirstName("Jane")

# retrieve daily tasks for user within specified time range
user1.getDailyTasks(startTime="2022-01-01 00:00:00", endTime="2022-01-02 00:00:00")

# get all users from the database
all_users = user.getAll(cursor)

# get user by email address
user2 = user.byEmail(cursor, "johndoe@example.com")

# get user information in dictionary format
user1_dict = user1.dict()
```