estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(estudiantes):
    for i in range(len(estudiantes)):
        for key, value in estudiantes[i].items():
            print(f"{key} - {value}", end=" , ")
        print("")


# iterateDictionary(estudiantes)

x = 10


def mayores_que_el_segundo(lista):
    filtrada = list(filter(lambda x: x > lista[1], lista))
    if (len(filtrada)) > 2:
        return filtrada
    return False


# print(mayores_que_el_segundo([1, 4, 3, 4, 5]))


def iterateDictionar(some_list):
    for item in some_list:
        # print(item)
        texto = ""
        for key, value in item.items():
            texto += key+"-"+value+" , "
        print(texto)


# iterateDictionar(estudiantes)


dict = {
    "nombre": "Nestor",
    "edad": 25,
    "ciudades": ["NewYork", "LA", "MIAMI", "CHICAGO", "LOUISVILLE"]
}
lista = ["NewYork", "LA", "MIAMI", "CHICAGO",
         "LOUISVILLE", {"ESTADO": "GEORGIA"}]

NBA = {
    "EAST": ["HEAT", "KNICKS", "CELTICS", "76ERS"],
    "WEST": ["LAKERS", "WARRIORS", "NUGGETS", "SPURS"]
}


print(NBA["EAST"])

""" for team in NBA["EAST"]:
    print(team)
for team in NBA["WEST"]:
    print(team) """

for key, value in NBA.items():
    print(key, value)
    for team in value:
        print(team)
