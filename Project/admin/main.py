
loggedIn = False

while not loggedIn:

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "123":
        print("You are logged in!")
        loggedIn = True
    else:
        print("Ups, invalid credencials...\n")

print("Admin zone...")

#def showMenu():
