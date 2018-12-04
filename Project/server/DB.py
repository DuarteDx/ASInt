import pickle
from building import building
from message import message
from user import user

class DB:
    def __init__(self):
        self.buildings = dict()
        self.messages = list()
        self.users = dict()
    
        '''try:
            #f = open('bd_dump'+name, 'rb')
            #self.bib = pickle.load(f)
            #f.close()
        except IOError:
            self.bib = {}'''

    def addBuilding(self, id_, name, latitude, longitude):
        build = building(id_, name, latitude, longitude)
        self.buildings[build.id] = build

    def addMessage(self, senderID, content):
        latitude, longitude, rang = self.getUserLocation(senderID)
        mess = message(senderID, latitude, longitude, rang, content)
        self.messages.append(mess)

    def addUser(self, userID, name, latitude=0, longitude=0, rang=10):
        if userID not in self.users.keys():
            new_user = user(userID, name, latitude, longitude, rang)
            self.users[userID] = new_user               

    def getUserLocation(self, userID):
        la = self.users[userID].latitude
        lo = self.users[userID].longitude
        ra = self.users[userID].range
        return la, lo, ra

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