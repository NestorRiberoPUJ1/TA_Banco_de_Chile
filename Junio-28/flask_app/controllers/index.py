from flask_app import app
from flask import render_template, redirect, request, session, flash


@app.route("/")
def root():

    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]

    return render_template("index.html", titulo="TABLA DE HTML", users=users)


@app.route("/chess/<int:n>/<int:m>")
def chessboard(n, m):
    print(type(n))
    return render_template("chessboard.html", n=n, m=m)
