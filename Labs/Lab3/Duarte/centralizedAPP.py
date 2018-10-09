class book:

    def __init__(self, author, title, publicationYear, id):
        self.author = author
        self.title = title
        self.publicationYear = publicationYear
        self.id = id
    
class bookDB:

    def __init__(self):
        self.currentId = 0
        self.books = []

    def insertBook(self, author, title, publicationYear):
        """Inserts book into database"""
        newBook = book(author, title, publicationYear, self.currentId)
        self.books.append(newBook.__dict__)
        self.currentId += 1

    def showBook(self, id):
        """Shows book information given an id"""
        id = int(id)
        if id < len(self.books):
            print("Author: " + self.books[id]['author'])
            print("Title: " + self.books[id]['title'])
            print("Publication year: " + self.books[id]['publicationYear'])
        else:
            print("Ups, looks like that book isn't in the database")

    def listAllAuthors(self):
        """Displays all authors in database"""
        for book in self.books:
            print(book['author'])

    def listBooksFromAuthor(self, author):
        """Displays books from a given author"""
        booksByAuthor = []
        for book in self.books:
            if book['author'] == author:
                booksByAuthor.append(book['title'])
        if len(booksByAuthor) == 0:
            print("Looks like there are no books from that author")
        else:
            print(booksByAuthor)

    def listBooksFromYear(self, year):
        """Displays books published in a given year"""
        booksByYear = []
        for book in self.books:
            if book['publicationYear'] == year:
                booksByYear.append(book['title'])
        if len(booksByYear) == 0:
            print("Looks like there are no books from that year yet")
        else:
            print(booksByYear)

class dbUI:

    def readInput(self):

        action = input("Action (NEW, SHOW, AUTHORS, SEARCH_AUTH, SEARCH_YEAR, EXIT): ")

        if action == "NEW":
            author = input("Author name: ")
            title = input("Book title: ")
            publicationYear = input("Publication year: ")
            bookDB.insertBook(author, title, publicationYear)

        elif action == "SHOW":
            id = input("Book id: ")
            bookDB.showBook(id)

        elif action == "AUTHORS":
            bookDB.listAllAuthors()

        elif action == "SEARCH_AUTH":
            author = input("Author name: ")
            bookDB.listBooksFromAuthor(author)

        elif action == "SEARCH_YEAR":
            year = input("Year: ")
            bookDB.listBooksFromYear(year)

        elif action == "EXIT":
            return 0

bookDB = bookDB()
dbUI = dbUI()

while True:
    if dbUI.readInput() == 0:
        # print(bookDB.books)
        break