from portal import *

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

            else:
                print('Bem vindo, usuário!')
    elif portal.valida_usuario_existe(usuario_e_senha['Usuario']) == 0:
        print('Usuário não encontrado!')









