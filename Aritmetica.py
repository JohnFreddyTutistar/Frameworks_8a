'''
    Developer: John Freddy Tutistar
    Description: Script que recibe dos numeros por consola y permite seleccionar de un menu
    una opcion de operacion aritmetica a realizar con los numeros ingresados.
    las operaciones son: suma, resta, multi, divi
'''

import os

#Functions
def menu():
    print("::: MENU :::")
    print("[1. ] Sumar")
    print("[2. ] Restar")
    print("[3. ] Mult")
    print("[4. ] Divi")
    print("[5. ] Cancelar operacion")
    op = input(".:: Digite una opcion: ")

def calculadora(x, y, z):
    if z == 1 :
        ans = x + y
    elif z == 2 :
        ans = x - y 
    elif z == 3 :
        ans = x * y
    elif z == 4 :
        ans = x / y
    elif z == 5 :
        print("La operacion ha sido cancelada")
        ans = 0
    else :
        print("Opcion incorrecta")
        ans = 0

    return ans

#Main
os.system("clear")

n1 = int(input("Ingrese el primer numero"))
n2 = int(input("Ingrese el segundo numero"))
menu()

op = input(":::Digite una opcion: ")
res = calculadora(n1, n2, op)
print("El resiltado de laoperacion es  ", res)

