class Building:
    def __init__(self, id, name, latitude, longitude):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.usersInside = list()

    def getUsersInside(self):
        return self.usersInside

    def addUserToList(self, userID):
        self.usersInside.append(userID)

    def removeUserFromList(self, userID):
        if userID in self.usersInside:
            self.usersInside.remove(userID)

    def __str__(self):
        return "%d - %s - %f - %f" % (self.id, self.name, self.latitude, self.longitude)

