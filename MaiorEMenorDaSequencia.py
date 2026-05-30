maior = 0
menor = 0

# Laço rodadando do 1 ao 58
for val in range(1,6):
    peso = float(input("Peso da {}° pessoa: ".format(val)))

    # Lógica do primeiro loop, primeira ocorrência
    if val == 1:
        maior = peso
        menor = peso
    # Lógica dos loops seguintes, após a primeira ocorência
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
    
    
print("O maior peso lido foi de {}Kg".format(maior))
print("O menor peso lido foi de {}Kg".format(menor))