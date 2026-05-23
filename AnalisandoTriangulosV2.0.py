segmento1 = float(input("primeiro segmento: "))
segmento2 = float(input("segundo segmento: "))
segmento3 = float(input("terceiro segmento: "))

if (segmento1 < segmento2+segmento3) and (segmento2 < segmento1+segmento3) and (segmento3 < segmento1+segmento2): #checa se os segmentos formam um triângulo
    print("Os segmentos acima podem formar um triângulo ", end="")
    if (segmento1 == segmento2 == segmento3): #if dentro de outro if para identificar que tipo de triângulo é
        print("EQUILÁTERO.")
    elif (segmento1 == segmento2) or (segmento1 == segmento3) or (segmento3 == segmento2):
        print("ISÓSCELES.")
    elif (segmento1 != segmento2) and (segmento1 != segmento3) and (segmento3 != segmento2):
        print("ESCALENO.")
else:
    print("Os segmentos acima não podem formar um triângulo.")
