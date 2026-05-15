from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "Pensar"
print('-=-' *20)
print("Pensei em um número entre 0 e 5. Tente adivinhar...")
print('-=-' *20)
jogador = int(input("Em qual número eu pensei? ")) # Jogador tenta adivinhar
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print("PARABÉNS, você Ganhou!!!")
else:
    print("GANHEI! Eu pensei no número {} e não no {}".format(computador, jogador))


