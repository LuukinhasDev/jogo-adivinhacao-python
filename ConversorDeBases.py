num = int(input("Digite um número inteiro: "))
print(''' Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''') # Exibição das opções possíveis
opcao = int(input("Sua opção: "))

if opcao == 1: # bin() para obter base binária
    print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:])) #[2:] para excluir as duas primeiras strings que indicam a base "0b..."
elif opcao == 2:
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num)[2:])) # oct() para obter base octal
elif opcao == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:])) # hex() para obter base hexadecimal
else: 
    print("Opção INVÁLIDA! escolha [1] para BINÁRIO, [2] para OCTAL ou [3] para HEXADECIMAL") # Menssagem que é exibida caso o usuário selecione uma opção fora das disponíveis.