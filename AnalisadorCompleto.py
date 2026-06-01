somaidade = 0
maisVelho = 0
nomeMaisVelho = ''
contMulher = 0
for p in range(1, 5):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    # Soma todas as idades e calcula a média
    somaidade += idade 
    media = somaidade / 4
    # Chega a idade e o nome do homem mais velho
    if sexo == 'M':
        if p == 1:
            maisVelho = idade
            nomeMaisVelho = nome
        
        if idade > maisVelho:
            maisVelho = idade
            nomeMaisVelho = nome
    # Verifica quando uma mulher é ou não menor de 20 anos e conta   
    if sexo == "F":
        if idade < 20:
            contMulher += 1
print('-'*40)
print('A média de idade do grupo é de {:.1f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maisVelho, nomeMaisVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(contMulher))