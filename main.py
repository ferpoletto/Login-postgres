from login import *

def menu_login():
    print('='*30)
    print('{:^30}'.format('PÁGINA DE LOGIN'))
    print('='*30)

login = Login()
while True:
    menu_login()
    user = input("Usuário: ")
    password = input("Senha: ")



    if login.autenticacao(user, password) == 1:
        pass
    else:




