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


print(mayores_que_el_segundo([1, 4, 3, 4, 5]))
