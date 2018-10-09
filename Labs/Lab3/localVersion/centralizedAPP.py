import book
import bookDB
import dbUI
import pickle

try:
    f = open("bookDatabase.pickle", "rb")
    oldData = pickle.load(f)
    bookDB = bookDB.bookDB()
    bookDB.books = oldData['books']
    bookDB.currentId = oldData['currentId']
    print(bookDB)
    f.close()
except:
    bookDB = bookDB.bookDB()

dbUI = dbUI.dbUI(bookDB)

while True:
    if dbUI.readInput() == 0:
        break