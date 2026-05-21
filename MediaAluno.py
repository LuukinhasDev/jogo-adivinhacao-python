n1 = float(input("primeira nota: "))
n2 = float(input("segunda nota: "))
media = (n1 + n2)/2
print("Quem tirou {:.1f} e {:.1f} ficou com média {:.1f}".format(n1, n2, media))
if media < 5:
    print("Aluno REPROVADO!")
elif media < 7:
    print("Aluno está de RECUPERAÇÃO!")
else:
    print("Aluno APROVADO!!!")
