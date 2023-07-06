from flask_app import app
import flask_app.controllers.paises
import flask_app.controllers.fabricantes

if __name__ == "__main__":
    app.run(debug=True)
