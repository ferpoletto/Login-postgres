from portal import *
from menu import *

while True:
    portal = Portal()

    usuario_e_senha = portal.menu_portal()
    if portal.valida_usuario_existe(usuario_e_senha['Usuario']) == 1:
        if portal.autenticar(usuario_e_senha['Usuario'], usuario_e_senha['Senha']) == 0:
            print('Senha inválida')

        elif portal.autenticar(usuario_e_senha['Usuario'], usuario_e_senha['Senha']) == 1:
            print('Login efetuado com sucesso!')

            if usuario_e_senha['Usuario'] == 'admin':
                print('Acessando sistema no modo ADM')
                menu_ADM = Menu()
                op = 0
                while op != 6:
                    op = menu_ADM.mostra_menu_ADM()
                    menu_ADM.opcoes_ADM(op)

            else:
                print('Bem vindo, usuário!')
                menu_USER = Menu()
                menu_USER.mostra_menu_USER()



    elif portal.valida_usuario_existe(usuario_e_senha['Usuario']) == 0:
        print('Usuário não encontrado!')









