termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = termo1 + (11 - 1) * razao # Fórula que calcula o décimo termo de uma PA
for i in range(termo1, decimo, razao): # termo1 é o início do intervalo, decimo mostra os 10 termos seguintese razao define de quanto em quanto a contagem vai ococrrer.
    print('{}'.format(i), end ='-> ')
print('ACABOU!')    