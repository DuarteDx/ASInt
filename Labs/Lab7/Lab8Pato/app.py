from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import bookDB

app = Flask(__name__)
db = bookDB.bookDB("mylib")

@app.route('/')
def hello_world():
    count = len(db.listAllBooks())
    return render_template("mainPage.html", count_books=count)

@app.route('/API/books/<id>/likes', methods = ['GET', 'POST'])
def bookLikesAPI(id):    
    if request.method == "GET":
        return jsonify(db.bib[int(id)].likes)

    elif request.method == "POST":
        db.bib[int(id)].likes += 1
        return jsonify(db.bib[int(id)].likes)


@app.route('/API/books/<id>', methods = ['GET', 'POST'])
def showBookAPI(id):    
    if request.method == "GET":
        bookInfo = db.showBook(int(id))

    else:
        bookInfo = db.showBook(int(id))

    message = { "id": bookInfo.id,
                "author": bookInfo.author,
                "year": bookInfo.year,
                "title": bookInfo.title,
                "likes": bookInfo.likes
    }
    resp = jsonify(message)
    resp.status_code = 200
    return resp

@app.route('/API/authors')
def list_authors_API():    
    bookList = db.listAllBooks()
    authors = list()
    for book in bookList:
        authors.append(book.author)
    message = list(set(authors))
    resp = jsonify(message)
    resp.status_code = 200
    return resp

@app.route('/API/authors/<name>', methods = ['GET'])
def listBooksAuthorAPI(name):
    bookList = db.listAllBooks()
    authors = list()
    for book in bookList:
        authors.append(book.author)
    
    if name in authors: 
        bookList = db.listBooksAuthor(request.args[name])
        titles = list()
        #len(titles)
        for book in bookList:
            titles.append(book.title)
        message = {"titles": titles}
        resp = jsonify(message)
        resp.status_code = 200
        return resp

    else:
        return not_found()

@app.route('/API/books')
def list_all_books_API():    
    bookList = db.listAllBooks()
    index = list()
    for book in bookList:
        index.append(book.id)
    message = {"books": index}
    resp = jsonify(message)
    resp.status_code = 200
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.route('/addBooksForm')
def add_Book_Form():
    return render_template("addBookTemplate.html")

@app.route('/listAllBooks')
def list_All_Books():
    bookList = db.listAllBooks()
    return render_template("listAllBooksTemplate.html", books = bookList)

@app.route('/showBookForm')
def ShowBookForm():
    return render_template("showBookFormTemplate.html")

@app.route('/showBook', methods=['POST', 'GET'])
def showBook():    
    if request.method == "GET":
        bookInfo = db.showBook(int(request.args['BookID']))
        return render_template("showBookTemplate.html", id=bookInfo.id, title=bookInfo.title, author=bookInfo.author, likes=bookInfo.likes, year=bookInfo.year)

    elif request.method == 'POST':
        bookInfo = db.showBook(int(request.form['BookID']))
        return render_template("showBookTemplate.html", bookInfo=str(bookInfo), id=bookInfo.id, title=bookInfo.title, author=bookInfo.author, likes=bookInfo.likes, year=bookInfo.year)
    
    return

@app.route('/listBooksYearForm')
def listBooksYearForm():
    return render_template("searchYearTemplate.html")

@app.route('/listBooksYear', methods=['POST', 'GET'])
def listBooksYear():
    if request.method == "GET":
        bookList = db.listBooksYear(request.args['Year'])
        return render_template("listAllBooksTemplate.html", books = bookList)

    else:
        bookList = db.listBooksYear(request.form['Year'])
        return render_template("listAllBooksTemplate.html", books = bookList)
    
    return

@app.route('/listBooksAuthorForm')
def listBooksAuthorForm():
    return render_template("searchAuthorTemplate.html")

@app.route('/listBooksAuthor', methods=['POST', 'GET'])
def listBooksAuthor():
    if request.method == "GET":
        bookList = db.listBooksAuthor(request.args['Author'])
        return render_template("listAllBooksTemplate.html", books = bookList)

    else:
        bookList = db.listBooksAuthor(request.form['Author'])
        return render_template("listAllBooksTemplate.html", books = bookList)
    
    return

@app.route('/addBook', methods=['POST', 'GET'])
def add_Book():
    if request.method == "GET":
        db.addBook(request.args['Author'], request.args['Title'], request.args['Year'])        
        return str(request.args['Title'])

    else:
        db.addBook(request.form['Author'], request.form['Title'], request.form['Year'])
        return str(request.form['Title'])
    return render_template("addBookTemplate.html")


if __name__ == '__main__':
    app.run()
