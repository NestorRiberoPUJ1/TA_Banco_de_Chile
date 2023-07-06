from flask_app.config.mysqlconnection import connectToMySQL


class Pais():

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO paises (nombre) VALUES (%(nombre)s);"
        return connectToMySQL('concesionario').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM paises;"
        result = connectToMySQL('concesionario').query_db(query)
        paises = []
        for pais in result:
            paises.append(cls(pais))
        return paises

    @classmethod
    def get_by_id(cls, id):
        data = {
            "id": id
        }
        query = "SELECT * FROM paises WHERE id = %(id)s;"
        result = connectToMySQL('concesionario').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_by_id(cls, data):
        query = "UPDATE paises SET nombre = %(nombre)s WHERE (id = %(id)s);"
        return connectToMySQL('concesionario').query_db(query, data)

    @classmethod
    def delete_by_id(cls, id):
        data = {
            "id": id
        }
        query = "DELETE FROM paises WHERE (id = %(id)s);"
        return connectToMySQL('concesionario').query_db(query, data)
