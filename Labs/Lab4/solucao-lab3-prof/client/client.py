#!/usr/bin/env python

import Pyro4
import dbUI
import proxyMulti


Pyro4.config.SERIALIZER = 'pickle'

def main():
        pm = proxyMulti.proxyMulti("193.136.128.108", 9090)
        ui = dbUI.dbUI(pm)
        ui.menu()

if __name__=="__main__":
        main() 
