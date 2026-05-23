#A aprovação do empréstimo é para a compra de uma casa, mas o valor da prestação mensal não pode passar de 30% do salário, caso isso ocorra o empréstimo é negado.

casa = float(input("Valor da casa? R$ "))
salario = float(input("Salário do comprador: R$ "))
anos = int(input("Quantos anos de financiamento: "))
prestacao = casa / (anos *12)#Calculo do valor das prestações que o comprador vai pagar

if salario *0.30 <= prestacao: #Condição para aprovação do empréstimo 
    print("Para pagar uma casa no valor de R${:.2f} a prestação será de R${:.2f}, Empréstimo NEGADO!".format(casa, prestacao))
else:
    print("Para pagar uma casa de R${:.2f} a prestação será de R${:.2f}, Empréstimo CONCEDIDO!".format(casa, prestacao))

