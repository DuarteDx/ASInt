from flask import Flask
from flask import redirect
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from DB import DB

#Functions from functions.py
import functions

server = Flask(__name__)
db = DB()
cors = CORS(server)
server.config['CORS_HEADERS'] = 'Content-Type'


#database = DB()

###################
# CLIENT ENDPOINTS
###################

@server.route('/sendLocation', methods=['POST', 'OPTIONS'])
@cross_origin()
def getClientLocation():
    #Get a location from a client and add it to database    
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
    db.addMessage(userID, userMessage)

    return '[S]Message received from ' + str(userID) + ': ' + str(userMessage)

@server.route('/getPeopleInRange', methods=['POST', 'OPTIONS'])
@cross_origin()
def getPeopleInRange():
    #Send a list of nearby users to client

    #Get data from client
    data = request.get_json(silent=True)
    #Parse response
    userID = data['data']['user']
    print('User ' + str(userID) + ' requested list of nearby users')

    #Get nearby users from database
    #nearbyUsersList = ...

    #return nearbyUsersList
    return '[S]1'

@server.route('/getUserMessages', methods=['POST', 'OPTIONS'])
@cross_origin()
def getUserMessages():
    #Sends a list of messages to client

    #Get data from client
    data = request.get_json(silent=True)
    #Parse response
    userID = data['data']['user'] 
    print('User ' + str(userID) + ' requested his list of messages')

    #Get client's messages from database
    #listOfMessages = ...

    #return listOfMessages
    return '[S]2'

'''
#################
# ADMIN ENDPOINTS
#################

@server.route('/addBuildingToDB')
# atenção a segurança
def addBuildingToDB():
    #Get a building information from an admin and add the building to the database

@server.route('/getLoggedInUsers')
def getLoggedInUsers():
    #Send a list logged in users to admin

@server.route('/getPeopleByBuilding')
def getPeopleByBuilding():
    #Send a list of users in specific building

@server.route('/getUserHistory')
def getUserHistory():
    #Send a list of exchanged messages and movements by users

@server.route('/getMessagesByBuilding')
def getMessagesByBuilding():
    #Send a list of messages all exchanged in a specific building

###############
# BOT ENDPOINTS
###############

@server.route('/broadcastBotMessage')
def broadcastBotMessage():
    #Get a message from a bot and broadcast it to users inside the building associated to the bot'''

if __name__ == '__main__':
    server.run()