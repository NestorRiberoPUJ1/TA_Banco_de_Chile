from flask_app.models.fabricante import Fabricante
from flask_app.models.pais import Pais
from flask_app import app
from flask import render_template, redirect, request, session, flash


@app.route("/fabricantes", methods=["GET"])
def show_fabricantes():
    fabricantes = Fabricante.get_all()
    paises = Pais.get_all()
    return render_template("fabricantes/fabricantes.html", fabricantes=fabricantes, paises=paises)


@app.route("/fabricantes", methods=["POST"])
def create_fabricante():
    data = {
        "pais_id": request.form["pais_id"],
        "nombre": request.form["nombre"],
    }
    Fabricante.create(data)

    return redirect("/fabricantes")


@app.route("/fabricantes/editar", methods=["POST"])
def put_fabricante():
    print(request.form)
    data = {
        "id": request.form["id"],
        "nombre": request.form["nombre"],
    }
    Fabricante.update_by_id(data)

    return redirect("/fabricantes/"+request.form["id"])


@app.route("/fabricantes/borrar/<int:id>", methods=["GET"])
def delete_fabricante(id):

    Fabricante.delete_by_id(id)

    return redirect("/fabricantes")


@app.route("/fabricantes/<int:id>", methods=["GET"])
def show_fabricante(id):
    pais = Fabricante.get_by_id(id)
    return render_template("fabricantes/fabricante.html", pais=pais)


@app.route("/fabricantes/editar/<int:id>", methods=["GET"])
def edit_fabricante(id):
    pais = Fabricante.get_by_id(id)
    return render_template("fabricantes/editar_fabricante.html", pais=pais)
