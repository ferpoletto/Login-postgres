from Teste.conexao import *

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
    
    def valida_usuario_existe(self, usuario):
        try:
            self.conexao = Connection()
            lista_usuarios = self.conexao.executarSQL('select nome from usuario')
            flag = 0
            for i in range(len(lista_usuarios)):
                if lista_usuarios[i][0] == usuario:
                    flag = 1
            return flag
        except:
            print('Erro ao validar usuario existente')
        finally:
            if self.conexao:
                self.conexao.cursor.close()
                self.conexao.connection.close()


        
    def autenticacao(self, usuario, senha):
        try:
            self.conexao = Connection()
            login = self.conexao.executarSQL("select senha from usuario where nome = {0}".format(usuario))
            print(login)


            if senha == login[1][0]:
                return 1
            else:
                return 0
        except:
            print('Erro ao executar autenticação')
        finally:
            if self.conexao:
                self.conexao.cursor.close()
                self.conexao.connection.close()
        