import DB, user, message
from math import sin, cos, sqrt, atan2, radians

def broadcastMessage(db, senderID, name, content):
    message = db.addMessage(senderID, content)
    nearbyUsers = db.getUsersInRange(senderID)
    for user in nearbyUsers:
        db.sendMessage(senderID, name, user["id"], content)



def getDistanceBetween2Points(lat1, lon1, lat2, lon2):
    # approximate radius of earth in m
    R = 6373000.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c
            