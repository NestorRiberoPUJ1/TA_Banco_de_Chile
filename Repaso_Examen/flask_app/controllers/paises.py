from flask_app.models.pais import Pais
from flask_app import app
from flask import render_template, redirect, request, session, flash


@app.route("/paises", methods=["GET"])
def show_paises():
    paises = Pais.get_all()
    return render_template("paises/paises.html", paises=paises)


@app.route("/paises", methods=["POST"])
def create_pais():
    data = {
        "nombre": request.form["nombre"],
    }
    Pais.create(data)

    return redirect("/paises")


@app.route("/paises/editar", methods=["POST"])
def put_pais():
    print(request.form)
    data = {
        "id": request.form["id"],
        "nombre": request.form["nombre"],
    }
    Pais.update_by_id(data)

    return redirect("/paises/"+request.form["id"])


@app.route("/paises/borrar/<int:id>", methods=["GET"])
def delete_pais(id):

    Pais.delete_by_id(id)

    return redirect("/paises")


@app.route("/paises/<int:id>", methods=["GET"])
def show_pais(id):
    pais = Pais.get_by_id(id)
    return render_template("paises/pais.html", pais=pais)


@app.route("/paises/editar/<int:id>", methods=["GET"])
def edit_pais(id):
    pais = Pais.get_by_id(id)
    return render_template("paises/editar_pais.html", pais=pais)
