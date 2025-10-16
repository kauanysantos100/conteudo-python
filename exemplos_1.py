nn_1 = int(input("Digite o valor da nota: "))
nn_2 = int(input("Digite o valor da nota: "))
nn_3 = int(input("Digite o valor da nota: "))
nn_4 = int(input("Digite o valor da nota: "))

media = int(nn_1 + nn_2 + nn_3 + nn_4) /4


if  media >= 7:
    print(" O aluno está aprovado")

elif media >= 3:
    print("em exame")

else:
    print("reprovado")