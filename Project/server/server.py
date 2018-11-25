from flask import Flask
from flask import redirect
from flask import request
from flask import jsonify

#Functions from functions.py
import functions

server = Flask(__name__)

###################
# CLIENT ENDPOINTS
###################

@app.route('/sendLocation')
def getClientLocation():
    #Get a location from a client and add it to database

@app.route('/defineRange')
def getClientRange():
    #Get a range from a client and add it to database

@app.route('/broadcastClientMessage')
def broadcastClientMessage():
    #Get a message from a client and broadcast it to nearby users

@app.route('/getPeopleInRange')
def getPeopleInRange():
    #Send a list of nearby users to client

#################
# ADMIN ENDPOINTS
#################

@app.route('/addBuildingToDB')
def addBuildingToDB():
    #Get a building information from an admin and add the building to the database

@app.route('/getLoggedInUsers')
def getLoggedInUsers():
    #Send a list logged in users to admin

@app.route('/getPeopleByBuilding')
def getPeopleByBuilding():
    #Send a list of users in specific building

@app.route('/getUserHistory')
def getUserHistory():
    #Send a list of exchanged messages and movements by users

@app.route('/getMessagesByBuilding')
def getMessagesByBuilding():
    #Send a list of messages all exchanged in a specific building

###############
# BOT ENDPOINTS
###############

@app.route('/broadcastBotMessage')
def broadcastBotMessage():
    #Get a message from a bot and broadcast it to users inside the building associated to the bot