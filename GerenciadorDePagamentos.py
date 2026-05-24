preco = float(input("Preço das compras: R$ "))
print(''' FORMAS DE PAGAMENTO
      [ 1 ] à vista dinheiro/cheque
      [ 2 ] à vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
opcao = int(input("Digite a opção de sua escolha: "))

if opcao == 1:
    desconto = preco * 0.10 # Desconto de 10%
    NovoPreco = preco - desconto
    print("Sua compra de R${:.2f} vai custar R${:.2f}".format(preco, NovoPreco))
elif opcao == 2:
    desconto = preco * 0.05 #Desconto de 5%
    NovoPreco = preco - desconto
    print("Sua compra de R${:.2f} vai custar R${:.2f}".format(preco, NovoPreco))
elif opcao == 3:
    parcela = preco / 2 # Parcelamento da compra em 2x
    print("Sua compre de R${:.2f} será dividida em duas parcelas de R${:.2f}".format(preco, parcela))
elif opcao == 4:
    numParcela = int(input("Quantas parcelas? ")) # Numero de parcelas
    juros = preco * 0.20 # Juros de 20%
    novoPreco = preco + juros # Juros aplicado ao preço das compras
    parcela = novoPreco / numParcela # Parcelamento do preço com Juros
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(numParcela, parcela))
    print("Sua compra de R${:.2f} vai custar R${:.2f}".format(preco, novoPreco))
else: # Caso escolham uma opção de pagamento fora das listadas
     print("OPÇÃO INVÁLIDA de pagamento. Tente novamente!")
