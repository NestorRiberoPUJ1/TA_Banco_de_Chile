# importar la función que devolverá una instancia de una conexión
from flask_app.config.mysqlconnection import connectToMySQL


class User():

    def _init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.password = data["password"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (email, password, first_name, last_name)"\
            "VALUES (%(email)s, %(password)s, %(first_name)s, %(last_name)s);"
        return connectToMySQL('mydb').query_db(query, data)
