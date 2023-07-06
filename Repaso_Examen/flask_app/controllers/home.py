from flask_app import app
from flask import render_template, redirect, request, session, flash



@app.route("/",methods=["GET"])
def home():

    return render_template("home/home.html")