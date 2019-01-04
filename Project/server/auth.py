import secrets
import hashlib

admins = {'admin': 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'pato':'a5e7c002443743c5836758c7d1cd8ddefd9fcf2061daa0efaac683fb99966057', 'dias':'079cc69d06f2eb3c8cf397d5a5b5f2e5df04edb68d6a8afdf58d35c7ef22d165'}
activeTokens = list() 

def generateToken():
    token = secrets.token_urlsafe() 
    activeTokens.append(token)
    return token

def verifyPassword(password, stored_hash):
    pw_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    if pw_hash == stored_hash:
        return True
    return False

def checkToken(token):
    if token in activeTokens:
        # TODO check Token time
        # if expired, delete token
        return True
    return False
