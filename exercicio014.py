#Loja oferece os seguintes descontos:
#Compras acima de R$ 500,00 têm 10%
#Acima de R$ 300,00 têm 5%
#Menor ou igual a R$ 300,00 não têm desconto

compra = int(input("Digite o valor da compra em reais."))

if compra >500:
    print("Voce ganhou 10% de desconto.")
elif compra >300:
    print("Voce ganhou 5% de desconto")
else:
    print("Voce nao comseguiu ganhar desconto.")
    # finalizado