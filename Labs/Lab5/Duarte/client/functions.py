import Pyro4

def lookup(name):
    ns = Pyro4.locateNS(host="193.136.128.108", port=9090)
    uri = ns.lookup(name)
    print("Server name: " + str(uri))
    return Pyro4.Proxy(uri)

def listServers():
    serverNameList = []
    # Connect to name server
    ns = Pyro4.locateNS(host="193.136.128.108", port=9090)

    # Get dictionary of available and valid servers in name server
    # Only gets servers whose names start with 'BookDB'
    d = ns.list('BookDB-')
    
    # Print valid servers
    for name in d:
        print(name)
        serverNameList.append(name)

    return serverNameList
