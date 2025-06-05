# Gabriel está acompanhando o desempenho de dois cursos online que lançou: Python Básico e JavaScript Essencial.
# Ele quer saber qual curso teve mais avaliações no último mês.

# Crie um programa que receba o número de avaliações de cada curso e exiba qual teve mais.
# Caso as quantidades sejam iguais, exiba uma mensagem dizendo que houve empate.

curso01 = int(input("Digite a quantidade de acessos do curso01."))
curso02 = int(input("Digite a quantidade de acessos do curso02."))

if curso01 > curso02 :
    print("Curso01 teve mais acessos.")
elif curso02 > curso01 : 
    print("Curso02 teve mais acessos.")
else:
    print("Ambos os cursos tem a mesma quantidade de acessos.")

#finalizado

