from conexao import *
from pprint import pprint

class Portal:
    
    def __init__(self):
        self.usuario = None
        self.senha = None
    
    def menu_portal(self):
        print('=' * 30)
        print('{:^30}'.format('PÁGINA DE LOGIN'))
        print('=' * 30)
        
        self.usuario = input("USUARIO: ")
        self.senha = input("SENHA: ")
        
        self.dicionario = {'Usuario': self.usuario, 'Senha':self.senha}
        
        return self.dicionario

    def autenticar(self, usuario, senha):
        try:
            self.bd = Connection()
            self.query = "SELECT senha FROM usuario WHERE nome = '{0}'".format(usuario)
            senha_cadastrada = self.bd.executarSQLRetorno(self.query)
            if senha_cadastrada[0][0] == senha:
                return 1
            else:
                return 0
        except:
            print('Erro ao autenticar')
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()
