local_val = "unicornios mágicos"


def square(x):
    return x * x


class Usuario:
    def __init__(self, name):
        self.name = name

    def di_hola(self):
        return "hola"



if (__name__ =="__main__"):
    print("EJECUTANDO COMO PRINCIPAL")
    # en el mismo archivo, agrega lo siguiente debajo de la clase Usuario
    print(square(5))
    user = Usuario("Annita")
    print(user.name)
    print(user.di_hola())
else:
    print("EJECUTANDO COMO MODULO IMPORTADO")