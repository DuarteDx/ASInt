class message:
    def __init__(self, senderID, latitude, longitude, rang, content):
        self.senderID = senderID
        self.latitude = latitude
        self.longitude = longitude
        self.range = rang
        self.content = content

    def __str__(self):
        return "%s - %f - %f - %d:\n%s\n" % (self.senderID, self.latitude, self.longitude, self.range, self.content)
