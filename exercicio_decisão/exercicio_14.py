nota_1 = float(input(" Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2) / 2
conceito = ''
if media >= 9:
    if media >= 9 and media <= 10:
        conceito = 'a'
if media>= 7.5:
    if media >= 7.5 and media <= 9 :
        conceito = 'b'
if media >= 6:
    if media>= 4 and media <= 6:
        conceito = "c"
if media >= 4 :
    if media >= 4 and media <= 0:
        conceito = 'd'
else:
    conceito = 'e'
if conceito == 'a' or conceito == 'b' or conceito =='c':
    situação = ("reprovado")
else:
    situação = "reprovado"

print("A média do aluno é: ", media)
print("A situação dele é ", situação)