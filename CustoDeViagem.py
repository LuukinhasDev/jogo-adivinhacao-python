#Viagens até 200Km, cobrar R$0.50 para cada km, viagens acima de 200km cobrar R$0.45 


distancia = float(input("Qual é a distância da sua viagem? ")) #Recebe o valor da distância em Km/h
print("você está pestes a começar uma viagem de {:.1f}Km".format(distancia))
if distancia <= 200: 
    preço = distancia * 0.50 #Calculo do valor da passagem
else:
    preço = distancia * 0.45
print ("Sua passagem vai custar R${:.2f}".format(preço))