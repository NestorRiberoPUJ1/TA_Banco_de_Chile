from persona import Persona


class Deportista (Persona):

    def __init__(self, nombre, estatura, peso):
        super().__init__(nombre)
        self.estatura = estatura
        self.peso = peso

    def ejercitarse(self):
        print(f"{self.nombre} haciendo ejercicio")

    def trotar(self):
        print(f"{self.nombre}: Estoy trotando")

    def saltar(self):
        raise NotImplementedError


class Politico (Persona):

    def __init__(self, nombre, partido, experiencia):
        super().__init__(nombre)
        self.nombre = nombre
        self.partido = partido
        self.experiencia = experiencia

    def hacer_campana(self):
        print(f"{self.nombre}: Voten por mi")


if __name__ == "__main__":

    Bolt = Deportista("Ussain", 195, 85)
    Bolt.ejercitarse()
    Bolt.saludar()
