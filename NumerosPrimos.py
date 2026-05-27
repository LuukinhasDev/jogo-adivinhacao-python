num = int(input('Digite um número: '))
total_div = 0 # Contador de divisões

for n in range(1, num+1): # Loop que vai de 1 até o valor escolhido pelo usuário
    if num % n == 0: # Checa o resto da divisão do número do usuário 
        total_div +=1 # Sempre que a divisão der resto 0, o contador aumenta em 1
if total_div == 2: # Se o número foi dividido 2 vezes, é exibido
    print("O número {} foi dividido apenas {} vezes, por isso é um número primo.".format(num, total_div))
else: # Qualquer outra possibilidade cai aqui
    print("O número {} foi dividido {} vezes, por isso não é um número primo".format(num, total_div))
    