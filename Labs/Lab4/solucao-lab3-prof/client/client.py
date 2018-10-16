#!/usr/bin/env python

import Pyro4
import dbUI


Pyro4.config.SERIALIZER = 'pickle'

def main():
        ns = Pyro4.locateNS(host="193.136.128.104", port=9090)
        uri = ns.lookup('BookDB')
        
        db = Pyro4.Proxy(uri)
        d = ns.list()
        uriList = list(d.values())


        
        ui = dbUI.dbUI(db)
        ui.menu()

if __name__=="__main__":
        main() 
