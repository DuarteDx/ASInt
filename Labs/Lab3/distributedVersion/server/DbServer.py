import bookDB
import book
import Pyro4

# From 05-A-Pyro.pdf, slide 5 & 6
# Create a class to expose to client
exposedBookDB = Pyro4.expose(bookDB.bookDB)

# Start daemon PYRO4
daemon = Pyro4.Daemon()

# Create the object
dbObject = exposedBookDB()

# Make object available
uri = daemon.register(dbObject, 'db')

print(uri)

# Start request loop
daemon.requestLoop()