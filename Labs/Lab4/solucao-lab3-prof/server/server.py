#!/usr/bin/env python

import Pyro4
import bookDB

Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')

def main():
        remoteLibrary = Pyro4.expose(bookDB.bookDB)

        db = bookDB.bookDB("mylib")

        daemon = Pyro4.Daemon()

        ns = Pyro4.locateNS(host="193.136.128.108", port=9090)
        print (ns)

        try:
                ns.createGroup(':libraries')
        except:
                pass

        uri = daemon.register(db, "BookDB7")
        ns.register("BookDB7", uri)

        try:
                daemon.requestLoop()
        finally:
                daemon.shutdown(True)

if __name__=="__main__":
        main() 
