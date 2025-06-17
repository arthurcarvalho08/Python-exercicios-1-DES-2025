#Peça ao usuário uma senha e verifique se ela contém pelo menos 8 caracteres.
#Exiba uma mensagem de "Senha válida" ou "Senha muito curta".

senha = input("digite sua senha, sua senha tem um numero de terminado de digitos:")

quantidade = len(senha)

if quantidade > 8:
    print ("senha muito longa")
elif quantidade < 8:
    print ("senha muito curta")
else:
    print("senha valida")
    # finalizado