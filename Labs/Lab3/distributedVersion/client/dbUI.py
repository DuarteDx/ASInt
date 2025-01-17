class dbUI:

    def __init__(self, db):
        self.bookDB = db

    def readInput(self):

        action = input("Action (NEW, SHOW, AUTHORS, SEARCH_AUTH, SEARCH_YEAR, EXIT): ")

        if action == "NEW":
            author = input("Author name: ")
            title = input("Book title: ")
            publicationYear = input("Publication year: ")
            self.bookDB.insertBook(author, title, publicationYear)

        elif action == "SHOW":
            id = input("Book id: ")
            print(self.bookDB.showBook(id))

        elif action == "AUTHORS":
            print(self.bookDB.listAllAuthors())

        elif action == "SEARCH_AUTH":
            author = input("Author name: ")
            print(self.bookDB.listBooksFromAuthor(author))

        elif action == "SEARCH_YEAR":
            year = input("Year: ")
            print(self.bookDB.listBooksFromYear(year))

        elif action == "EXIT":
            return 0