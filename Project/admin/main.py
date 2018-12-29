import menuFunctions

loggedIn = False

while not loggedIn:

    username = input("Username: ")
    password = input("Password: ")

    menuFunctions.loadingAnimation()

    if username == "admin" and password == "123":
        print("You are logged in!")
        loggedIn = True
    else:
        print("Ups, invalid credencials...\n")

while True:
    menuFunctions.showMenu()