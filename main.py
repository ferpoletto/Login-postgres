from login import *
from validacoes import *
from usuario import *


def portal():
    print('='*30)
    print('{:^30}'.format('PÁGINA DE LOGIN'))
    print('='*30)


login = Login()
garanta = Validacoes()
usuario = Usuario()

while True:
    portal()
    user = input("Usuário: ")
    password = input("Senha: ")

    if garanta.valida_user_existe(user) == 0:
        print("Usuário não encontrado.")
    else:

            if login.autenticacao(user, password) == 1:
                opcao = usuario.menu_usuario()
                if opcao == 1:
                    print('=' * 30)
                    print('{:^30}'.format('CADASTRO DE USUARIO'))
                    print('=' * 30)

                elif opcao == 2:
                    print('=' * 30)
                    print('{:^30}'.format('EXCLUIR USUARIO'))
                    print('=' * 30)

                elif opcao == 3:
                    print('=' * 30)
                    print('{:^30}'.format('ALTERAR USUARIO'))
                    print('=' * 30)

                elif opcao == 4:
                    print('=' * 30)
                    print('{:^30}'.format('MOSTRAR USUARIO'))
                    print('=' * 30)

                elif opcao == 5:
                    break
                else:
                    print("Opção inválida.")
        else:
            print("Senha inválida!")




