from flask_app.models.pais import Pais
from flask_app import app
from flask import render_template, redirect, request, session, flash


@app.route("/paises", methods=["GET"])
def show_paises():
    paises = Pais.get_all()
    return render_template("paises.html", paises=paises)


@app.route("/paises", methods=["POST"])
def create_pais():
    data = {
        "nombre": request.form["nombre"],
    }
    Pais.create(data)

    return redirect("/paises")


@app.route("/paises/<int:id>", methods=["GET"])
def show_pais(id):
    pais = Pais.get_by_id(id)
    return render_template("pais.html", pais=pais)
