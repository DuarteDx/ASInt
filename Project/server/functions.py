import DB, user, message
from math import sin, cos, sqrt, atan2, radians

# sends a message to all users inside the range of sender
def broadcastMessage(db, senderID, name, content):
    db.addLog(senderID, "aa", "message", content)
    nearbyUsers = db.getUsersInRange(senderID)
    for user in nearbyUsers:
        db.sendMessage(senderID, name, user["id"], content)
        # add message log to all buildings user is inside of 
        builds = db.getBuildingsFromUser(senderID)
        for b in builds:
            db.addLog(senderID, b, "message", content)

# returns the list of user IDs that are inside buildingID
def getUsersInBuilding(db, buildingID):
    userList = list()
    for user in db.users:           # check every user
        if buildingID in db.getBuildingsFromUser(user):       # check if user is inside buildingID
            if user not in userList:     # check if user already in the list
                userList.append(user)
    return userList

# checks if userID is in range of buildingID
def inRange(db, userID, buildingID):
    # returns true if closer than 10m to building centre
    uLat, uLong, _ = db.getUserLocation(userID)
    bLat, bLong = db.getBuildingLocation(buildingID)
    if getDistanceBetween2Points(uLat, uLong, bLat, bLong) < 10:
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
            