class Bot:
    def __init__(self, name, buildingID):
        self.name = name
        self.buildingID = buildingID

    def __str__(self):
        return "BOT: %s is at building %s" % (self.name, self.buildingID)