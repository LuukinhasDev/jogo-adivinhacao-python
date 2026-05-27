soma = 0
cont = 0
for n in range(1, 7): # intervalo de 1 a 6 
    num = int(input("Digite um valor: ")) # Pergunta que vai ser feita 6 vezes ao usuário
    if num % 2 == 0: # Condição para um número ser par
        soma += num # Armazena o valor se for par e soma com outros possíveis 
        cont += 1 # Conta quantos valores pares foram digitados
print('Você informou {} números PARES e a soma deles é {}'.format(cont, soma))