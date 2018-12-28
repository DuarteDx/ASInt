import time
import ajaxFunctions

def addBuildingOption():
    print('Press "q" at any moment to cancel')

    #print('Insert single building(1) or file(2)?')
    #inputMethod = input('Insert number: ')

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

    #if inputMethod == 2:


    #Send new building data to server
    ajaxFunctions.addBuilding(buildingID, buildingName, latitude, longitude)
    
    return 1

def showMenu():
    print('Select an operation (write number)')
    print('1 - Add building')
    print('2 - List currently logged in users')
    print('3 - List users inside a certain building')
    print('4 - List history by user or building')

    operation = input('>')

    if operation == '1':
        addBuildingOption()
        return 1
    elif operation == '2':
        #listLoggedInUsersOption()
        return 2
    elif operation == '3':
        #listUsersByBuildinOption()
        return 3
    elif operation == '4':
        #listHistoryOption()
        return 4
    else:
        print('Invalid input, try again!')

def loadingAnimation():
    print('.')
    #time.sleep(1)
    print('..')
    #time.sleep(1)
    print('...')
    #time.sleep(1)