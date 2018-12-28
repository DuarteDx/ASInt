from flask import Flask
from flask import redirect
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from DB import DB

#Functions from functions.py
import functions as f

server = Flask(__name__)
db = DB()
cors = CORS(server)
server.config['CORS_HEADERS'] = 'Content-Type'


###################
# CLIENT ENDPOINTS
###################

@server.route('/sendUserInfo', methods=['POST', 'OPTIONS'])
@cross_origin()
def getClientInfo():
    #Get data from client
    data = request.get_json(silent=True)
    #Parse response
    userID = data['data']['id']
    userName = data['data']['name']
    print('Received user info: ' + str(userID) + ' - ' + str(userName))
    #Add user to database if new    
    db.addUser(int(userID), userName)

    return '[S]User info received: ' + str(userID) + ' - ' + str(userName)



@server.route('/sendLocation', methods=['POST', 'OPTIONS'])
@cross_origin()
def getClientLocation():
    #Get a location from a client and add it to database   
    # REDO to update logs and buildings 
    #Get data from client
    data = request.get_json(silent=True)
    #Parse response
    userID = data['data']['user']
    location = data['data']['location']
    latitude = location['latitude']
    longitude = location['longitude']
    print(userID)
    print(location)    
    #Update user in database
    db.updateUser(userID, latitude=latitude, longitude=longitude)
    #print(userLocations)
    return '[S]Location received: ' + str(latitude) + '  ' + str(longitude) + ' by id: ' + str(userID)


@server.route('/defineRange', methods=['POST', 'OPTIONS'])
@cross_origin()
def getClientRange():
    #Get a range from a client and add it to database
    #Get data from client
    data = request.get_json(silent=True)
    #Parse response
    userID = data['data']['user']
    userRange = data['data']['range']
    userRange = int(userRange)
    print('Received range from ' + str(userID) + ': ' + str(userRange))
    db.updateUser(userID, rang = userRange)
    return '[S]Range received from ' + str(userID) + ': ' + str(userRange)



@server.route('/broadcastClientMessage', methods=['POST', 'OPTIONS'])
@cross_origin()
def broadcastClientMessage():
    #Get a message from a client and broadcast it to nearby users
    #Get data from client
    data = request.get_json(silent=True)
    #Parse response
    userID = data['data']['user']
    userMessage = data['data']['message']
    print('Message from ' + str(userID) + ': ' + str(userMessage))
    #Add message to database

    f.broadcastMessage(db, userID, db.getNameFromID(userID), userMessage)

    return '[S]Message received from ' + str(userID) + ': ' + str(userMessage)



@server.route('/getPeopleInRange', methods=['POST', 'OPTIONS'])
@cross_origin()
def getPeopleInRange():
    #Send a list of nearby users to client
    nearbyUsersList = list()
    #Get data from client
    data = request.get_json(silent=True)
    #Parse response
    userID = data['data']['user']
    print('User ' + str(userID) + ' requested list of nearby users')
    #Get nearby users from database
    nearbyUsersList = db.getUsersInRange(userID)
    return jsonify(nearbyUsersList)



@server.route('/getUserMessages', methods=['POST', 'OPTIONS'])
@cross_origin()
def getUserMessages():
    #Sends a list of messages to client

    #Get data from client
    data = request.get_json(silent=True)
    #Parse response
    userID = data['data']['user'] 
    userID = int(userID)
    print('User ' + str(userID) + ' requested his list of messages')

    #Get client's messages from database
    listOfMessages = db.users[userID].readMessages()
    return jsonify(listOfMessages)


#################
# ADMIN ENDPOINTS
#################

# Receives building information: 
# 'buildingID', 'buildingName', 'latitude', 'longitude'
@server.route('/addBuildingToDB', methods=['POST', 'OPTIONS'])
@cross_origin()
def addBuildingToDB():
    #Get a building information from an admin and add the building to the database
    #Get data from request
    data = request.get_json(silent=True)
    buildingID = data['data']['buildingID'] 
    buildingName = data['data']['buildingName'] 
    latitude = data['data']['latitude'] 
    longitude = data['data']['longitude'] 
    print('Received new building info: ID:' + str(buildingID) + ' name: ' + buildingName + ' latitude: ' + latitude + ' longitude: ' + longitude)
    db.addBuilding(buildingID, buildingName, latitude, longitude)

    return '[S]Received building ID ' + str(buildingID) + ': ' + buildingName


@server.route('/getLoggedInUsers', methods=['POST', 'OPTIONS'])
@cross_origin()
def getLoggedInUsers():
    #Send a list logged in users to admin
    return jsonify(db.getAllUsers())

# 'buildingID' ~ or name
@server.route('/getUsersInBuilding', methods=['POST', 'OPTIONS'])
@cross_origin()
def getUsersInBuilding():
    #Send a list of users in specific building    
    # #Get data from request
    data = request.get_json(silent=True)
    buildingID = data['data']['buildingID']
    userList = db.buildings[buildingID].getUsersInside()
    # returns a list of user ID's
    return jsonify(userList)

# 'UserID' or 'buildingID' or both
@server.route('/getHistory', methods=['POST', 'OPTIONS'])
@cross_origin()
def getUserHistory():
    # Get data from request
    data = request.get_json(silent=True)
    userID = data['data']['userID']
    buildingID = data['data']['buildingID']

    # Retrieve logs from database
    if (userID != 'None' and buildingID != 'None'):
        logs = db.retrieveLogs(userID, buildingID)
    elif (userID != 'None' and buildingID == 'None'):
        logs = db.retrieveLogs(userID)
    elif (userID == 'None' and buildingID != 'None'):
        logs = db.retrieveLogs(buildingID)
    elif (userID == 'None' and buildingID == 'None'):
        logs = db.retrieveLogs()
    
    return jsonify(logs)




'''
###############
# BOT ENDPOINTS
###############

@server.route('/broadcastBotMessage')
def broadcastBotMessage():
    #Get a message from a bot and broadcast it to users inside the building associated to the bot'''

if __name__ == '__main__':
    server.run()