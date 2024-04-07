from flask import request, redirect, render_template, url_for, session, jsonify
from sqlalchemy.ext.serializer import Serializer

from base import app, db
from base.features.user.user_dao import UserDAO
from base.features.user.user_vo import User


@app.route("/register", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User()
        user.full_name = request.form['fullName'],
        user.email = request.form["email"],
        user.password = request.form["password"]

        user_dao = UserDAO()
        user_dao.create_user(user)

        return redirect(url_for("user_login"))

    return render_template("user/register.html")


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == "POST":
        user_vo = User()
        user_vo.email = request.form["email"],
        user_vo.password = request.form["password"]

        user_dao = UserDAO()
        user_data = user_dao.get_user(user_vo)

        if user_data is None:
            return redirect(url_for("user_login"))

        access_token = user_dao.encode_auth_token(user_data.id)

        # Store tokens in session
        session['access_token'] = access_token

        return redirect(url_for("expense_list"))
    if session.get('access_token', None):
        return redirect(url_for("expense_list"))
    return render_template("user/login.html")


@app.route('/logout')
def user_logout():
    session.clear()
    return redirect(url_for('user_login'))



