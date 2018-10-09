import pickle

class bookDB:

    def __init__(self):
        self.currentId = 0
        self.books = []

    def insertBook(self, author, title, publicationYear):
        """Inserts book into database"""
        newBook = book(author, title, publicationYear, self.currentId)
        self.books.append(newBook.__dict__)
        self.currentId += 1
        f = open("bookDatabase.pickle", "wb")
        pickle.dump(self.__dict__, f)
        f.close()

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