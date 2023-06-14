

class Equipos():

    puntos_victoria = 3
    puntos_empate = 1
    puntos_derrota = 0

    equipos = []

    def __init__(self, nombre):

        self.nombre=nombre
        self.victorias = 0
        self.empates = 0
        self.derrotas = 0
        self.puntos = 0

        Equipos.equipos.append(self)

    def victoria(self):
        self.victorias += 1
        self.puntos += Equipos.puntos_victoria

    def derrota(self):
        self.derrotas += 1
        self.puntos += Equipos.puntos_derrota

    def empate(self):
        self.empates += 1
        self.puntos += Equipos.puntos_empate

    @staticmethod
    def enfrentarEquipos(equipo1, equipo2, puntaje1, puntaje2):
        if (puntaje1 > puntaje2):
            equipo1.victoria()
            equipo2.derrota()

        elif (puntaje2 > puntaje1):
            equipo2.victoria()
            equipo1.derrota()
        else:
            equipo1.empate()
            equipo2.empate()

    @classmethod
    def mostrarTabla(cls):
        print("------------------------------------------")
        for item in cls.equipos:
            print(
                f"{item.nombre} \t{item.puntos} \t{item.victorias} \t{item.empates} \t{item.derrotas}")


nacional = Equipos("Atletico Nacional")
rosario =Equipos("Rosario Central")
santos = Equipos("Santos")

Equipos.mostrarTabla()

Equipos.enfrentarEquipos(nacional,rosario,3,1)

Equipos.mostrarTabla()

Equipos.enfrentarEquipos(santos,rosario,2,2)
Equipos.mostrarTabla()