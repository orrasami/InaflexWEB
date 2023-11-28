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
            consulta = f"SELECT * FROM inspecao_final WHERE lote = '{lote}'"
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
        print(context)
        try:
            lote = context['lote']
            self.cursor = conexao.cursor()
            consulta = f"SELECT lote FROM inspecao_final WHERE lote = '{lote}'"
            self.cursor.execute(consulta)
            conexao.commit()
            resultados = self.cursor.fetchall()
            if resultados:
                try:
                    self.cursor = conexao.cursor()
                    consulta = "UPDATE inspecao_final SET "
                    fields = ["correto", "h_inicial", "h_final", "data", "empatacao", "encaixe",
                              "encaixe_obs", "solda", "solda_obs", "cordoalha", "cordoalha_obs",
                              "tipado", "tipado_obs", "tag", "tag_obs", "tag_num", "cola", "cola_obs",
                              "pead", "pead_obs", "corda", "corda_obs", "corda_cor", "silicone",
                              "silicone_obs", "cupilha", "cupilha_obs", "drenado", "drenado_obs",
                              "plaqueta", "plaqueta_obs", "plaqueta_info", "plaqueta_info_obs",
                              "diametro", "diametro_obs", "etiquetas", "etiquetas_obs", "modelo",
                              "modelo_obs", "retrabalho", "retrabalho_obs", "data_armazenamento",
                              "embalagem", "embalagem_obs", "pregos", "pregos_obs", "falha",
                              "falha_obs", "responsavel", "responsavel_obs", "qualidade_obs",
                              "inspetor", "data_inspecao", "remetente", "n_pedido", "n_embalagem",
                              "pais_origem", "pais_destino", "liquido", "bruto", "dimensoes",
                              "simbolos", "tipo_embalagem", "cintada", "stretch", "foto"]
                    values = []
                    for field in fields:
                        try:
                            value = context[field]
                        except KeyError:
                            continue  # Skip this field if it's not in context
                        values.append(f"{field}='{value}'")
                    consulta += ", ".join(values) + f" WHERE lote='{context['lote']}'"
                    print(consulta)
                    self.cursor.execute(consulta)
                    conexao.commit()
                    mensagem = '1'
                    return mensagem
                except:
                    mensagem = '2'
                    return mensagem
            else:
                try:
                    print(f'fase 1')
                    consulta = f"INSERT INTO inspecao_final (pedido, cliente, cnpj, exigencias, correto, h_inicial, h_final, data, empatacao, encaixe, " \
                               f"encaixe_obs, solda, solda_obs, cordoalha, cordoalha_obs, tipado, tipado_obs, tag, " \
                               f"tag_obs, tag_num, cola, cola_obs, pead, pead_obs, corda, corda_obs, corda_cor, " \
                               f"silicone, silicone_obs, cupilha, cupilha_obs, drenado, drenado_obs, plaqueta, " \
                               f"plaqueta_obs, plaqueta_info, plaqueta_info_obs, diametro, diametro_obs, etiquetas, " \
                               f"etiquetas_obs, modelo, modelo_obs, retrabalho, retrabalho_obs, data_armazenamento, " \
                               f"embalagem, embalagem_obs, pregos, pregos_obs, falha, falha_obs, responsavel, " \
                               f"responsavel_obs, qualidade_obs, inspetor, data_inspecao, lote, usuario_logado, " \
                               f"remetente, n_pedido, n_embalagem, pais_origem, pais_destino, liquido, bruto, " \
                               f"dimensoes, simbolos, tipo_embalagem, cintada, stretch, foto, finalizado) " \
                               f"VALUES ('{context.get('pedido', '')}', '{context.get('cliente', '')}', '{context.get('cnpj', '')}', '{context.get('exigencias', '')}', " \
                               f"'{context.get('correto', '')}', '{context.get('h_inicial', '')}', '{context.get('h_final', '')}', " \
                               f"'{context.get('data', '')}', '{context.get('empatacao', '')}', '{context.get('encaixe', '')}', " \
                               f"'{context.get('encaixe_obs', '')}', '{context.get('solda', '')}', '{context.get('solda_obs', '')}', " \
                               f"'{context.get('cordoalha', '')}', '{context.get('cordoalha_obs', '')}', '{context.get('tipado', '')}', " \
                               f"'{context.get('tipado_obs', '')}', '{context.get('tag', '')}', '{context.get('tag_obs', '')}', " \
                               f"'{context.get('tag_num', '')}', '{context.get('cola', '')}', '{context.get('cola_obs', '')}', " \
                               f"'{context.get('pead', '')}', '{context.get('pead_obs', '')}', '{context.get('corda', '')}', " \
                               f"'{context.get('corda_obs', '')}', '{context.get('corda_cor', '')}', '{context.get('silicone', '')}', " \
                               f"'{context.get('silicone_obs', '')}', '{context.get('cupilha', '')}', '{context.get('cupilha_obs', '')}', " \
                               f"'{context.get('drenado', '')}', '{context.get('drenado_obs', '')}', '{context.get('plaqueta', '')}', " \
                               f"'{context.get('plaqueta_obs', '')}', '{context.get('plaqueta_info', '')}', '{context.get('plaqueta_info_obs', '')}', " \
                               f"'{context.get('diametro', '')}', '{context.get('diametro_obs', '')}', " \
                               f"'{context.get('etiquetas', '')}', '{context.get('etiquetas_obs', '')}', " \
                               f"'{context.get('modelo', '')}', '{context.get('modelo_obs', '')}', " \
                               f"'{context.get('retrabalho', '')}', '{context.get('retrabalho_obs', '')}', " \
                               f"'{context.get('data_armazenamento', '')}', '{context.get('embalagem', '')}', '{context.get('embalagem_obs', '')}', " \
                               f"'{context.get('prego', '')}', '{context.get('prego_obs', '')}', " \
                               f"'{context.get('falha', '')}', '{context.get('falha_obs', '')}', " \
                               f"'{context.get('responsavel', '')}', '{context.get('responsavel_obs', '')}', " \
                               f"'{context.get('qualidade_obs', '')}', '{context.get('inspetor', '')}', " \
                               f"'{context.get('data_inspecao', '')}', '{context.get('lote', '')}', '{context.get('usuario_logado', '')}', " \
                               f"'{context.get('remetente', '')}', '{context.get('n_pedido', '')}', " \
                               f"'{context.get('n_embalagem', '')}', '{context.get('pais_origem', '')}', " \
                               f"'{context.get('pais_destino', '')}', '{context.get('liquido', '')}', " \
                               f"'{context.get('bruto', '')}', '{context.get('dimensoes', '')}', " \
                               f"'{context.get('simbolos', '')}', '{context.get('tipo_embalagem', '')}', " \
                               f"'{context.get('cintada', '')}', '{context.get('stretch', '')}', " \
                               f"'{context.get('foto', '')}', '0') "
                    print(f'consulta: {consulta}')
                    self.cursor.execute(consulta)
                    print(f'fase 3')
                    conexao.commit()
                    print(f'fase 4')
                    mensagem = '1'
                    print(f'fase 5')
                    return mensagem
                except:
                    mensagem = '2'
                    return mensagem
        except:
            mensagem = '3'
            return mensagem

    def finaliza_lote(self, conexao, context):
        try:
            self.cursor = conexao.cursor()
            consulta = f"UPDATE inspecao_final SET finalizado='1' WHERE lote='{context['lote']}' "
            self.cursor.execute(consulta)
            conexao.commit()
            mensagem = '1'
            return mensagem
        except:
            mensagem = '3'
            return mensagem

    def insere_nome_foto(self, conexao, context, filename, numeracao):
        try:
            self.cursor = conexao.cursor()
            consulta = ""
            if numeracao == 1:
                consulta = f"UPDATE inspecao_final SET foto1='{filename}' WHERE lote='{context['lote']}' "
            if numeracao == 2:
                consulta = f"UPDATE inspecao_final SET foto2='{filename}' WHERE lote='{context['lote']}' "
            if numeracao == 3:
                consulta = f"UPDATE inspecao_final SET foto3='{filename}' WHERE lote='{context['lote']}' "
            self.cursor.execute(consulta)
            conexao.commit()
            mensagem = '1'
            return mensagem
        except:
            mensagem = '3'
            return mensagem

    def pega_nome_foto(self, conexao, lote):
        self.cursor = conexao.cursor()
        consulta = f"SELECT foto1, foto2, foto3 FROM inspecao_final WHERE lote = '{lote}'"
        self.cursor.execute(consulta)
        conexao.commit()
        resultado = self.cursor.fetchall()
        return resultado

    def apaga_nome_foto1(self, conexao, lote):
        self.cursor = conexao.cursor()
        consulta = f"UPDATE inspecao_final SET foto1='' WHERE lote='{lote}' "
        self.cursor.execute(consulta)
        conexao.commit()
        mensagem = '1'
        return mensagem

    def apaga_nome_foto2(self, conexao, lote):
        self.cursor = conexao.cursor()
        consulta = f"UPDATE inspecao_final SET foto2='' WHERE lote='{lote}' "
        self.cursor.execute(consulta)
        conexao.commit()
        mensagem = '1'
        return mensagem

    def apaga_nome_foto3(self, conexao, lote):
        self.cursor = conexao.cursor()
        consulta = f"UPDATE inspecao_final SET foto3='' WHERE lote='{lote}' "
        self.cursor.execute(consulta)
        conexao.commit()
        mensagem = '1'
        return mensagem

    def procura_pedido(self, conexao, pedido):
        try:
            self.cursor = conexao.cursor()
            consulta = f"SELECT cnpj, cliente, obs_cliente FROM pedidos WHERE pedido = '{pedido}'"
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
