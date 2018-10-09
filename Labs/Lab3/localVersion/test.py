class book:

    def __init__(self, author, title, publicationYear, id):
        self.author = author
        self.title = title
        self.publicationYear = publicationYear
        self.id = id

books = []
myBook = book('Fernando Pessoa', 'O Banqueiro Anarquista', 1922, 0)
books.append(myBook)

print(books[0].author)
print(len(books))