import psycopg2

class Connection():

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                user="postgres",
                password="ads",
                host="127.0.0.1",
                port="5432",
                database="banco_livro")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

        except:
            print('Falha na conexão')

    def inserir(self, query):
        try:
            self.cursor.execute(query)
        except:
            print('Falha ao inserir')

    def deletar(self, query):
        try:
            self.cursor.execute(query)
        except:
            print('Falha ao deletar')

    def mostrar_tudo(self, query):
        try:
            result = self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result

        except:
            return ('Falha ao mostrar tudo')

    def mostra_um(self, query):
        try:
            result = self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result

        except:
            return ('Falha ao mostrar tudo')


    def atualizar(self, query):
        try:
            self.cursor.execute(query)
        except:
            print('Falha ao atualizar')
