from conexao import *
from pprint import pprint

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

    def alterar_usuario(self, nome, novo_nome, nova_senha, novo_email, novo_flinativo):
        try:
            self.bd = Connection()
            self.query ="update usuario set nome = '{0}', senha = '{1}', email = '{2}', flinativo = '{3}' where nome = '{4}'".format(novo_nome, nova_senha, novo_email, novo_flinativo, nome)
            self.bd.executarSQL(self.query)
            print('Usuário atualizado!')

        except:
            print('Erro ao atualizar o usuário')
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

    def mostrar_usuarios(self):
        try:
            self.bd = Connection()
            self.query = 'select * from usuario'
            self.resultado = self.bd.executarSQLRetorno(self.query)
            for user in self.resultado:
                print('=' * 30)
                print(f'ID: {user[0]}')
                print(f'Nome: {user[1]}')
                print(f'Senha: {user[2]}')
                print(f'Email: {user[3]}')
                print(f'Inativo: {user[4]}')

        except:
            print('Erro ao mostrar todos os usuário')
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

