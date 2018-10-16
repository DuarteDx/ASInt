#!/usr/bin/env python

import Pyro4
import bookDB

Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')

def main():
        remoteLibrary = Pyro4.expose(bookDB.bookDB)

        db = bookDB.bookDB("mylib")

        daemon = Pyro4.Daemon(host="194.210.229.61")

        # Localiza o Name Server
        ns = Pyro4.locateNS(host="193.136.128.104", port=9090)
        print (ns)

        try:
                ns.createGroup(':libraries')
        except:
                pass

        # Regista a base de dados do servidor no Name Server
        uri = daemon.register(db, "BookDB-80931")
        ns.register("BookDB-80931", uri)

        try:
                daemon.requestLoop()
        finally:
                daemon.shutdown(True)

if __name__=="__main__":
        main() 
