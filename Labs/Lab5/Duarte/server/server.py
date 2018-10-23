#!/usr/bin/env python

import Pyro4
import bookDB

Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')

def main():
        remoteLibrary = Pyro4.expose(bookDB.bookDB)

        db = bookDB.bookDB("mylib")

        # Run ipconfig to get this machine's IPv4 address
        daemon = Pyro4.Daemon(host="194.210.228.147")

        ns = Pyro4.locateNS(host="193.136.128.108", port=9090)
        print (ns)

        try:
                ns.createGroup(':libraries')
        except:
                pass

        uri = daemon.register(db, "BookDB-81356")
        ns.register("BookDB-81356", uri)

        try:
                daemon.requestLoop()
        finally:
                daemon.shutdown(True)

if __name__=="__main__":
        main() 
