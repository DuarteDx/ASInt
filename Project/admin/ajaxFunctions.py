import requests
import json

serverURL = 'http://127.0.0.1:5000/admin'

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

def adminLogin(username, password):
    url = serverURL + '/login'
    data = {'user':username, 'password':password}
    response = makePostRequest(url, data)
    # check if response is positive
    # TODO extract and return the token
    return response.content['token']


def addBuilding(buildingID, buildingName, latitude, longitude, token):
    #Make ajax call to server
    url = serverURL + '/addBuildingToDB'
    data = {'buildingID':buildingID, 'buildingName':buildingName, 'latitude':latitude, 'longitude':longitude, 'token':token}
    print('Sending data: ' + str(data))
    makePostRequest(url, data)

def listLoggedInUsersOption(token):
    url = serverURL + '/getLoggedInUsers'
    print('Asking server for list of logged in users...')
    data = {'token': token}
    response = makePostRequest(url, data)
    response = json.loads(response)
    print(response['userID'])

def getUsersInBuilding(buildingId, token):
    url = serverURL + '/getUsersInBuilding'
    print('Asking server for list of users in building...')
    data = {'buildingID':buildingId, 'token':token}
    response = makePostRequest(url, data)
    response = json.loads(response)
    return response

def getHistory(userId, buildingId, token):
    url = serverURL + '/getHistory'
    print('Asking server for history...')
    data = {'userID':userId, 'buildingID':buildingId, 'token':token}
    response = makePostRequest(url, data)
    response = json.loads(response)
    return response
