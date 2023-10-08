"""
Nos piden hacer un programa que gestione una serie de productos. Los productos tienen los siguientes atributos:
    Nombre
    Precio

Tenemos dos tipos de productos:
    Perecedero: tiene un atributo llamado días a caducar.
    No perecedero: tiene un atributo llamado tipo.

Tendremos una función llamada calcular, y que según la clase hará una cosa u otra.

A esta función le pasaremos un número que será la cantidad de productos:
    En Producto, simplemente sería multiplicar el precio por la cantidad de productos pasados y devolverá el resultado.
    En Perecedero, además de lo que hace producto, el precio se reducirá según los días a caducar:
    Si le queda 1 día para caducar, se reducirá 4 veces el precio final (dividir entre 4).
    Si le quedan 2 días para caducar, se reducirá 3 veces el precio final (dividir entre 3).
    Si le quedan 3 días para caducar, se reducirá a la mitad de su precio final (dividir entre 2).
    En NoPerecedero, hace lo mismo que en Producto.
    Producto tiene que implementar los métodos __str__ y __lt__.
"""