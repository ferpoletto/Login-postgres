from Teste.portal import *

while True:
    portal = Portal()

    usuario_e_senha = portal.menu_portal()
    
    usuario_existe = portal.valida_usuario_existe(usuario_e_senha['Usuario'])

    if usuario_existe == 0:
        print("USUARIO não encontrado. Tente novamente!")
    elif usuario_existe == 1:
        autenticado = portal.autenticacao(usuario_e_senha['Usuario'], usuario_e_senha['Senha'])
        if autenticado == 1:
            print('SUCESSO')
        else:
            print('LOGIN FALHOU')
