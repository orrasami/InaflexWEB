from .bd_pedidos import BDPedidos


class FuncoesExtras:

    @staticmethod
    def verifica_se_lote_completo(context):
        status = True

        lote_num = context['lote']
        conexao = BDPedidos().conectar()
        nome_foto = BDPedidos().pega_nome_foto(conexao, lote_num)
        BDPedidos().fecha(conexao)

        if nome_foto:
            if nome_foto[0]['foto1']:
                context['foto1'] = nome_foto[0]['foto1']
            else:
                context['foto1'] = ''
            if nome_foto[0]['foto2']:
                context['foto2'] = nome_foto[0]['foto2']
            else:
                context['foto2'] = ''
            if nome_foto[0]['foto3']:
                context['foto3'] = nome_foto[0]['foto3']
            else:
                context['foto3'] = ''

        if context['pedido'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher Pedido"
        if context['cliente'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher Cliente"
        if context['cnpj'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher CNPJ"
        if context['exigencias'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher exigencias"
        if context['lote'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher Lote"
        if context['h_inicial'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher Hora Inicial"
        if context['h_final'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher Hora Final"
        if context['data'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher data"
        if 'empatacao' not in context or context['empatacao'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher empatacao"
        if 'remetente' not in context or context['remetente'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher remetente em identificação da caixa"
        if 'n_pedido' not in context or context['n_pedido'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher o numero de pedido em identificação da caixa"
        if 'n_embalagem' not in context or context['n_embalagem'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher o numero da embalagem em identificação da caixa"
        if 'pais_origem' not in context or context['pais_origem'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher o pais de origem em identificação da caixa"
        if 'pais_destino' not in context or context['pais_destino'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher o pais de destino em identificação da caixa"
        if 'liquido' not in context or context['liquido'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher o peso liquido em identificação da caixa"
        if 'bruto' not in context or context['bruto'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher o peso bruto em identificação da caixa"
        if 'dimensoes' not in context or context['dimensoes'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher as dimensões em identificação da caixa"
        if 'simbolos' not in context or context['simbolos'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher se contem símbolo pictóricos em identificação da caixa"
        if 'tipo_embalagem' not in context or context['tipo_embalagem'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher o tipo de embalagem"
        if 'cintada' not in context or context['cintada'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher se a caixa está cíntada"
        if 'stretch' not in context or context['stretch'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher se o pallet foi embalado com filme stretch"
        if 'foto' not in context or context['foto'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher se tem fotos ou não"
        if 'foto' not in context or context['foto'] == "2":
            if 'foto1' not in context or context['foto1'] == "":
                status = False
                mensagem = "Salvo! Mas falta colocar ao menos uma foto"
            # if 'foto2' not in context or context['foto2'] == "":
            #     status = False
            #     mensagem = "Salvo! Mas falta colocar a foto 2"
            # if 'foto3' not in context or context['foto3'] == "":
            #     status = False
            #     mensagem = "Salvo! Mas falta colocar a foto 3"
        if 'encaixe' not in context or context['encaixe'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher encaixe"
        if 'encaixe' not in context or context['encaixe'] == "4":
            if context['encaixe_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. encaixe"
        if 'solda' not in context or context['solda'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher solda"
        if 'solda' not in context or context['solda'] == "4":
            if context['solda_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. solda"
        if 'cordoalha' not in context or context['cordoalha'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher cordoalha"
        if 'cordoalha' not in context or context['cordoalha'] == "4":
            if context['cordoalha_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. cordoalha"
        if 'tipado' not in context or context['tipado'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher tipado"
        if 'tipado' not in context or context['tipado'] == "4":
            if context['tipado_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs tipado"
        if 'tag' not in context or context['tag'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher TAG"
        if 'tag' not in context or context['tag'] == "4":
            if context['tag_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. TAG"
        if context['tag_num'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher numero da TAG"
        if 'cola' not in context or context['cola'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher cola"
        if 'cola' not in context or context['cola'] == "4":
            if context['cola_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. Cola"
        if 'pead' not in context or context['pead'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher PEAD"
        if 'pead' not in context or context['pead'] == "4":
            if context['pead_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. PEAD"
        if 'corda' not in context or context['corda'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher corda"
        if 'corda' not in context or context['corda'] == "4":
            if context['corda_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. corda"
        if context['corda_cor'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher cor da corda"
        if 'silicone' not in context or context['silicone'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher silicone"
        if 'silicone' not in context or context['silicone'] == "4":
            if context['silicone_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. silicone"
        if 'cupilha' not in context or context['cupilha'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher cupilha"
        if 'cupilha' not in context or context['cupilha'] == "4":
            if context['cupilha_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. cupilha"
        if 'drenado' not in context or context['drenado'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher drenado"
        if 'drenado' not in context or context['drenado'] == "4":
            if context['drenado_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. drenado"
        if 'plaqueta' not in context or context['plaqueta'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher plaquetas"
        if 'plaqueta' not in context or context['plaqueta'] == "4":
            if context['plaqueta_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. plaquetas"
        if 'plaqueta_info' not in context or context['plaqueta_info'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher info plaquetas"
        if 'plaqueta_info' not in context or context['plaqueta_info'] == "4":
            if context['plaqueta_info_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. info plaquetas"
        if 'diametro' not in context or context['diametro'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher diamentro"
        if 'diametro' not in context or context['diametro'] == "4":
            if context['diametro_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. diamentro"
        if 'etiquetas' not in context or context['etiquetas'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher etiquetas"
        if 'etiquetas' not in context or context['etiquetas'] == "4":
            if context['etiquetas_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. Etiquetas"
        if 'modelo' not in context or context['modelo'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher modelo"
        if 'modelo' not in context or context['modelo'] == "4":
            if context['modelo_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. modelo"
        if 'retrabalho' not in context or context['retrabalho'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher retrabalho"
        if 'retrabalho' not in context or context['retrabalho'] == "4":
            if context['retrabalho_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. retrabalho"
        if context['data_armazenamento'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher data de armazenamento"
        if 'embalagem' not in context or context['embalagem'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher embalagem"
        if 'embalagem' not in context or context['embalagem'] == "4":
            if context['embalagem_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. embalagem"
        if 'pregos' not in context or context['pregos'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher pregoso"
        if 'pregos' not in context or context['pregos'] == "4":
            if context['pregos_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. de pregos"
        if 'falha' not in context or context['falha'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher falha"
        if 'falha' not in context or context['falha'] == "2":
            if context['falha_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. de falha"
        if 'responsavel' not in context or context['responsavel'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher Responsavel"
        if 'responsavel' not in context or context['responsavel'] == "2":
            if context['responsavel_obs'] == "":
                status = False
                mensagem = "Salvo! Mas falta preencher Obs. do Responsavel"
        if context['qualidade_obs'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher Obs. da Qualidade"
        if context['inspetor'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher Inspetor"
        if context['data_inspecao'] == "":
            status = False
            mensagem = "Salvo! Mas falta preencher Data da Inspecao"
        if status == True:
            mensagem = "Salvo! Pronto para finalizar"

        return status, mensagem