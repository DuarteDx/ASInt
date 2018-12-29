import pickle
import time
from building import Building
from message import Message
from user import User
import functions

class DB:
    def __init__(self):    
        try:
            f = open('users_dump', 'rb')
            self.users = pickle.load(f)
            f.close()
        except IOError:
            self.users = dict()
        try:
            f = open('buildings_dump', 'rb')
            self.buildings = pickle.load(f)
            f.close()
        except IOError:
            self.buildings = dict()
        try:
            f = open('logs.pkl', 'rb')
            self.logs = pickle.load(f)
            f.close()
        except:
            self.logs = list()


    ########################################
    ##              Users                 ##
    ########################################

    # gets name of the user from its ID
    def getNameFromID(self, userID):
        if userID not in self.users.keys():
            return None
        return self.users[userID].name         

    # adds new user to database
    def addUser(self, userID, name, latitude=0, longitude=0, rang=10):
        if userID not in self.users.keys():
            new_user = User(userID, name, latitude, longitude, rang)
            self.users[userID] = new_user
            f = open('users_dump', 'wb')
            pickle.dump(self.users, f)
            f.close()   

    # returns list of all user IDs
    def getAllUsers(self):
        userList = list()
        for usr in self.users:
            userList.append(self.users[usr].id)
        return userList

    # returns user latitude, longitude and range
    def getUserLocation(self, userID):
        la = self.users[userID].latitude
        lo = self.users[userID].longitude
        ra = self.users[userID].range
        return la, lo, ra

    # get buildings user is inside of
    def getBuildingsFromUser(self, userID):
        return self.users[userID].buildings

    # returns list of userID's and userName's in range of senderID
    def getUsersInRange(self, senderID):
        lat, lon, rang = self.getUserLocation(senderID)
        usersInRange = list()
        for userID in self.users.keys():
            userLat, userLong, _ = self.getUserLocation(userID)
            if functions.getDistanceBetween2Points(lat, lon, userLat, userLong) < int(rang):
                usersInRange.append({'id':userID, 'userName':self.users[userID].name})
        return usersInRange

    # adds a message to messsage queue of receiverID
    def sendMessage(self, senderID, senderName, receiverID, message):
        self.users[receiverID].addMessageToQueue(senderID, senderName, message)

    # updates user location or range or both
    def updateUser(self, userID, latitude=None, longitude=None, rang=None):
        if userID not in self.users.keys():
            return
        # update location
        if latitude != None and longitude != None:
            self.users[userID].updateLocation(latitude, longitude)
            # update user location
            for b in self.buildings:
                if functions.inRange(self, userID, b):      # user is inside building b
                    if b not in self.users[userID].buildings:   # user was not already inside b
                        print("User " + str(userID) + " entered building " + str(b)) 
                        self.users[userID].buildings.append(b)
                        self.addLog(userID, b, "move", "entered")
                else:                                       # user is no inside building b
                    if b in self.users[userID].buildings:   # user was inside building b
                        print("User " + str(userID) + " left building " + str(b))
                        self.users[userID].buildings.remove(b)
                        self.addLog(userID, b, "move", "left")
        # update range
        if rang != None:
            self.users[userID].updateRange(rang)


    ########################################
    ##             Buildings              ##
    ########################################
    
    # adds new building to DB
    def addBuilding(self, id_, name, latitude, longitude):
        if id_ not in self.buildings:
            build = Building(id_, name, float(latitude), float(longitude))
            self.buildings[build.id] = build
            f = open('buildings_dump', 'wb')
            pickle.dump(self.buildings, f)
            f.close()

    # gets building latitude and longitude
    def getBuildingLocation(self, buildingID):
        if buildingID in self.buildings:
            return self.buildings[buildingID].latitude, self.buildings[buildingID].longitude
        else:
            return 0, 0             
    

    ########################################
    ##              Logs                  ##
    ########################################

    # creates a new log and adds it to logs
    # log: userID, building, timestamp, type: ["move"/"message"], data: ["entered"/"left"/message content] 
    def addLog(self, userID, building, type_, data):
        log = {'userID':userID, 'building':building, 'timestamp':time.time(), 'type':type_, 'data':data}
        self.logs.append(log)

    def printLogs(self):
        print(self.logs)

    # returns a list of logs from userID or in buildingID
    def retrieveLogs(self, userID = None, building = None):
        logList = list()
        for log in self.logs:
            if (userID == None or log['userID'] == userID) and (building == None or log['building'] == building):
                logList.append(log)
        return logList

  

