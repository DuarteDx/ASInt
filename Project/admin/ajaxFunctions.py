import requests

serverURL = 'http://127.0.0.1:5000'

def makePostRequest(url, data):
    response = requests.post(url, data)
    return response

def addBuilding(buildingID, buildingName, latitude, longitude):
    #Make ajax call to server
    url = serverURL + '/addBuildingToDB'
    data = {'buildingID':buildingID, 'buildingName':buildingName, 'latitude':latitude, 'longitude':longitude}
    makePostRequest(url, data)