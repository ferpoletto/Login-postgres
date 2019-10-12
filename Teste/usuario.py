import psycopg2

from Teste.conexao import Connection

class Usuario:

    def cadastrar(self, nome, email, CPF, senha):
        try:
            conexao = Connection()
            conexao.executarSQL('insert into usuario values ({0}, {1}, {2}, {3})'.format(nome, email, CPF, senha))
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)


    def alterar(self):
        pass

    def excluir(self):
        pass

    def mostrar(self):
        pass
