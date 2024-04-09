from datetime import datetime

import pytz
from flask import render_template, request, redirect, session, url_for
from pytz import utc

from base import app
from base.features.expense.expense_dao import ExpenseDAO
from base.features.expense.expense_vo import Expense
from base.features.user.user_dao import UserDAO


@app.route('/expenses/<book_id>')
def expense_list(book_id):
    if session.get('access_token', None):
        expense_dao = ExpenseDAO()
        user_dao = UserDAO()
        user_id = user_dao.decode_auth_token(session['access_token'])
        expenses, total = expense_dao.expense_list(user_id, book_id)

        return render_template('expense/expense_list.html', expenses=expenses, total=total, book_id=book_id)
    else:
        return redirect(url_for("user_login"))


@app.route('/add-expense/<book_id>', methods=["GET", "POST"])
def add_expense(book_id):
    if request.method == "POST":
        expense_vo = Expense()
        expense_dao = ExpenseDAO()

        expense_vo.book_id = book_id
        expense_vo.remark = request.form.get('remark')
        expense_vo.price = request.form.get('price')
        expense_vo.quantity = request.form.get('quantity')
        expense_vo.created_at = expense_dao.local_to_utc(request.form.get('date'), request.form.get('time'))

        user_dao = UserDAO()
        user_id = user_dao.decode_auth_token(session['access_token'])
        expense_vo.user_id = user_id

        expense_dao.create_expense(expense_vo)

        return redirect(url_for("expense_list", book_id=book_id))

    return render_template("expense/add_expense.html")


@app.route('/expense-details/<book_id>/<id>')
def expense_details(book_id, id):
    expense_dao = ExpenseDAO()
    expense = expense_dao.get_expense(id)
    return render_template("expense/expense_details.html", expense=expense, book_id=book_id)


@app.route('/update-expense/<book_id>/<id>', methods=["GET", "POST"])
def edit_expense(book_id, id):
    expense_dao = ExpenseDAO()
    if request.method == "POST":
        expense_vo = Expense()
        user_dao = UserDAO()
        expense_vo.id = id
        expense_vo.remark = request.form.get('remark')
        expense_vo.price = request.form.get('price')
        expense_vo.quantity = request.form.get('quantity')
        expense_vo.created_at = expense_dao.local_to_utc(request.form.get('date'), request.form.get('time'))

        user_id = user_dao.decode_auth_token(session['access_token'])
        expense_vo.user_id = user_id

        expense_dao.update_expense(expense_vo)

        return redirect(url_for("expense_list", book_id=book_id))
    expense = expense_dao.get_expense(id)
    return render_template("expense/update_expense.html", expense=expense)


@app.route('/delete-expense/<book_id>/<id>')
def delete_expense(book_id, id):
    expense_dao = ExpenseDAO()
    expense_dao.delete_expense(id)
    return redirect(url_for("expense_list", book_id=book_id))
