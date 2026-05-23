print("-=-"*20)
print("Analizador de Triangulos")
print("-=-"*20)

segmento1 = float(input("Primeiro segmento: "))
segmento2 = float(input("Segundo segmento: "))
segmento3 = float(input("Terceiro segmento: "))

#Cada lado precisa ser menor do que a soma dos outros dois
if (segmento1 < segmento2+segmento3) and (segmento2 < segmento1+segmento3) and (segmento3 < segmento2+segmento1):
    print("Os segmentos acima podem formar um triãngulo")
else:
    print("Os segmentos acima não podem formar um triângulo")
