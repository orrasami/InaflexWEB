import pymysql.cursors


class BDPedidos:
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
        return self.conn

    def fecha(self, conexao):
        self.cursor = conexao
        self.cursor.close()

    def verifica_orcamento(self, conexao, orcamento):
        try:
            print(orcamento)
            self.cursor = conexao.cursor()
            consulta = f"SELECT * FROM liberacao_pedidos WHERE orcamento = '{orcamento}'"
            self.cursor.execute(consulta)
            conexao.commit()
            resultados = self.cursor.fetchall()
            if resultados != ():
                mensagem = 1
                return mensagem, resultados
            else:
                mensagem = 2
                return mensagem, resultados
        except:
            resultados = []
            mensagem = 3
            return mensagem, resultados

    def salva_orcamento(self, conexao, context):
        try:
            self.cursor = conexao.cursor()
            try:
                consulta = f"INSERT INTO liberacao_pedidos (" \
                           f"quando, responsavel, obs, orcamento, " \
                           f"ckl_01, ckl_02, ckl_03, ckl_04, " \
                           f"ckl_05, ckl_06, ckl_07, ckl_08, " \
                           f"ckl_09, ckl_10, ckl_11, ckl_12, " \
                           f"ckl_13, ckl_14, ckl_15, ckl_16) " \
                           f"VALUES ('{context.get('quando', '')}', '{context.get('usuario_logado', '')}', " \
                           f"'{context.get('obs', '')}', '{context.get('orcamento', '')}', " \
                           f"'{context.get('ckl_01', '')}', '{context.get('ckl_02', '')}', " \
                           f"'{context.get('ckl_03', '')}', '{context.get('ckl_04', '')}', " \
                           f"'{context.get('ckl_05', '')}', '{context.get('ckl_06', '')}', " \
                           f"'{context.get('ckl_07', '')}', '{context.get('ckl_08', '')}', " \
                           f"'{context.get('ckl_09', '')}', '{context.get('ckl_10', '')}', " \
                           f"'{context.get('ckl_11', '')}', '{context.get('ckl_12', '')}', " \
                           f"'{context.get('ckl_13', '')}', '{context.get('ckl_14', '')}', " \
                           f"'{context.get('ckl_15', '')}', '{context.get('ckl_16', '')}') "
                self.cursor.execute(consulta)
                conexao.commit()
                mensagem = '1'
                return mensagem
            except:
                mensagem = '2'
                return mensagem
        except:
            mensagem = '3'
            return mensagem
