from datetime import date

nascimento = int(input("Digite o ano do seu nascimento: ")) # Ano de nascimento
atual = date.today().year #Pegando o ano atual
idade = atual - nascimento # idade do usuário
print("Quem nasceu em {} tem {} anos em {} ".format(nascimento, idade, atual))

if idade < 18:
    saldo = 18 - idade #Calcula quanto falta para chgar aos 18
    alist =  idade + atual #Calcula o ano em que será o alistamento
    print("Faltam {} anos para você poder se alistar".format(saldo))
    print("Seu alistamento será em {}".format(alist))
elif idade > 18:
    saldo = idade - 18 #Calcula quanto passou dos 18
    alist = atual - idade #Calcula o ano em que o alistaento deveria ter ocorrido
    print ("Você deveria ter se alistado ao há {} anos".format(saldo))
    print("Seu alistamento foi em {}".format(alist))
else:
    print ("Você está apto para se alistar neste ano") #Caso a idade seja exatamente 18 anos




