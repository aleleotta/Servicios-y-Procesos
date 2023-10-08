"""
Solicita al usuario un n�mero n y dibuja un tri�ngulo de base y altura n. Por ejemplo para n=4 debe dibujar lo siguiente:
   *
  * *
 * * *
* * * *
"""

num = int(input("Type in a number to build a triangle: "))
for i in range(1, num+1):
    print(" "*(num-i)+"* "*i)