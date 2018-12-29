import time
import ajaxFunctions
import csv

def addBuildingOption():
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

        latitude = input('Latitude of center of building: ')
        if latitude == 'q':
            return 1

        longitude = input('Longitude of center of building: ')
        if longitude == 'q':
            return 1

        #Send new building data to server
        ajaxFunctions.addBuilding(buildingID, buildingName, latitude, longitude)

    # Import multiple buildings from file in csv format
    elif inputMethod == '2':
        filename = input('Insert file name (without .txt extension): ')
        filepath = 'files/' + filename + '.txt'
        with open(filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                ajaxFunctions.addBuilding(row[0], row[1], row[2], row[3])
    
    return 1

def listUsersByBuildinOption():
    print('Insert building id')
    buildingId = input('Building id: ')

    usersList = ajaxFunctions.getUsersInBuilding(buildingId)

    # ToDo: Do some parsing to the usersList

    print('Users in building with id ' + buildingId + ':')
    for user in usersList:
        print(user)

def listHistoryOption():
    print('Search by: user(1), building(2), user and building(3)')
    option = input('Select a number: ')

    userId = 'None'
    buildingId = 'None'

    if option == '1' or option == '3':
        userId = input('Insert user id: ')

    if option == '2' or option == '3':
        buildingId = input('Insert building id: ')

    historyList = ajaxFunctions.getHistory(userId, buildingId)

    print('\nServer history:')
    for log in historyList:
        print(log)

def showMenu():
    print('\nSelect an operation (write number)')
    print('1 - Add building')
    print('2 - List currently logged in users')
    print('3 - List users inside a certain building')
    print('4 - List history by user or building')

    operation = input('>')

    if operation == '1':
        addBuildingOption()
        return 1
    elif operation == '2':
        ajaxFunctions.listLoggedInUsersOption()
        return 2
    elif operation == '3':
        listUsersByBuildinOption()
        return 3
    elif operation == '4':
        listHistoryOption()
        return 4
    else:
        print('Invalid input, try again!')

def loadingAnimation():
    print('.')
    time.sleep(0.3)
    print('..')
    time.sleep(0.3)
    print('...')
    time.sleep(0.3)