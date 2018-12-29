class Building:
    def __init__(self, id_, name, latitude, longitude):
        self.id = id_
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return "%d - %s - %f - %f" % (self.id, self.name, self.latitude, self.longitude)

