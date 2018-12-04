from math import sin, cos, sqrt, atan2, radians


def getDistanceBetween2Points(lat1, lon1, lat2, lon2):
    # approximate radius of earth in m
    R = 6373000.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def getUsersInRange(db, lat, lon, rang):
    usersInRange = list()
    for userID in db.users.keys():
        userLat, userLong = db.getUserLocation(userID)
        if getDistanceBetween2Points(lat, lon, userLat, userLong) < rang:
            usersInRange.append(userID, db.users[userID].name)
            