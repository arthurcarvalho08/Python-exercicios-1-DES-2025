# Bianca está programando o controle de acesso a uma plataforma que só funciona entre 9h e 21h.
# O programa deve receber a hora atual (formato 24h) e informar se o acesso é permitido.

acesso_plataforma = int(input("Digite o horário quer você está tentando acessar a plataforma: "))

if acesso_plataforma == 9:
    print("Horario autorizado.")
elif acesso_plataforma <= 21:
    print("Horario autorizado.")
else:
    print("Horário não autorizado.")
#finalizado
