from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    print("Calculadora:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Suma avanzada (varios números)")
    print("6. Salir")

while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print("Resultado:", sumar(a, b))
    elif opcion == "2":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print("Resultado:", restar(a, b))
    elif opcion == "3":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print("Resultado:", multiplicar(a, b))
    elif opcion == "4":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print("Resultado:", dividir(a, b))
    elif opcion == "5":
        numeros = input("Escribe los números separados por coma: ")
        lista = [float(x) for x in numeros.split(",")]
        print("Resultado:", suma_avanzada(lista))
    elif opcion == "6":
        break
    else:
        print("Opción inválida")
