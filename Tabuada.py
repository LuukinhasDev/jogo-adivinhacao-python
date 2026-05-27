num = int(input("Digite um número: "))
intervalo = int(input("Digite até onde quer que a tabuada vá: ")) + 1 # Valor que vai definir o fim do intervalo
for n in range(1, intervalo):
    resultado = num * n
    print(f"{num} x {n} = {resultado}")