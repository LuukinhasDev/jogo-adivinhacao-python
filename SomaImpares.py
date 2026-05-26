# Calcular a soma de todos os números impares e multiplos de 3 entre 1 e 500

soma = 0 # Acumulador para guardar o valor total das somas
cont = 0 # Contador para guardar a quantidade de números encontrados
for n in range(0, 501):
    if (n % 2 != 0 and n % 3 == 0): # condição para verificar se o valor é impar e multiplo de 3
        cont += 1
        soma = soma + n
print('A soma dos {} valores encontrados é de {}'.format(cont, soma))