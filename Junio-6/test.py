
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
for idx in range(0, 5001):
    if idx % 2 != 0:
        sumaImpares += idx
print(sumaImpares)
suma = 0
for idx in range(1, 5001, 2):
    suma += idx
print(suma)