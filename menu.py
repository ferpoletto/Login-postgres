class Menu:

    def mostra_menu_ADM(self):
        print('=' * 30)
        print('{:^30}'.format('MENU DO ADM'))
        print('=' * 30)
        op = int(input('1 - CADASTRAR NOVO USUARIO\n'
                       '2 - EXCLUIR USUARIO\n'
                       '3 - ALTERAR USUARIO\n'
                       '4 - VER USUARIOS CADASTRADOS\n''
                       '5 - FAZER LOGOFF\n'
                       'Digite a opção desejada: '))

    def mostra_menu_USER(self):
        print('=' * 30)
        print('{:^30}'.format('MENU DO USUARIO'))
        print('=' * 30)
