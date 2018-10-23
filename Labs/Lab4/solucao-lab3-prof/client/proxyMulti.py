#!/usr/bin/env python

import Pyro4


class proxyMulti:
    
    def __init__(self, hostNS, portNS):        
        ns = Pyro4.locateNS(host=hostNS, port=portNS)        
        d = ns.list('BookDB-80931')
        uriList = list(d.values())
        print(uriList)
        print()
        
        self.dbList = []
        for uri in uriList:
                self.dbList.append(Pyro4.Proxy(uri))

    def addbook(self, author, title, year):
        self.dbList[1].addBook(author, title, year)

    def showBook(self, b_id):
        for db in self.dbList:
            db.showBook(b_id)
    
    def listAllBooks(self):
        for db in self.dbList:
            db.listAllBooks()

    def listBooksAuthor(self, authorName):
        for db in self.dbList:
            db.listBooksAuthor(authorName)

    def listBooksYear(self, year):
        for db in self.dbList:
            db.listBooksYear(year)
    

    


