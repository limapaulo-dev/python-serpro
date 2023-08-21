import random
import math

numeroTotal = 10

while(numeroTotal > 0):
    print(numeroTotal)
    numeroTotal -= 1 

secretGame = True
rangeNumb = True
secretNumb = math.ceil(float(random.random() * 50))

while(secretGame):        
    print("jogo para adivinhar o número secreto")
    while(rangeNumb):
        guestNumb = int(input("Digite um número entre 0 e 50 "))
        if guestNumb > 0 and guestNumb < 51:
            rangeNumb = False

    if guestNumb == secretNumb:
        print("você adivinhou")
        secretGame = False
    elif guestNumb > secretNumb:
        print("número secreto menor")
    else:
        print("número secreto maior")
    rangeNumb = True


