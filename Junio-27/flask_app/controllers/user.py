from flask_app.models.user import User
from flask_app import app
from flask import render_template, redirect, request, session, flash


@app.route("/user", methods=["POST"])
def create_user():
    data = {
        "email": request.form["email"],
        "password": request.form["password"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
    }
    print(data)
    User.save(data)
    return redirect("/")
