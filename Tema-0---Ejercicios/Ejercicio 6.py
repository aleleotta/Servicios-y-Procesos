"""
Pedir un n�mero y calcular su factorial. Por ejemplo, el factorial de 5 se denota 5! y es igual a 5x4x3x2x1 = 120.
"""

num = int(input("Introduce a number: "))
result = num
for i in range(num-1, 1, -1):
    result = result * i
print("Result:", result)