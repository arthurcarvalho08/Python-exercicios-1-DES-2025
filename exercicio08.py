# Talita está simulando o custo de frete para sua loja virtual. O valor depende da distância:

# Até 50 km: R$ 5,00
# De 51 a 150 km: R$ 15,00
# Acima de 150 km: R$ 25,00

distancia = int(input("Digite a distancia em KM"))

if distancia <= 50 :
    print("O preço do frete seria a 5 reais.")
elif distancia <= 150 : 
    print("o prço do frete será 15 reais.")
else:
    print("O preço do frete será 25 reais.")
#finalizado