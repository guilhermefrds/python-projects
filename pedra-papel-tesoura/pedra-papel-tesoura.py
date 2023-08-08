# Projeto em Python de Pedra, papel e tesoura
import random

print("---------------------------------------------------")

print("Escolha entre pedra papel e tesoura!")

userescolha = str(input("Pedra, papel ou tesoura? "))

userescolha = userescolha.lower()

maquinalist = ["pedra","papel","tesoura"]
#                 0       1        2  

maquinaescolha = random.choice(maquinalist)

print("---------------------------------------------------")

if userescolha == maquinalist[0] and maquinaescolha == maquinalist[0]:      #user: pedra, maquina: pedra = valores iguais
    print(f"Maquina: {maquinaescolha}, \nUsuario: {userescolha}")
    print("---------------------------------------------------")
    print("valores iguais!")
elif userescolha == maquinalist[1] and maquinaescolha == maquinalist[1]:    #user: papel, maquina: papel = valores iguais
    print(f"Maquina: {maquinaescolha}, \nUsuario: {userescolha}")
    print("---------------------------------------------------")
    print("valores iguais!")
elif userescolha == maquinalist[2] and maquinaescolha == maquinalist[2]:    #user: tesoura, maquina: tesoura = valores iguais
    print(f"Maquina: {maquinaescolha}, \nUsuario: {userescolha}")
    print("---------------------------------------------------")
    print("valores iguais!")
# valores iguais 
elif userescolha == maquinalist[0] and maquinaescolha == maquinalist[1]:    #user: pedra, maquina: papel = Usuario perdeu
    print(f"Maquina: {maquinaescolha}, \nUsuario: {userescolha}")
    print("---------------------------------------------------")
    print("Usuario perdeu!")
elif userescolha == maquinalist[1] and maquinaescolha == maquinalist[2]:    #user: papel, maquina: tesoura = Usuario perdeu
    print(f"Maquina: {maquinaescolha}, \nUsuario: {userescolha}")
    print("---------------------------------------------------")
    print("Usuario perdeu!")
elif userescolha == maquinalist[1] and maquinaescolha == maquinalist[0]:    #user: papel, maquina: pedra = Usuario venceu
    print(f"Maquina: {maquinaescolha}, \nUsuario: {userescolha}") 
    print("---------------------------------------------------")
    print("Usuario venceu!")
elif userescolha == maquinalist[2] and maquinaescolha == maquinalist[0]:    #user: tesoura, maquina: pedra = Usuario perdeu
    print(f"Maquina: {maquinaescolha}, \nUsuario: {userescolha}")
    print("---------------------------------------------------")
    print("Usuario perdeu!")
elif userescolha == maquinalist[2] and maquinaescolha == maquinalist[1]:    #user: tesoura, maquina: papel =  Usuario ganhou
    print(f"Maquina: {maquinaescolha}, \nUsuario: {userescolha}")
    print("---------------------------------------------------")
    print("Usuario ganhou!")
elif userescolha == maquinalist[0] and maquinaescolha == maquinalist[2]:    #user: pedra, maquina: tesoura =  Usuario ganhou
    print(f"Maquina: {maquinaescolha}, \nUsuario: {userescolha}")
    print("---------------------------------------------------")
    print("Usuario ganhou!")
else:
    print("Voce nao digitou corretamente")