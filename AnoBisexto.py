from datetime import date #Módulo para pegar o ano atual da máquina
ano = int(input("Qual ano você gostaria de analizar? Coloque 0 para analizar o ano atual: "))
if ano == 0:
    ano = date.today().year #Pega o ano atual caso o usuário digite 0
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): #Condição para um ano ser ou não Bissexto.
    print("O ano de {} é um ano Bissexto!".format(ano))
else:
    print("O ano de {} é um ano normal (365 dias)!".format(ano))