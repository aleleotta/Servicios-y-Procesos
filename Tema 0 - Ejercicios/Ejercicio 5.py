"""
Escribir una aplicaci�n para aprender a contar, que pedir� un n�mero n y mostrar� todos los n�meros del 1 al n.
"""

n = int(input("Give a random number: "))
for currentNum in range(n+1):
    print(currentNum, end=" ")