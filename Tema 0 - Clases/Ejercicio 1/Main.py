"""
Diseñar la clase CuentaCorriente, que almacena los datos DNI, nombre y el saldo.

Añade los siguientes constructores:
    Con el DNI del titular de la cuenta y un saldo inicial. El nombre se inicializará a cadena vacía.
    Con el DNI, nombre y el saldo inicial.
    
Las operaciones típicas de una cuenta corriente son:
    Sacar dinero: el método debe indicar si ha sido posible llevar a cabo la operación, si existe saldo suficiente. Si es posible llevar a cabo la operación se resta la cantidad a sacar al saldo de la cuenta.
    Ingresar dinero: se incrementa el saldo.

Crear también los métodos __str__, __eq__ y __lt__.
Se considera que dos cuentas corrientes son iguales si tienen el mismo DNI.
Las cuentas corrientes se ordenarán de menor a mayor por el saldo.
"""

from CuentaCorriente import *

class Main:

    list = []

    def list():
        print("1) Add bank account")
        print("2) Show all bank accounts")
        print("3) Remove bank account")
        print("0) Exit")
        print("\nChoose one of the options above:")

    def add():
        dni = 0
        hasName = 0
        name = ""
        balance = 0
        dni = int(input("Introduce your DNI: "))
        hasName = int(input("Do you wanna introduce your name? 0 = No, 1 = Yes"))
        if hasName == 1:
            name = input("Introduce your name: ")
            obj = CuentaCorriente(dni, name, balance)
            list.append(obj)
        else:
            obj = CuentaCorriente(dni, balance)
            list.append(obj)

    def showList():
        for currentObj in list:
            currentObj.__str__
        print("\n")

    def remove():
        dni = 0
        dni = int(input("Introduce the DNI of the account to remove from list: "))
        for currentObj in list:
            if currentObj.dni == dni:
                list.remove(currentObj)

    option = 4
    while option != 0:
        list()
        option = int(print("Introduce an option: "))
        if option == 1:
            add()
        if option == 2:
            showList()
        if option == 3:
            remove()
        if option == 0:
            print("Have a great day!")