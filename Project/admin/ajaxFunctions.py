import requests
import json

serverURL = 'http://127.0.0.1:5000'

def makePostRequest(url, data):
    headers = {'Content-Type': 'application/json'}
    S = requests.session()
    r = S.post(url, headers=headers, json=data)
    print(r.status_code, r.reason)
    return r

def addBuilding(buildingID, buildingName, latitude, longitude):
    #Make ajax call to server
    url = serverURL + '/addBuildingToDB'
    data = {'buildingID':buildingID, 'buildingName':buildingName, 'latitude':latitude, 'longitude':longitude}
    print('Sending data: ' + str(data))
    makePostRequest(url, data)