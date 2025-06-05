#Peça a idade do usuário e diga se ele pode se cadastrar em um site:
#Permitido: 13 anos ou mais

idade = 13
idade = int(input("Digite sua idade."))

if idade >= 13 :
    print("Acesso permitido.")
elif idade < 13 :
    print("Ops, sua idade não corresponde aos nossos requisitos *SAIR*.")

#finalizado