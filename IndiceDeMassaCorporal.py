peso = float(input("Qual é o seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (m) "))
imc = peso/(altura**2) #Calculo do IMC

print("O seu IMC é de {:.1f} seu status é: ".format(imc), end="")
if imc < 18.5: #Condições para o status 
    print("ABAIXO DO PESO")
elif imc < 25:
    print("PESO IDEAL")
elif imc < 30:
    print("SOBREPESO")
elif imc < 40:
    print("OBESIDADE")
else:
    print("OBESIDADE MÓRBIDA")
