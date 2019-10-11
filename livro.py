import psycopg2
from conexao import Connection

class Livro():

    def cadastrar(self, autor, tipo):
        try:
            conexao = Connection()
            conexao.inserir("insert into livro (autor, tipo) values ('{0}', '{1}');".format(autor, tipo))

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)


    def deletar(self, id):
        try:
            conexao = Connection()
            conexao.deletar("delete from livro where id = {0};".format(id))

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)


    def mostrar_tudo(self):
        try:
            conexao = Connection()
            result = conexao.mostrar_tudo('select * from livro')
            for row in result:
                print("Id = ", row[0], )
                print("Autor = ", row[1])
                print("Tipo  = ", row[2], "\n")

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)

    def find_one(self, id):
        try:
            conexao = Connection()
            result = conexao.mostra_um('select * from livro where id = {0}'.format(id))
            print("Id = ", result[0][0], )
            print("Autor = ", result[0][1])
            print("Tipo  = ", result[0][2], "\n")

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)

    def atualizar(self, id, autor, tipo):
        try:
            conexao = Connection()
            conexao.atualizar('update livro set autor = {0}, tipo = {1} where id = {2}'.format(autor, tipo, id))

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)

