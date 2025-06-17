#Crie um programa que receba um ano e diga se ele é bissexto.
# (Dica: múltiplos de 4, exceto os múltiplos de 100, a menos que também sejam múltiplos de 400)

AnoB6 = int(input("digite o numero do(e) ano(s): "))

if AnoB6 / 4 == 0 or AnoB6 / 400 == 0:
    print ("esse ano é bissexto. ")
elif AnoB6 / 100 == 0:
    print ("esse ano não é bissexto.")
else:
    print ("esse ano não é bissexto.")
    # finalizado