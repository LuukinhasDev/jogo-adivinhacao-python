velocidade = float(input("Qual a velocidade atual do carro? ")) #pega a velocidade do veículo

if velocidade > 80:
   multa = (velocidade - 80) * 7 #calculo da multa
   print("MULTADO! Você execeu o limite permitido de 80km/h. Sua multa é de R${:.2f}".format(multa))
else:
    print("Tenha um bom dia! E siga com segurança.")