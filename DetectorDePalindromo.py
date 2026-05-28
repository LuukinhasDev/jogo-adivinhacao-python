frase = str(input('Digite uma palavra ou frase: ')).strip().upper() # Recebe a frase, remove espaços inuteis e deixa tudo em maiuscul
Texto = "".join(frase.split()) # divide a frase em listas e junta tudo em uma string removendo espaços

TextoInvertido = "" # Espaço que vai receber o texto invertido
for letra in range(len(Texto) -1, -1, -1): # Lê o texto de trás para frente 
    TextoInvertido += Texto[letra] # Texto invertido armazenado
print('O inverso de {} é {}'.format(Texto, TextoInvertido))

# Compara se o texto normal e o invertido são iguais
if Texto == TextoInvertido: 
    print("O texto digitado é um PALÍNDROMO.")
else:
    print("O texto digitado não é um PALÍNDROMO.")