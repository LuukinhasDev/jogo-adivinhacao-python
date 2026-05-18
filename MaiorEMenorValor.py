valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Terceiro valor: "))
#Verificando o maior valor
maior = valor1
if valor2 > valor1 and valor3:
    maior = valor2
if valor3 > valor2 and valor1:
    maior = valor3
#Verificando o menor valor
menor = valor1
if valor2 < valor1 and valor3:
    menor = valor2
if valor3 < valor1 and valor2:
    menor = valor3
print("_"*30)
print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")
