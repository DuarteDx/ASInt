import pickle
from building import building
from message import message
from user import user
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
            f = open('messages_dump', 'rb')
            self.messages = pickle.load(f)
            f.close()
        except IOError:
            self.messages = list()

    def addBuilding(self, id_, name, latitude, longitude):
        build = building(id_, name, latitude, longitude)
        self.buildings[build.id] = build
        f = open('buildings_dump', 'wb')
        pickle.dump(self.buildings, f)
        f.close()               

    def addMessage(self, senderID, content):
        latitude, longitude, rang = self.getUserLocation(senderID)
        mess = message(senderID, latitude, longitude, rang, content)
        self.messages.append(mess)
        f = open('messages_dump', 'wb')
        pickle.dump(self.messages, f)
        f.close()               

    def addUser(self, userID, name, latitude=0, longitude=0, rang=10):
        if userID not in self.users.keys():
            new_user = user(userID, name, latitude, longitude, rang)
            self.users[userID] = new_user
            f = open('users_dump', 'wb')
            pickle.dump(self.users, f)
            f.close()               

    def getUserLocation(self, userID):
        la = self.users[userID].latitude
        lo = self.users[userID].longitude
        ra = self.users[userID].range
        return la, lo, ra
    
    def getUsersInRange(self, senderID):
        lat, lon, rang = self.getUserLocation(senderID)
        usersInRange = list()
        for userID in self.users.keys():
            userLat, userLong, r_ = self.getUserLocation(userID)
            if functions.getDistanceBetween2Points(lat, lon, userLat, userLong) < rang:
                usersInRange.append((userID, self.users[userID].name))
        return usersInRange

    def getUserHistory(self, userID):
        return self.users[userID].locationHistory

    def getMessagesFromUser(self, userID):
        mList = list()
        for m in self.messages:
            if m.senderID == userID:
                mList.append(m)
        return mList

    def updateUser(self, userID, latitude=None, longitude=None, rang=None):
        if userID not in self.users.keys():
            return
            #addUser(userID, latitude)

        if latitude != None and longitude != None:
            self.users[userID].updateLocation(latitude, longitude)
        if rang != None:
            self.users[userID].updateRange(range)