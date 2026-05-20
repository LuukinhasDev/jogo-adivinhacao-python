num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
#Comparando os números 
if num1 > num2:
    print("O primeiro valor {} é maior do que o segundo valor {}".format(num1, num2))
elif num2 > num1:
    print("O segundo valor {} é maior do que o primeiro valor {}".format(num2, num1))
else:
    print("Não existe valor maior, os dois são iguais.")