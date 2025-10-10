peso_peixe = float(input(" qual é o valor da sua carga: "))
peso_maximo = 50.0
valor_multa = 4

if  peso_peixe > peso_maximo:
    execesso = peso_peixe -  peso_maximo
    multa = execesso * valor_multa
    print("peso maximo excedido por", execesso)
    print(" sua multa é r$", multa)

else:
    print("você não passou do limite permitido")

