from login import *
from usuario import *
from validacoes import *


def menu():

    op = int(input("1 - FAZER LOGIN\n"
                   "2 - CADASTRAR USUARIO\n"
                   "3 - INATIVAR USUARIO\n"
                   "4 - ALTERA USUARIO\n"
                   "5 - VER DADOS DO USUARIO\n"
                   "6 - SAIR\n"
                   "\nDigite a opção desejada: "))

    return op

user = Usuario()
valida = Validacao()

while True:

    op = menu()

    if op == 1:
        print(f'LOGIN')
        #Input das informações para autenticação
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")

        #Chama método autenticar da classe login para validar login
        login = Login()

        if login.autenticar(usuario, senha) == 1:






    elif op == 2:
        print(f'CADASTRAR USUARIO')
        #Input de dados
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        email = input("Digite o email: ")
        #Quando cadastra o usuário fica como ativo sempre
        flag_ativo = 1


        #chama o cadastro de usuário
        resultado = user.cadastrar(nome, cpf, email, flag_ativo)
        print(resultado)

    elif op == 3:
        print(f'INATIVAR USUÁRIO')
        nome_inativar = input("Digite o nome para inativar: ")

        #chama o método inativar
        resultado = user.inativar(nome_inativar)
        print(resultado)

    elif op == 4:
        print("ALTERA USUARIO")


    elif op == 5:
        print("VER DADOS DO USUARIO")
        find = input("Digite o nome para visualizar oa dados: ")

        #valida se o nome existe no banco
        resultado = valida.valida_usuario_existe(find)

        if resultado == 1:
            user.mostrar(find)
        else:
            print("Usuário inexistente!")





    elif op == 6:
        print('Finalizando...')
        break

    else:
        print("Opção inválida. Tente novamente!")

print('FIM!')
