#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.
trabalhoX = int(input("Digite o tempo do trabalhoX"))
trabalhoY = int(input("Digite o tempo do trabalhoY"))
trabalhoZ = int(input("Digite o tempo do trabalhoZ"))

soma = trabalhoX + trabalhoY + trabalhoZ
if trabalhoX < 0:
     print("ERRO! Seu tempo foi negativo.")
elif trabalhoY < 0:
     print("ERRO! Seu tempo foi negativo.")
elif trabalhoZ < 0:
     print("ERRO! Seu tempo foi negativo.")
else:
    print("Seu tempo foi:" , soma)

#finalizado

