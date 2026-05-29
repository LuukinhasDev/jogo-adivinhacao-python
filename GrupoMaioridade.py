from datetime import date

ano_atual = date.today().year # Pega o ano atual
maior_idade = 0 # Contador de maioridade
menor_idade = 0 # Contador de menoridade

# Loop que recebe os anos de nescimento de 7 pessoas calcula a idade e conta quantos passaram dos 18 e quantos não passaram
for i in range(1, 8):
    nascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(i))) 
        
    if (ano_atual - nascimento < 18):
        menor_idade += 1
    else:
        maior_idade += 1
print("="*30)
print("Ao todo tivemos {} pessoas maiores de idade.".format(maior_idade))
print("E também {} pessoas menores de idade.".format(menor_idade))