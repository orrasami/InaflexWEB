import pymysql.cursors


class BDWorkflow:
    def __init__(self):
        self.conn = pymysql.connect(
            host='mysql.inaflex-app.kinghost.net',
            user='inaflexapp',
            password='zt4cr3',
            db='inaflexapp',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

    def conectar(self):
        self.conn = pymysql.connect(
            host='mysql.inaflex-app.kinghost.net',
            user='inaflexapp',
            password='zt4cr3',
            db='inaflexapp',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()
        return self.cursor

    def login(self, conexao, usuario, senha):
        try:
            self.cursor = conexao
            consulta = f"SELECT senhaUsuario, id FROM usuarios WHERE nomeUsuario = '{usuario}'"
            self.cursor.execute(consulta)
            self.conn.commit()
            resultados = self.cursor.fetchall()
            senha_login = resultados[0]['senhaUsuario']
            if senha_login == senha:
                mensagem = 1
                return mensagem
            else:
                mensagem = 2
                return mensagem
        except:
            mensagem = 3
            return mensagem

    def fecha(self, conexao):
        self.cursor = conexao
        self.cursor.close()
