#!/usr/bin/env python

import Pyro4
import dbUI
import functions


Pyro4.config.SERIALIZER = 'pickle'

def main():
        serverNameList = functions.listServers()
        '''
        print('Select option(connect, all): ')
        option1 = input('> ')
        print(option1)
        
        if option1 == 'connect':
                bookName = input('Select server name: ')
                db = functions.lookup(bookName)

        elif option1 == 'all':
                for serverName in serverNameList:
                        if '4028' not in serverName \
                        and '3000' not in serverName \
                        and '81074' not in serverName:
                                db = functions.lookup(serverName)
                                b_list = db.listAllBooks()
                                for b in b_list:
                                        print(b)
        '''

        name = input('Insert server name: ')
        db = functions.lookup(name)

        print(db)
        
        ui = dbUI.dbUI(db)
        ui.menu()

if __name__=="__main__":
        main() 
