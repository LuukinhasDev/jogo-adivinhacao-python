salario = float(input("Qual é o salário atual do funcionário? R$ "))

if salario > 1250: 
    aumento = salario + (salario * 10 / 100) #Calculo de 10% de aumento
else:
    aumento = salario + (salario * 15 / 100) #Calculo de 15% de aumento

print("Quem ganhava R${:.2f} passa a ganhar R${:.2f}".format(salario, aumento))