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
        bookInf = str(db.showBook(request.args['BookID']))
        return render_template("listAllBooksTemplate.html", bookInfo = bookInf)

    else:
        bookInf = db.listBooksYear(request.form['BookID'])
        return render_template("listAllBooksTemplate.html", bookInfo = bookInf)
    
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
