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

    def verifica_lote(self, conexao, lote):
        try:
            self.cursor = conexao.cursor()
            consulta = f"SELECT * FROM recebimento WHERE lote = '{lote}'"
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

    def salva_lote(self, conexao, context):
        try:
            self.cursor = conexao.cursor()
            try:
                consulta = f"INSERT INTO recebimento (" \
                           f"fornecedor, plcq, lote, quando, nota, oc, quantidade, " \
                           f"inspecionado, defeito, material, rnc, " \
                           f"med_forma_1, med_valor_1, med_laudo_1, " \
                           f"med_forma_2, med_valor_2, med_laudo_2, " \
                           f"med_forma_3, med_valor_3, med_laudo_3, " \
                           f"med_forma_4, med_valor_4, med_laudo_4, " \
                           f"med_forma_5, med_valor_5, med_laudo_5, " \
                           f"med_forma_6, med_valor_6, med_laudo_6, " \
                           f"med_forma_7, med_valor_7, med_laudo_7, " \
                           f"med_forma_8, med_valor_8, med_laudo_8, " \
                           f"med_forma_9, med_valor_9, med_laudo_9, " \
                           f"med_forma_10, med_valor_10, med_laudo_10, " \
                           f"med_forma_11, med_valor_11, med_laudo_11, " \
                           f"med_forma_12, med_valor_12, med_laudo_12, " \
                           f"med_forma_13, med_valor_13, med_laudo_13, " \
                           f"med_forma_14, med_valor_14, med_laudo_14, " \
                           f"med_forma_15, med_valor_15, med_laudo_15, " \
                           f"laudo_final, obs_final, liberacao_condicional, liberacao, usuario) " \
                           f"VALUES ('{context.get('fornecedor', '')}', '{context.get('plcq', '')}', " \
                           f"'{context.get('lote', '')}', '{context.get('quando', '')}', " \
                           f"'{context.get('nota', '')}', '{context.get('oc', '')}', " \
                           f"'{context.get('quantidade', '')}', '{context.get('inspecionado', '')}', " \
                           f"'{context.get('defeito', '')}', '{context.get('material', '')}', '{context.get('rnc', '')}', " \
                           f"'{context.get('med_forma_1', '')}', '{context.get('med_valor_1', '')}', '{context.get('med_laudo_1', '')}', " \
                           f"'{context.get('med_forma_2', '')}', '{context.get('med_valor_2', '')}', '{context.get('med_laudo_2', '')}', " \
                           f"'{context.get('med_forma_3', '')}', '{context.get('med_valor_3', '')}', '{context.get('med_laudo_3', '')}', " \
                           f"'{context.get('med_forma_4', '')}', '{context.get('med_valor_4', '')}', '{context.get('med_laudo_4', '')}', " \
                           f"'{context.get('med_forma_5', '')}', '{context.get('med_valor_5', '')}', '{context.get('med_laudo_5', '')}', " \
                           f"'{context.get('med_forma_6', '')}', '{context.get('med_valor_6', '')}', '{context.get('med_laudo_6', '')}', " \
                           f"'{context.get('med_forma_7', '')}', '{context.get('med_valor_7', '')}', '{context.get('med_laudo_7', '')}', " \
                           f"'{context.get('med_forma_8', '')}', '{context.get('med_valor_8', '')}', '{context.get('med_laudo_8', '')}', " \
                           f"'{context.get('med_forma_9', '')}', '{context.get('med_valor_9', '')}', '{context.get('med_laudo_9', '')}', " \
                           f"'{context.get('med_forma_10', '')}', '{context.get('med_valor_10', '')}', '{context.get('med_laudo_10', '')}', " \
                           f"'{context.get('med_forma_11', '')}', '{context.get('med_valor_11', '')}', '{context.get('med_laudo_11', '')}', " \
                           f"'{context.get('med_forma_12', '')}', '{context.get('med_valor_12', '')}', '{context.get('med_laudo_12', '')}', " \
                           f"'{context.get('med_forma_13', '')}', '{context.get('med_valor_13', '')}', '{context.get('med_laudo_13', '')}', " \
                           f"'{context.get('med_forma_14', '')}', '{context.get('med_valor_14', '')}', '{context.get('med_laudo_14', '')}', " \
                           f"'{context.get('med_forma_15', '')}', '{context.get('med_valor_15', '')}', '{context.get('med_laudo_15', '')}', " \
                           f"'{context.get('laudo_final', '')}', '{context.get('obs_laudo', '')}', " \
                           f"'{context.get('liberacao_condicional', '')}', '{context.get('liberacao', '')}', " \
                           f"'{context.get('usuario', '')}') "
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
