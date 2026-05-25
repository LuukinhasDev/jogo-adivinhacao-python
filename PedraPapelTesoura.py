from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura") #Tupla com os itens das jogadas 
print("{:=^40}".format("PEDRA PAPEL OU TESOURA"))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador= int(input("Qual é a sua jogada? "))
computador = randint(0, 2) # Gera uma jogada aleatória ao computador 
print("JO...")
sleep(1)
print("KEN...")
sleep(1)
print("PO !!!")
print("-=-"*9)
print("O jogador jogou {}".format(itens[jogador])) # pega um item da tupla e coloca na posiçaõ jogador
print("O computador jogou {}".format(itens[computador])) # pega um item da tupla e coloca na posição computador
print("-=-"*9)
if (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 0): #condições para o jogador vencer 
    print("O Jogador venceu! Parabéns!!!")
elif jogador == computador:
    print("Deu empate")
else:
    print("O Computador venceu!")



