cadastros: dict[str, str] = {}

rodando = True

def cadastro():
    print('Cadastrando...')
    var_login = str(input('Login: '))
    var_senha = str(input('Senha: '))

    try:
        if var_login in cadastros.keys():
            raise Exception('\nLogin já cadastrado')
        
    except Exception as e:
        print('\nErro ao cadastrar: ', e)

    cadastros[var_login] = var_senha
    return

def login():
    print('Logando...')
    var_login = str(input('Login: '))
    var_senha = str(input('Senha: '))

    try:
        if var_login not in cadastros.keys():
            raise Exception('\nEsse login não existe')
            
        if cadastros[var_login] != var_senha:
            raise Exception('\nSenha incorreta')

        print('\nLogin realizado com sucesso!')
    except Exception as e:
        print(e)

while (rodando):

    print('-------------')
    print("1.: Cadastrar")
    print("2.:     Logar")
    print("0.:      Sair")
    print('-------------\n')
    selecao = int(input('Escolha: '))
    
    match (selecao):
        case 1:
            cadastro()
        case 2:
            login()
        case 0:
            rodando = False
            break
        case _:
            print('\nOpção inválida, escolha uma opção válida')
