import time
import ajaxFunctions
import csv



def addBuildingOption(token):
    print('Press "q" at any moment to cancel')

    print('Insert single building(1) or file(2)?')
    inputMethod = input('Insert number: ')

    # Insert a single building manually
    if inputMethod == '1':
        #Get parameters
        buildingID = input('Building id: ')
        if buildingID == 'q':
            return 1

        buildingName = input('Building name: ')
        if buildingName == 'q':
            return 1

        latitude = input('Latitude: ')
        if latitude == 'q':
            return 1

        longitude = input('Longitude: ')
        if longitude == 'q':
            return 1

        #Send new building data to server
        ajaxFunctions.addBuilding(buildingID, buildingName, latitude, longitude, token)

    # Import multiple buildings from file in csv format
    elif inputMethod == '2':
        filename = input('Insert file name (without .txt extension): ')
        filepath = 'files/' + filename + '.txt'
        with open(filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                ajaxFunctions.addBuilding(row[0], row[1], row[2], row[3], token)
    else:
        print("Wrong input method, should be 1 or 2")
        addBuildingOption(token)
    return

def listUsersByBuildinOption(token):
    print('Insert building id')
    buildingId = input('Building id: ')
    usersList = ajaxFunctions.getUsersInBuilding(buildingId, token)
    # ToDo: Do some parsing to the usersList
    print('Users in building with id ' + buildingId + ' :')
    if usersList:
        for user in usersList:
            print(user)
    else:
        print("none")

def listHistoryOption(token):
    print('Search by: user(1), building(2), user and building(3), any user or building(4)')
    option = input('Select a number: ')

    userId = 'None'
    buildingId = 'None'

    if option == '1' or option == '3':
        userId = input('Insert user id: ')
    if option == '2' or option == '3':
        buildingId = input('Insert building id: ')
    logs = ajaxFunctions.getHistory(userId, buildingId, token)
    print('\nServer logs:')
    for log in logs:
        print(log)

def showMenu(token):
    print('\nSelect an operation (write number)')
    print('1 - Add building')
    print('2 - List currently logged in users')
    print('3 - List users inside a certain building')
    print('4 - List history by user or building')
    print('exit - Close app')

    operation = input('>')

    if operation == '1':
        addBuildingOption(token)
    elif operation == '2':
        ajaxFunctions.listLoggedInUsersOption(token)
    elif operation == '3':
        listUsersByBuildinOption(token)
    elif operation == '4':
        listHistoryOption(token)
    elif operation.lower() == 'exit' or operation == 'q':
        quit()
    else:
        print('Invalid input, try again!')

def loadingAnimation():
    print('.')
    time.sleep(0.1)
    print('..')
    time.sleep(0.1)
    print('...')
    time.sleep(0.1)