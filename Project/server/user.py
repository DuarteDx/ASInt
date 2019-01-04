import time
from flask import jsonify

class User:
    def __init__(self, userID, name, latitude, longitude, rang):
        self.id = userID
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.range = rang
        self.lastUpdate = time.time()
        self.messageQueue = list()
        self.buildings = list()         # list of building IDs user is inside of
        # o prof escreveu:
        # pubsub.send(msg, topic=dest) para o caso de publish-subscribe

    def addMessageToQueue(self, senderName, content):
        self.messageQueue.insert(0,{'sender':senderName, 'content':content})

    def readMessages(self):
        return self.messageQueue

    def updateLocation(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.lastUpdate = time.time()

    def updateRange(self, rang):
        self.range = int(rang)
        self.lastUpdate = time.time()

    def __str__(self):
        return "USER: %d - %s - %f - %f - %d" % (self.id, self.name, self.latitude, self.longitude, self.range)
