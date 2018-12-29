import secrets
import hashlib

admins = {'admin': 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'pato':'boss', 'dias':'paneleiro'}
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
        return True
    return False
