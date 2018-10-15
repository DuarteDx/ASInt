import dbUI
import Pyro4

# Get URI 
uri = input("DB Port Number: ")
uri = "PYRO:db@localhost:" + uri
print(uri)

# Get proxy for remote object
db = Pyro4.Proxy(uri)

print("Received db:\n")
print(str(db))

# Call methods and access attributes
ui = dbUI.dbUI(db)

while True:
    if ui.readInput() == 0:
        break