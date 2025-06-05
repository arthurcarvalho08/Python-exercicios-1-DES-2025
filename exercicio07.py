# Uma empresa quer avaliar seus colaboradores com base em três metas atingidas.
# O programa deve calcular a média das três avaliações e exibir:

# Aprovado (>=7)
# Em treinamento (>=5 e <7)
# Reprovado (<5)

meta01 = int(input("Digite a nota 01."))
meta02 = int(input("Digite a nota 02."))
meta03 = int(input("Digite a meta 03."))

if meta01 + meta02 + meta03 >= 7 :
    print("Aprovado.")
elif meta01 + meta02 + meta03 >=5 <7 :
    print("Em treinamento.")
elif meta01 + meta02 + meta03 <5 :
    print("Reprovado.")

