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

    def addMessage(self, id_, time_, latitude, longitude, rang, building, senderID, content):
        mess = message(id_, time_, latitude, longitude, rang, building, senderID, content)
        self.messages.append(mess)

    def addUser(self, userID, name, latitude, longitude, rang):
        if userID not in self.users.keys():
            new_user = user(userID, name, latitude, longitude, rang)
            self.users[userID] = new_user
        else:
            self.updateUser(userID, latitude, longitude, rang)                

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