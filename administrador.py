from conexao import *

class Administrador():


    def cadatrar_usuario(self, nome, senha, email):

        try:
            self.bd = Connection()
            self.query = "INSERT INTO usuario(nome, senha, email, flinativo) VALUES ('{0}','{1}','{2}','N')".format(nome, senha, email)
            self.bd.executarSQL(self.query)
            print(f'Cadastro do {nome} realizado com sucesso!')
        except:
            print('Erro ao cadastrar usuário')
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

    def inativar_usuario(self, nome):
        try:
            self.bd = Connection()
            self.query = "update usuario set flinativo = 'S' where nome = '{0}'".format(nome)
            self.bd.executarSQL(self.query)
            print(f'Usuário {nome} está inativo!')
        except:
            print('Erro ao cadastrar usuário')
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

    def ativar_usuario(self, nome):
        try:
            self.bd = Connection()
            self.query = "update usuario set flinativo = 'N' where nome = '{0}'".format(nome)
            self.bd.executarSQL(self.query)
            print(f'Usuario {nome} está ativo!')
        except:
            print('Erro ao cadastrar usuário')
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

    def alterar_usuario(self, nome, novo_nome, nova_senha, novo_email):
        pass

    def mostrar_usuarios(self):
        pass


