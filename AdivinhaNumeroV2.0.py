from random import randint
computador = randint(0,10) # Gera número aleaório
tentativas = 1 # contador de tentativas
print('Sou o seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você conegue adivinhar qual foi? ')
jogador = int(input('Qual é o seu palpite? '))
# Enquanto o valor do jogador for menor do que o número aleatório gerado pelo computador, loop while é executado
while jogador != computador:
    # Se o chute do jogador for menor...
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
        tentativas +=1
    # Se o chute do jogador for maior...
    elif jogador > computador:
        print('Menos... Tente mais uma vez.')
        tentativas +=1 
    # Se o valor do jogador cair em uma das condições, o loop reinicia uma nova tentativa até o jogador acertar
    jogador = int(input('Qual é o seu palpite? ')) 

# Mensagem exibida quando o jogador acertar o número secreto
print('Acertou com {} tentativas. Parabéns!!!'.format(tentativas))
