from flask import render_template, request, redirect, session, url_for

from base import app
from base.features.expense.expense_dao import ExpenseDAO
from base.features.expense.expense_vo import Expense
from base.features.user.user_dao import UserDAO


@app.route('/')
def expense_list():
    if session.get('access_token', None):
        expense_dao = ExpenseDAO()
        user_dao = UserDAO()
        user_id = user_dao.decode_auth_token(session['access_token'])
        expenses = expense_dao.expense_list(user_id)
        return render_template('home.html', expenses=expenses)
    else:
        return redirect(url_for("user_login"))


@app.route('/add-expense', methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        expense_vo = Expense()
        expense_dao = ExpenseDAO()

        expense_vo.remark = request.form.get('remark')
        expense_vo.price = request.form.get('price')
        expense_vo.quantity = request.form.get('quantity')
        expense_vo.created_at = expense_dao.local_to_utc(request.form.get('date'), request.form.get('time'))

        user_dao = UserDAO()
        user_id = user_dao.decode_auth_token(session['access_token'])
        expense_vo.user_id = user_id

        expense_dao.create_expense(expense_vo)

        return redirect(url_for("expense_list"))

    return render_template("expense/add_expense.html")


@app.route('/update-expense/<id>', methods=["GET", "POST"])
def edit_expense(id):
    expense_dao = ExpenseDAO()
    if request.method == "POST":
        expense_vo = Expense()
        expense_vo.id = id
        expense_vo.remark = request.form.get('remark')
        expense_vo.price = request.form.get('price')
        expense_vo.quantity = request.form.get('quantity')

        user_dao = UserDAO()
        user_id = user_dao.decode_auth_token(session['access_token'])
        expense_vo.user_id = user_id

        expense_dao.update_expense(expense_vo)

        return redirect(url_for("expense_list"))
    expense = expense_dao.get_expense(id)
    return render_template("expense/update_expense.html", expense=expense)


@app.route('/delete-expense/<id>')
def delete_expense(id):
    expense_dao = ExpenseDAO()
    expense_dao.delete_expense(id)
    return redirect(url_for("expense_list"))
