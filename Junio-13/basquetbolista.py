
from profesiones import Deportista


class Basquetbolista(Deportista):

    def __init__(self, nombre, estatura, peso, salto):
        super().__init__(nombre, estatura, peso)
        self.salto = salto

    def trotar(self):
        print(f"{self.nombre}: Recogiendo Balón")
        return super().trotar()

    def saltar(self):
        print(f"{self.nombre}: Saltando más de {self.salto}cm")


if __name__ == "__main__":
    LeBron = Basquetbolista("LeBron", 210, 100, 120)
    LeBron.ejercitarse()
    LeBron.trotar()
    LeBron.saltar()
    LeBron.saludar()
