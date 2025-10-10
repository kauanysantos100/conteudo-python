valor_hora = float(input("digite o valor do salario: "))
horas_trabalhadas = float(input("digiteo tanto de horas trabalhadas:  "))


# parte A
salario_bruto = valor_hora * horas_trabalhadas
print("o salario bruto do funcionario sera igual a:", salario_bruto)

# parte B
pagou_INSS = salario_bruto * 0.08
print("o valor que o funcionario pagará ao INSS será de: ",pagou_INSS)

# parte C
pagou_sindicato = salario_bruto * 0.05
print(" o valor que o funcionario pagaá ao sindicato será de: ",pagou_sindicato)
ir = 0.11

# parte D
salario_liquido = salario_bruto - pagou_INSS - pagou_sindicato - ir
print("o salario liquido do funcionario será de: " ,salario_liquido)