valor1 = int(input('Primeiro valor: '))
valor2 = int(input('segundo valor: '))
opcao = 0

while opcao != 5:
    # Menu de opções que é exibido enquanto o valor da opção não for 5
    print(''' 
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    # Caso a opção 1 seja selecionada
    if opcao == 1:
        soma = valor1 + valor2
        print('A soma entre {} + {} é {}'.format(valor1, valor2, soma))
    # Caso a opção 2 seja selecionada
    elif opcao == 2:
        multiplicar = valor1 * valor2
        print('A multiplicação entre {} x {} é {}'.format(valor1, valor2, multiplicar))    
    # Caso a opção 3 seja selecionada
    elif opcao == 3:
        # comparação para saber o maior valor ou se são iguais
        if valor1 > valor2:
            maior = valor1
            print('O maior valor entre {} e {} é {}'.format(valor1, valor2, maior))
        elif valor2 > valor1:
            maior = valor2
            print('O maior valor entre {} e {} é {}'.format(valor2, valor1, maior))
        else:
            print('Os valores são iguais')
    # Caso a opção 4 seja selecionada
    elif opcao == 4:
        # Retorna para a escolha de novos números
        print('Por favor, informe os valores novamente')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('segundo valor: '))
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)
# Caso a opção 5 seja selecionada
print('Programa finalizado com sucesso!')