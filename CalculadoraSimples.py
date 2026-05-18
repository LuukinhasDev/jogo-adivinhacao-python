num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operação = input("Digite a operação desejada: ")

match operação: #Com base na operaão digitada o calculo é direcionado para um dos cases
    case "+":
        res = num1 + num2
    case "-":
        res = num1 - num2
    case "*":
        res = num1 * num2
    case "/":
        res = num1 / num2
    case "%":
        res = num1 % num2
    case "**":
        res = num1 ** num2
print("-=-" * 20)
print("O Resultado é igual a {}".format(res))
print("-=-" * 20)
