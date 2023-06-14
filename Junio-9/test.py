

# Clases -> estructura de datos orden caracteristicas atributos

class Animal ():

    reino = "ANIMAL"
    manada = 0

    def __init__(self, grupo, familia, especie):
        # Atributos de la clase
        self.grupo = grupo
        self.familia = familia,
        self.especie = especie
        Animal.manada += 1



print("Animales en la manada:", Animal.manada)
Alpaca = Animal("mamífero", "camelido", "Alpaca")
print(Alpaca)
print(Alpaca.familia)
print("Animales en la manada:", Animal.manada)
print(Animal.reino)
