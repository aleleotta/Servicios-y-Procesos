"""
Codificar el juego �el n�mero secreto�, que consiste en acertar un n�mero entre 1 y 100 (generado aleatoriamente).
Para ello se introduce por teclado una serie de n�meros, para los que se indica: �mayor� o �menor�, seg�n sea mayor o menor con respecto al n�mero secreto.
El proceso termina cuando el usuario acierta o cuando se rinde (introduciendo un -1).
"""
import random
guessnumber = random.randint(0, 100)
userNum = 0
while userNum!=-1 and userNum!=guessnumber:
    userNum = int(input("Guess number: "))
    if userNum==-1:
        print("Good luck next time!")
        break
    print("You guessed!") if userNum==guessnumber else print("Wrong!")