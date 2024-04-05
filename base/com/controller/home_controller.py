from base import app
from flask import render_template, request, redirect

@app.route('/')
def admin_load_category():
    return render_template('home.html')