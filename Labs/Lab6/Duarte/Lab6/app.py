from flask import Flask
from flask import render_template
from flask import request
import bookDB

app = Flask(__name__)
db = bookDB.bookDB("mylib")

@app.route('/')
def hello_world():
    count = len(db.listAllBooks())
    return render_template("mainPage.html", count_books=count)

@app.route('/addBooksForm')
def add_Book_Form():
    return render_template("addBookTemplate.html")

@app.route('/addBook', methods=['POST', 'GET'])
def add_Book():
    if request.method == "GET":
        db.addBook(request.args['Author'], request.args['Title'], request.args['Year'])
        return str(request.args)
    else:
        db.addBook(request.form['Author'], request.form['Title'], request.form['Year'])
        return str(request.form)
    return render_template("addBookTemplate.html")

@app.route('/listAllBooks')
def listAllValues():
    bookList = db.listAllBooks()
    return render_template("listAllBooksTemplate.html", books = bookList)

@app.route('/searchBooksAuthor')
def searchBooksAuthor():
    return render_template("searchAuthorTemplate.html")

@app.route('/searchBooksYear')
def searchBooksYear():
    return render_template("searchYearTemplate.html")

@app.route('/listBooksAuthor')
def listBooksAuthor():
    if request.method == "GET":
        bookList = db.listBooksAuthor(request.args['Author'])
    else:
        bookList = db.listBooksYear(request.form['Author'])
    return render_template("listAllBooksTemplate.html", books = bookList)

@app.route('/listBooksYear')
def listBooksYear():
    if request.method == "GET":
        bookList = db.listBooksYear(request.args['Year'])
    else:
        bookList = db.listBooksYear(request.form['Year'])
    return render_template("listAllBooksTemplate.html", books = bookList)

if __name__ == '__main__':
    app.run()
