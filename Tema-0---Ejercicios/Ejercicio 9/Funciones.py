"""
Escribe una funci�n a la que se le pasen dos enteros y muestre todos los n�meros comprendidos entre ellos.
Desde el m�todo main() lee los dos n�meros enteros, los cuales deben introducirlos el usuario, y p�salos como par�metros de entrada de la funci�n.
"""

def printBetweenNums(num1, num2):
    for i in range(num1, num2+1):
        print(i, end=" ")