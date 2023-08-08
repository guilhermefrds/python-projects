# Projeto do jogo Adivinhe o Número em Python
import time
import random
import sys

nummaq = random.randrange(1,10)
print(nummaq)

try:
    print("Neste programa voce tera que adivinhar o *NUMERO* de *1 A 10* que a maquina escolheu.")
    num1 = int(input("Escolha um numero: "))
    if num1 > 10:
        print("Voce deve digitar um numero de 1 ate 10!")
        exit
except ValueError:
    print("Apenas numeros sao permitidos")
    sys.exit()
    
while num1 > 10:
    num1 = int(input("Escolha um numero de 1 ate 10!: "))

while num1 != nummaq:
    num1 = int(input("Escolha outro numero de 1 ate 10: "))
    print("tente novamente!")

if num1 == nummaq:
    print("Parabens! voce acertou!")
else:
    print("tente novamente!")
    