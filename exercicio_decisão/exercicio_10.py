turno = input("você estuda em que turno? (M - Matutino, - V - vespertino, N - Noturno): ")
if turno =='M':
    print("Bom dia!")
elif turno == 'V':
    print("Boa tarde!")
elif turno =='N':
    print("Boa noite!")
else:
    print("Opção inválida! Por favor, digite M,V ou N. ")