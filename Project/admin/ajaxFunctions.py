import requests
import json

serverURL = 'http://127.0.0.1:5000/admin'

def makePostRequest(url, data):
    headers = {'Content-Type': 'application/json'}
    S = requests.session() # ToDo: test without this line (and edit next line)
    r = S.post(url, headers=headers, json=data)
    return r

def makeGetRequest(url):
    r = requests.get(url)
    return r.content

def adminLogin(username, password):
    url = serverURL + '/login'
    data = {'user':username, 'password':password}
    response = makePostRequest(url, data)
    # check if response is positive
    if "Wrong" in str(response.content):
        return False
    return json.loads(response.content)['sessionToken']

def addBuilding(buildingID, buildingName, latitude, longitude, token):
    #Make ajax call to server
    url = serverURL + '/addBuildingToDB'
    data = {'buildingID':buildingID, 'buildingName':buildingName, 'latitude':latitude, 'longitude':longitude, 'token':token}
    # print('Sending data: ' + str(data))
    response = makePostRequest(url, data)
    if "Received" in str(response.content):
        print("Added building to database")

def listLoggedInUsersOption(token):
    url = serverURL + '/getLoggedInUsers'
    data = {'token': token}
    response = makePostRequest(url, data)
    print('Logged in users: ')
    print(json.loads(response.content)['userID'])

def getUsersInBuilding(buildingId, token):
    url = serverURL + '/getUsersInBuilding'
    data = {'buildingID':buildingId, 'token':token}
    response = makePostRequest(url, data)
    response = json.loads(response.content)
    return response

def getHistory(userId, buildingId, token):
    url = serverURL + '/getHistory'
    data = {'userID':userId, 'buildingID':buildingId, 'token':token}
    response = makePostRequest(url, data)
    response = json.loads(response.content)
    return response
