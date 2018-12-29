import menuFunctions
import getpass
from ajaxFunctions import adminLogin

loggedIn = False

while not loggedIn:
    username = input("Username: ")  # admin
    password = getpass.getpass('Password: ') # 123
    menuFunctions.loadingAnimation()
    token = adminLogin(username, password)
    if token:
        print("Login successful!")
        loggedIn = True
    else:
        print("Login failed. Wrong credentials.")

while True:
    menuFunctions.showMenu(token)