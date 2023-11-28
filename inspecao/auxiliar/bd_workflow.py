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

    def fecha(self, conexao):
        self.cursor = conexao
        self.cursor.close()
