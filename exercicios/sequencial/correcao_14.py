limite_peso =50
multa_por_kg = 4

peso_peixe = float(input(" informe o peso total: "))

excedente = peso_peixe - limite_peso
multa = excedente * multa_por_kg

print("houveram",excedente," kg de peixe a mais do permitido")
print("O valor da multa é R$",multa)