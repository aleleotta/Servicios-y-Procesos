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