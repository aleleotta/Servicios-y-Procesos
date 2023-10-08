"""
Crea una clase llamada Articulo con los siguientes atributos: nombre, precio (sin IVA),
iva (siempre será 21) y cuantosQuedan (representa cuántos quedan en el almacén).

Añade los siguientes métodos:
    Constructor con 3 parámetros que asigne valores a nombre, precio y cuantosQuedan. El IVA siempre lo pondrá a 21.
    Método getPVP que devuelva el precio de venta al público (PVP) con iva incluido. 
    Método getPVPDescuento que devuelva el PVP con un descuento pasado como argumento. 
    Método vender que actualiza los atributos del objeto tras vender una cantidad 'x' (si es posible).
    Devolverá true si ha sido posible (false en caso contrario).
    La cantidad a vender se pasará como argumento al método.
    Método almacenar que actualiza los atributos del objeto tras almacenar una cantidad 'x'.
    La cantidad a almacenar se pasará como argumento.

Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos  artículos son iguales si tienen el mismo nombre.
Los artículos se ordenarán de menor a mayor por el nombre.
"""