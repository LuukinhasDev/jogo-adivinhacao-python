numero = int(input("Digite um número qualquer: ")) #Recebe o número

if numero % 2 == 0: #Calcula se o número é Par ou Impar com baso no resto da divisão
    print("O número {} é PAR".format(numero))
else:
    print("O número {} é IMPAR".format(numero))