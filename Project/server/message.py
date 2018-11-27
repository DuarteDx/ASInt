class message:
    def __init__(self, id_, time, latitude, longitude, rang, building, senderID, content):
        self.id = id_
        self.time = time
        self.latitude = latitude
        self.longitude = longitude
        self.range = rang
        self.building = building
        self.senderID = senderID
        self.content = content

    def __str__(self):
        return "%d - %s - %s - %s\n%s" % (self.id, self.time, self.building, self.senderID, self.content)
