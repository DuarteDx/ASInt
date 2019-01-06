import DB, user, message
from math import sin, cos, sqrt, atan2, radians

# sends a message to all users inside the range of sender
def broadcastMessage(db, senderID, name, content):
    # db.addLog(senderID, "aa", "message", content)
    nearbyUsers = db.getUsersInRange(senderID)
    for user in nearbyUsers:
        db.sendMessage(name, user["id"], content)
        # add message log to all buildings user is inside of 
        builds = db.getBuildingsFromUser(senderID)
        if not builds:
            db.addLog(senderID, "None", "message", content)
        else:
            for b in builds:
                db.addLog(senderID, b, "message", content)

# send message from bot to all users inside its building
def broadcastBotMessage(db, botName, content):
    buildingID = db.getBuildingFromBot(botName)
    recipients = getUsersInBuilding(db, buildingID)
    if recipients:
        for recv in recipients:
            db.sendMessage(botName, recv, content)
            db.addLog(botName, buildingID, "message", content)


# returns the list of user IDs that are inside buildingID
def getUsersInBuilding(db, buildingID):
    if buildingID not in db.buildings:
        return None
    return db.getUsersInBuilding(buildingID)

# checks if userID is in range of buildingID
def inRange(db, uLat, uLong, buildingID):
    # returns true if closer than 10m to building centre
    bLat, bLong = db.getBuildingLocation(buildingID)
    if getDistanceBetween2Points(uLat, uLong, bLat, bLong) < 20:
        return True
    else:
        return False

# computes geographical distance between 2 locations
def getDistanceBetween2Points(lat1, lon1, lat2, lon2):
    # approximate radius of earth in m
    R = 6373000.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c
            