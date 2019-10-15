from administrador import *

class Menu:

    def mostra_menu_ADM(self):
        print('=' * 30)
        print('{:^30}'.format('MENU DO ADM'))
        print('=' * 30)
        op = int(input('1 - CADASTRAR NOVO USUARIO\n'
                       '2 - INATIVAR USUARIO\n'
                       '3 - ALTERAR USUARIO\n'
                       '4 - VER USUARIOS CADASTRADOS\n'
                       '5 - ATIVAR USUARIO\n'
                       '6 - FAZER LOGOFF\n'
                       'Digite a opção desejada: '))
        return op

    def opcoes_ADM(self, op):

        adm = Administrador()

        if op == 1:
            print('=' * 30)
            print('{:^30}'.format('CADASTRAR NOVO USUARIO'))
            print('=' * 30)
            nome = input('Nome: ')
            senha = input('Senha: ')
            email = input('Email: ')

            adm.cadatrar_usuario(nome, senha, email)

        elif op == 2:
            print('=' * 30)
            print('{:^30}'.format('INATIVAR USUÁRIO'))
            print('=' * 30)
            nome = input("Digite o nome para INATIVAR: ")
            adm.inativar_usuario(nome)

        elif op == 3:
            print('=' * 30)
            print('{:^30}'.format('ALTERAR USUÁRIO'))
            print('=' * 30)
            nome = input("Digite o nome para alterar: ")
            novo_nome = input("Digite o novo nome: ")
            nova_senha = input("Digite a nova senha: ")
            novo_email = input("Digite o novo email: ")
            novo_flinativo = input("Digite o novo status do usuário inativo [S/N]: ")

            adm.alterar_usuario(nome, novo_nome, nova_senha, novo_email, novo_flinativo)

        elif op == 4:
            print('=' * 30)
            print('{:^30}'.format('VER USUARIOS CADASTRADOS'))
            print('=' * 30)
            adm.mostrar_usuarios()

        elif op == 5:
            print('=' * 30)
            print('{:^30}'.format('ATIVAR USUARIO'))
            print('=' * 30)
            nome = input("Digite o nome para ATIVAR: ")
            adm.ativar_usuario(nome)

        elif op == 6:
            print('Saindo do modo ADM')

        else:
            print('Opçao inválida!')


    def mostra_menu_USER(self):
        print('=' * 30)
        print('{:^30}'.format('MENU DO USUARIO'))
        print('=' * 30)
        print('Modulo em construção')
