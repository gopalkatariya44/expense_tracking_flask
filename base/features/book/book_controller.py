from flask import render_template, request, redirect, session, url_for

from base import app
from base.features.book.book_dao import BookDAO
from base.features.book.book_vo import Book
from base.features.user.user_dao import UserDAO


@app.route('/')
def book_list():
    if session.get('access_token', None):
        book_dao = BookDAO()
        user_dao = UserDAO()
        user_id = user_dao.decode_auth_token(session['access_token'])
        books = book_dao.book_list(user_id)
        return render_template('home.html', books=books)
    else:
        return redirect(url_for("user_login"))


@app.route('/add-book', methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book_vo = Book()
        book_dao = BookDAO()
        user_dao = UserDAO()

        user_id = user_dao.decode_auth_token(session['access_token'])
        book_vo.user_id = user_id
        book_vo.name = request.form.get('name')

        print(book_vo)
        book_dao.create_book(book_vo)

        return redirect(url_for("book_list"))

    return render_template("book/add_book.html")


# @app.route('/expense-details/<id>')
# def expense_details(id):
#     expense_dao = ExpenseDAO()
#     expense = expense_dao.get_expense(id)
#     return render_template("expense/expense_details.html", expense=expense)


@app.route('/update-book/<id>', methods=["GET", "POST"])
def edit_book(id):
    book_dao = BookDAO()
    if request.method == "POST":
        book_vo = Book()
        book_dao = BookDAO()

        book_vo.id = id
        book_vo.name = request.form.get('name')

        user_dao = UserDAO()
        user_id = user_dao.decode_auth_token(session['access_token'])
        book_vo.user_id = user_id

        book_dao.update_book(book_vo)

        return redirect(url_for("book_list"))

    book = book_dao.get_book(id)
    return render_template("book/update_book.html", book=book)


@app.route('/delete-book/<id>')
def delete_book(id):
    book_dao = BookDAO()
    book_dao.delete_book(id)
    return redirect(url_for("book_list"))
