from flask_app import app
import flask_app.controllers.paises
import flask_app.controllers.fabricantes
import flask_app.controllers.home

if __name__ == "__main__":
    app.run(debug=True)
