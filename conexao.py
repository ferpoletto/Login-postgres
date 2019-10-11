import psycopg2

class Connection():

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                user="postgres",
                password="ads",
                host="127.0.0.1",
                port="5432",
                database="login")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

        except:
            print('Falha na conexão')