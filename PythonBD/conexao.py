import mysql.connector #conecta com o banco de dados
from mysql.connector import errorcode

class conexao:
    def __init__(self):
        pass


    def conectar(self):
        try:
            self.db_connection = mysql.connector.connect(host = 'localhost',
                                                         user = 'root',
                                                         password = '',
                                                         database = 'bdTI14TPython')
            print('Conectado com sucesso.')
            return self.db_connection
        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_BAD_DB_ERRO: #caso o banco de dados nao exista
                print('Banco de dados não existe.\n Erro: {}'.format(erro))
            elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR: #há um erro de usuário
                print('Nome de usuário ou senha inválido. \n Erro: {}'.format(erro))
            else:
                print(erro)
        else:
            self.db_connection.close() #fechando conexao com o banco de dados
