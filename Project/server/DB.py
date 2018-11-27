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

    def addBuilding(self, id, name, latitude, longitude):
        build = building(id, name, latitude, longitude)
        self.buildings[build.id] = build

    def addMessage(self, id_, time_, latitude, longitude, rang, building, senderID, content):
        mess = message(id_, time_, latitude, longitude, rang, building, senderID, content)
        self.messages.append(mess)

    def getMessagesFromUser(self, userID):
        mList = list()
        for m in self.messages:
            if m.senderID == userID:
                mList.append(m)
        return mList

    def addUser(self, userID, name, latitude, longitude, rang):
        new_user = user(userID, name, latitude, longitude, rang)
        self.users[userID] = new_user

    def updateUser(self, userID, latitude=None, longitude=None, rang=None):
        if latitude != None and longitude != None:
            self.users[userID].updateLocation(latitude, longitude)
        if rang != None:
            self.users[userID].updateRange(range)