from flask import Flask, request, render_template, redirect, url_for, jsonify, abort
from forms import BookForm
from models import books

app = Flask(__name__)
app.config["SECRET_KEY"] = "BARDZO_TAJNY_KLUCZ"


# WIDOK HTML

@app.route("/books/", methods=["GET", "POST"])
def books_list():
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            books.create(form.data)
            return redirect(url_for("books_list"))
    return render_template("books.html", form=form, books=books.all())


@app.route("/books/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = books.get(book_id - 1)
    if not book:
        return "Książka nie istnieje", 404

    form = BookForm(
        formdata=request.form if request.method == "POST" else None,
        data=book
    )

    if request.method == "POST":
        if form.validate_on_submit():
            books.update(book_id - 1, form.data)
            return redirect(url_for("books_list"))

    return render_template("book.html", form=form, book_id=book_id)


# REST API

@app.route("/api/v1/books/", methods=["GET"])
def get_all_books():
    return jsonify(books.all()), 200


@app.route("/api/v1/books/", methods=["POST"])
def create_book():
    if not request.json:
        abort(400)
        
    data = request.json
    
    if not all(['title' in data, 'author' in data, 'year' in data]):
        abort(400)
        
    if any([
        not isinstance(data.get('title'), str),
        not isinstance(data.get('author'), str),
        not isinstance(data.get('year'), int),
        'is_read' in data and not isinstance(data.get('is_read'), bool)
    ]):
        abort(400)
        
    new_book = {
        'title': data['title'],
        'author': data['author'],
        'year': data['year'],
        'is_read': data.get('is_read', False)
    }
    
    books.create(new_book)
    return jsonify({'book': new_book}), 201


@app.route("/api/v1/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = books.get(book_id - 1)
    if not book:
        abort(404)
    return jsonify(book), 200


@app.route("/api/v1/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = books.get(book_id - 1)
    if not book:
        abort(404)
        
    if not request.json:
        abort(400)
        
    data = request.json
    
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'author' in data and not isinstance(data.get('author'), str),
        'year' in data and not isinstance(data.get('year'), int),
        'is_read' in data and not isinstance(data.get('is_read'), bool)
    ]):
        abort(400)
        
    updated_book = {
        'title': data.get('title', book['title']),
        'author': data.get('author', book['author']),
        'year': data.get('year', book['year']),
        'is_read': data.get('is_read', book['is_read'])
    }
    
    books.update(book_id - 1, updated_book)
    return jsonify({'book': updated_book})


@app.route("/api/v1/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    result = books.delete(book_id - 1)
    if not result:
        abort(404)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)