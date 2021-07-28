from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from model.userModel import user
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
    addUser = user(first_name=data["first_name"], last_name=data["last_name"],
    account_type=data["account_type"],password=data["password"],email=data["email"])
    try:
        addUser.sync()
    except Exception as e:
        print("ERROR: "+e)
    return jsonify(str(addUser.dict()))

@app.route('/loginUser', methods=['GET'])
def loginUser():
    addUser = user.byEmail(request.args.get("email"))
    return jsonify(str(addUser.dict()))

@app.route('/getUser', methods=['GET'])
def getUser():
    addUser = user.byEmail(request.args.get("email"))
    return jsonify(str(addUser.dict()))

@app.route('/getAllUsers', methods=['GET'])
def getAllUsers():
    userList = user.getAll()
    return jsonify(str(userList))

@app.route('/updateEmail', methods=['POST'])
def updateEmail():
    data = request.get_json()
    addUser = user.byEmail(data["oldEmail"])
    addUser.updateEmail(data["newEmail"])
    return jsonify(str(addUser.dict()))   

@app.route('/updateFirstName', methods=['POST'])
def updateFirstName():
    data = request.get_json()
    addUser = user.byEmail(data["email"])
    addUser.updateFirstName(data["first_name"])
    return jsonify(str(addUser.dict()))   

@app.route('/updateFirstName', methods=['POST'])
def updateLastName():
    data = request.get_json()
    addUser = user.byEmail(data["email"])
    addUser.updateLastName(data["last_name"])
    return jsonify(str(addUser.dict()))  

@app.route('/updatePoints', methods=['POST'])
def updatePoints():
    data = request.get_json()
    addUser = user.byEmail(data["email"])
    addUser.updatePoints(data["points"])
    return jsonify(str(addUser.dict()))    

try:
    balance_me_db.autocommit = True
except Exception as e:
    print(e)
if __name__ == "__main__":
    app.run(debug=True)
