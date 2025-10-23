valor_horas = float(input(" Digite o valor de cada hora trabalhadas : "))
horas_trabalhadas = float(input("Digite o tento de horas trabalhadas: "))

salario_bruto = valor_horas + horas_trabalhadas

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = (salario_bruto * 0.05) -salario_bruto
elif  salario_bruto <= 2500 :
    ir = (salario_bruto * 0.10)
elif salario_bruto > 2500 :
    ir = (salario_bruto * 0.20)

sindicato = salario_bruto * 0.03

FGTS = salario_bruto * 0.11

descontos = ir + FGTS

salario_liquido = salario_bruto - descontos

print(" o salario bruto é: ", valor_horas * horas_trabalhadas)
print("o salario com o desconto do ir fica:", ir)
print("o salario com o desconto o desconto do sindicato fica: ", sindicato)
print("osalario com o desconto do FGTS fica: " ,FGTS)
print("o salario líquido é de: ",salario_liquido)


