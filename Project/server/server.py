from flask import Flask
from flask import redirect
from flask import request
from flask import jsonify

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