
for idx in range(0, 151):
    print(idx)


# Condicional
for idx in range(5, 1001):
    if (idx % 5 == 0):
        print(idx)

# Saltos
for idx in range(5, 1001, 5):
    print(idx)


for idx in range(1, 101):
    if idx % 5 == 0:
        if idx % 2 == 0:
            print("Coding Dojo")
        else:
            print("Coding")
    else:
        print(idx)


for idx in range(0, 50):
    if idx % 2 == 0 and idx % 6 != 0:
        print("Coding")
    elif idx % 6 == 0:
        print("DOJO")
    else:
        print(idx)


sumaImpares = 0
for idx in range(0, 51):
    if idx % 2 != 0:
        sumaImpares += idx
print(sumaImpares)
suma = 0
for idx in range(1, 51, 2):
    suma += idx
print(suma)


# rango de valores con incrementales inicial a un final y cuente de x en x

# para recorrer una lista

lista = [4, 8, 12, 16, 20, 24]

for idx in range(len(lista)):
    print(idx, lista[idx])


for elemento in lista:
    print(elemento)

dictionary = {"a": 42, "b": 44}

print(dictionary.values())


def obtenerCarro():
    marca = "Ferrari"
    modelo = "Enzo"
    return marca, modelo


elementos = obtenerCarro()
print(elementos)
