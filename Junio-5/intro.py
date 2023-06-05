edad = 25

if edad > 20:
    print("Mayor")
elif edad > 15:
    print("Joven")
elif edad > 10:
    print("Niño")
else:
    print("Infante")

if edad == 25:
    print(edad)
    diferencia = edad-18
    print("diferencia", diferencia)
print("diferencia", diferencia)

"""
JAVASCRIPT
function sumar(num1,num2){
    let resultado = num1+num2;
    return resultado;
}
"""


def sumar(num1, num2):
    print("edad", edad)
    resultado = num1+num2
    return resultado


adicion = sumar(2, 7)
print(adicion)


def cortesia(nombre, titulo="Sr"):
    print("Hola "+titulo+" "+nombre)


cortesia("Nestor", "Ing")

cortesia("Pablo")

graduado = None
num = 1232
flotante = 123.312312
nombre = "TEXTO"

lista = [1, 2, 3, 4, 5]
dictionary = {"nombre": "Nestor", "edad": 25}
tuplas = ("hola", 2, False)

persona = {"nombre": "Nestor", "numeros": [
    1, 6234, 73254], "contactos": {"mama": 13221, "papa": 123123}}
