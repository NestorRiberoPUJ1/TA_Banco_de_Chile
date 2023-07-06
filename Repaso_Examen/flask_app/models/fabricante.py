from flask_app.config.mysqlconnection import connectToMySQL


class Fabricante():

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        if "pais_id" in data:
            self.pais_id = data["pais_id"]
        if "pais" in data:
            self.pais=data["pais"]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO fabricantes (nombre, pais_id) VALUES (%(nombre)s ,%(pais_id)s);"
        return connectToMySQL('concesionario').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT fb.id,fb.nombre,fb.created_at,fb.updated_at,"\
                "paises.nombre as pais "\
                "FROM concesionario.fabricantes fb "\
                "JOIN paises  ON fb.pais_id = paises.id"
        result = connectToMySQL('concesionario').query_db(query)
        fabricantes = []
        for pais in result:
            fabricantes.append(cls(pais))
        return fabricantes

    @classmethod
    def get_by_id(cls, id):
        data = {
            "id": id
        }
        query = "SELECT * FROM fabricantes WHERE id = %(id)s;"
        result = connectToMySQL('concesionario').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_by_id(cls, data):
        query = "UPDATE fabricantes SET nombre = %(nombre)s, pais_id = %(pais_id)s  WHERE (id = %(id)s);"
        return connectToMySQL('concesionario').query_db(query, data)

    @classmethod
    def delete_by_id(cls, data):
        query = "DELETE FROM fabricantes WHERE (id = %(id)s);"
        return connectToMySQL('concesionario').query_db(query, data)
