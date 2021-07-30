from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from model.userModel import user
from model.taskModel import task
import mysql.connector

app = Flask(__name__)


balance_me_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="balancemedev",
  database="balance_me",
  auth_plugin='mysql_native_password'
)

cursor = balance_me_db.cursor()

@app.route('/createUser', methods=['POST'])
def createUser():
    data = request.get_json()
    print(data)
    addUser = user(cursor, first_name=data["first_name"], last_name=data["last_name"], account_type=data["account_type"],password=data["password"],email=data["email"])
    addUser.sync()
    return jsonify(str(addUser.dict()))

@app.route('/loginUser', methods=['GET'])
def loginUser():
    addUser = user.byEmail(cursor,request.args.get("email"))
    return jsonify(str(addUser.dict()))

@app.route('/getUser', methods=['GET'])
def getUser():
    addUser = user.byEmail(cursor, request.args.get("email"))
    return jsonify(str(addUser.dict()))

@app.route('/getAllUsers', methods=['GET'])
def getAllUsers():
    userList = user.getAll(cursor)
    return jsonify(str(userList))

@app.route('/getDailyTasks', methods=['GET'])
def getDailyTasks():
    refUser = user.byEmail(cursor, request.args.get("email"))
    refUser.getDailyTasks(request.args.get("start_time"), request.args.get("end_time"))
    return 

@app.route('/updateEmail', methods=['POST'])
def updateEmail():
    data = request.get_json()
    addUser = user.byEmail(cursor,data["oldEmail"])
    addUser.updateEmail(data["newEmail"])
    return jsonify(str(addUser.dict()))   

@app.route('/updateFirstName', methods=['POST'])
def updateFirstName():
    data = request.get_json()
    addUser = user.byEmail(cursor,data["email"])
    addUser.updateFirstName(data["first_name"])
    return jsonify(str(addUser.dict()))   

@app.route('/updateFirstName', methods=['POST'])
def updateLastName():
    data = request.get_json()
    addUser = user.byEmail(cursor,data["email"])
    addUser.updateLastName(data["last_name"])
    return jsonify(str(addUser.dict()))  

@app.route('/updatePoints', methods=['POST'])
def updatePoints():
    data = request.get_json()
    addUser = user.byEmail(cursor,data["email"])
    addUser.updatePoints(data["points"])
    return jsonify(str(addUser.dict()))   

@app.route("/createTask", methods=['POST'])
def createTask():
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
            estimated_time=data['estimated_time'], description=data['description'], start_time=data['start_time'], 
            estimated_completion_time=data['estimated_completion_time'], status=data['status'], image_path=data['image_path'],
            assigned_user_id=data['assigned_user_id'], created_user_id=data['created_user_id'])
    
    addTask.createTask()
    return jsonify(str(addTask.dict))

try:
    balance_me_db.autocommit = True
except Exception as e:
    print(e)
if __name__ == "__main__":
    app.run(debug=True)
