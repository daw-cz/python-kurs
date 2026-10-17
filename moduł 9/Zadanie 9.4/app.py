from flask import Flask, request, render_template, redirect, url_for
from forms import BookForm
from models import books

app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret-library-key"


@app.route("/books/", methods=["GET", "POST"])
def books_list():
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            books.create(form.data)
            books.save_all()
            return redirect(url_for("books_list"))

    return render_template("books.html", form=form, books=books.all())


@app.route("/books/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = books.get(book_id - 1)
    if not book:
        return "Książka nie istnieje", 404

    form = BookForm(formdata=request.form if request.method == "POST" else None, data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            books.update(book_id - 1, form.data)
            books.save_all()
            return redirect(url_for("books_list"))

    return render_template("book.html", form=form, book_id=book_id)


if __name__ == "__main__":
    app.run(debug=True)