segmento1 = float(input("primeiro segmento: "))
segmento2 = float(input("segundo segmento: "))
segmento3 = float(input("terceiro segmento: "))

if (segmento1 < segmento2+segmento3) and (segmento2 < segmento1+segmento3) and (segmento3 < segmento1+segmento2):
    print("Os segmentos acima podem formar um triângulo ", end="")
    if (segmento1 == segmento2 == segmento3):
        print("EQUILÁTERO.")
    elif (segmento1 == segmento2) or (segmento1 == segmento3) or (segmento3 == segmento2):
        print("ISÓSCELES.")
    elif (segmento1 != segmento2) and (segmento1 != segmento3) and (segmento3 != segmento2):
        print("ESCALENO.")
else:
    print("Os segmentos acima não podem formar um triângulo.")
