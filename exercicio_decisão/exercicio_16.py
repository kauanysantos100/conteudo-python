a = float(input("Digite o valor de a: "))
if a == 0:
    print("não é uma equação do segundo grau")
else:
    b = float(input(" Digite u valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta =( b**2 )- (4*a)*c
    print("Delta é: ",delta)

    if delta < 0:
        print(" A equação não possui raízes reais")
    elif delta == 0 :
        x = -b / (2*a)
        print("A equação possui raízes reais")

    else:
        x1 = (-b + delta ) / 2*a
        x2 = ( -b - delta ) / 2*a
        print(" O x1 dessa equação é",x1)
        print(" O x2 dessa equação é ",x2)