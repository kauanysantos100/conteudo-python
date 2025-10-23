salario = float(input("Digite o salario atual do colaborador: R$ "))

# Definição das faixase percentuais
if salario <= 1450.00:
    percentual = 20
elif salario <= 2800.00:
    percentual = 15
elif salario <= 3500.00:
    percentual = 10
else:
    percentual = 5

valor_aumento = salario * (percentual / 100)
novo_salario = salario + valor_aumento

print(" o salario novo será igual a: ",novo_salario)