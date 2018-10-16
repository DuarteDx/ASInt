import Pyro4

def lookup(name):
    ns = Pyro4.locateNS(host="193.136.128.104", port=9090)
    uri = ns.lookup(name)
    print("Server name: " + str(uri))
    return Pyro4.Proxy(uri)

