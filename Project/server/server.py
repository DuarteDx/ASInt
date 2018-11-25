from flask import Flask
from flask import redirect
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

#Functions from functions.py
import functions

server = Flask(__name__)
cors = CORS(server)
server.config['CORS_HEADERS'] = 'Content-Type'

userLocations = []

###################
# CLIENT ENDPOINTS
###################

@server.route('/sendLocation', methods=['POST', 'OPTIONS'])
@cross_origin()
def getClientLocation():
    #Get a location from a client and add it to database
    data = request.get_json(silent=True)
    print(data)
    userLocations.append(data)
    print(userLocations)
    return 'Location sent!'


'''@server.route('/defineRange')
def getClientRange():
    #Get a range from a client and add it to database

@server.route('/broadcastClientMessage')
def broadcastClientMessage():
    #Get a message from a client and broadcast it to nearby users

@server.route('/getPeopleInRange')
def getPeopleInRange():
    #Send a list of nearby users to client

#################
# ADMIN ENDPOINTS
#################

@server.route('/addBuildingToDB')
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