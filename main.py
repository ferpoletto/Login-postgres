from portal import *

while True:
    portal = Portal()

    usuario_e_senha = portal.menu_portal()

    if portal.autenticar(usuario_e_senha['Usuario'], usuario_e_senha['Senha']) == 0:
        print('Login falhou')
    else:
        print('Login efetuado com sucesso!')










