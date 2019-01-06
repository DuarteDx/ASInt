import requests
import json

serverURL = 'http://127.0.0.1:5000/bot/'

def makePostRequest(url, data):
    headers = {'Content-Type': 'application/json'}
    S = requests.session() # ToDo: test without this line (and edit next line)
    r = S.post(url, headers=headers, json=data)
    return r

def sendRegisterMessage(buildingId, botName):
    url = serverURL + 'register'
    data = {'buildingID':buildingId, 'botName':botName}
    resp = makePostRequest(url, data)
    return resp

def sendBroadcastMessage(botName, message):
    url = serverURL + 'broadcastMessage'
    data = {'botName':botName, 'message':message}
    makePostRequest(url, data)
    return 'Sent message: ' + message