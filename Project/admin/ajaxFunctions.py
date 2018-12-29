import requests
import json

serverURL = 'http://127.0.0.1:5000'

def makePostRequest(url, data):
    headers = {'Content-Type': 'application/json'}
    S = requests.session() # ToDo: test without this line (and edit next line)
    r = S.post(url, headers=headers, json=data)
    print(r.status_code, r.reason)
    return r

def makeGetRequest(url):
    r = requests.get(url)
    #print(r.status_code, r.reason)
    #print(r.content)
    return r.content


def addBuilding(buildingID, buildingName, latitude, longitude):
    #Make ajax call to server
    url = serverURL + '/addBuildingToDB'
    data = {'buildingID':buildingID, 'buildingName':buildingName, 'latitude':latitude, 'longitude':longitude}
    print('Sending data: ' + str(data))
    makePostRequest(url, data)

def listLoggedInUsersOption():
    url = serverURL + '/getLoggedInUsers'
    print('Asking server for list of logged in users...')
    response = makeGetRequest(url)
    response = json.loads(response)
    print(response['userID'])

def getUsersInBuilding(buildingId):
    url = serverURL + '/getUsersInBuilding'
    print('Asking server for list of users in building...')
    data = {'buildingID':buildingId}
    response = makePostRequest(url, data)
    response = json.loads(response)
    return response

def getHistory(userId, buildingId):
    url = serverURL + '/getHistory'
    print('Asking server for history...')
    data = {'userID':userId, 'buildingID':buildingId}
    response = makePostRequest(url, data)
    response = json.loads(response)
    return response
