sexo = ''
# Enquanro sexo não estiver em ['M', 'F']
while sexo not in ['M', 'F']:
    sexo = str(input('Informe o seu sexo: [M/F]: ')).strip().upper()
# Se sexo não estivem em ['M', 'F']
    if sexo not in ['M', 'F']:
        print('Dados inválidos, Tente novamente!')
# Se sexo for 'M' ou 'F'
print('Sexo {} registrado com sucesso'.format(sexo))
