
qtd_litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustivel( A - alcool, G - gasolina) ")

desconto = 0

if tipo == "A":
    if qtd_litros <= 20:
        desconto = 0.03
    else:
     desconto = 0.05
        preco_litros = qtd_litros * preco_alcool
        preco_total = preco_litros * (preco_litros * desconto)
elif tipo =="G":
    if qtd_litros <= 20:
        desconto = 0.06
    else:
        desconto = 0.0
preco_litros = qtd_litros * preco_gasolina
preco_total = preco_litros * desconto

if preco_total > 0:
    print("Valor a pagar é: ", preco_total)
