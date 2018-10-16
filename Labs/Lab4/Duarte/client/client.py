#!/usr/bin/env python

import Pyro4
import dbUI
import functions


Pyro4.config.SERIALIZER = 'pickle'

def main():
        name = input('Insert server name: ')
        db = functions.lookup(name)

        print(db)
        
        ui = dbUI.dbUI(db)
        ui.menu()

if __name__=="__main__":
        main() 
