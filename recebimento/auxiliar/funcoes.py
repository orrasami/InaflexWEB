class FuncoesExtras:
    @staticmethod
    def verifica_se_lote_completo(context):
        try:
            teste = context['med_laudo_1']
        except:
            context['med_laudo_1'] = '0'
        try:
            teste = context['med_laudo_2']
        except:
            context['med_laudo_2'] = '0'
        try:
            teste = context['med_laudo_3']
        except:
            context['med_laudo_3'] = '0'
        try:
            teste = context['med_laudo_4']
        except:
            context['med_laudo_4'] = '0'
        try:
            teste = context['med_laudo_5']
        except:
            context['med_laudo_5'] = '0'
        try:
            teste = context['med_laudo_6']
        except:
            context['med_laudo_6'] = '0'
        try:
            teste = context['med_laudo_7']
        except:
            context['med_laudo_7'] = '0'
        try:
            teste = context['med_laudo_8']
        except:
            context['med_laudo_8'] = '0'
        try:
            teste = context['med_laudo_9']
        except:
            context['med_laudo_9'] = '0'
        try:
            teste = context['med_laudo_10']
        except:
            context['med_laudo_10'] = '0'
        try:
            teste = context['med_laudo_11']
        except:
            context['med_laudo_11'] = '0'
        try:
            teste = context['med_laudo_12']
        except:
            context['med_laudo_12'] = '0'
        try:
            teste = context['med_laudo_13']
        except:
            context['med_laudo_13'] = '0'
        try:
            teste = context['med_laudo_14']
        except:
            context['med_laudo_14'] = '0'
        try:
            teste = context['med_laudo_15']
        except:
            context['med_laudo_15'] = '0'
        status = True
        if context['fornecedor'] == "":
            status = False
            mensagem = "Preencher fornecedor"
            return status, mensagem
        if context['plcq'] == "":
            status = False
            mensagem = "Preencher PL-CQ"
            return status, mensagem
        if context['quando'] == "":
            status = False
            mensagem = "Preencher Data"
            return status, mensagem
        if context['nota'] == "":
            status = False
            mensagem = "Preencher Numero da Nota"
            return status, mensagem
        if context['oc'] == "":
            status = False
            mensagem = "Preencher Numero da O.C."
            return status, mensagem
        if context['quantidade'] == "":
            status = False
            mensagem = "Preencher Quantidade"
            return status, mensagem
        if context['inspecionado'] == "":
            status = False
            mensagem = "Preencher quantidade Inspecionada"
            return status, mensagem
        if context['defeito'] == "":
            status = False
            mensagem = "Preencher Quantidade com Defeito"
            return status, mensagem
        if context['material'] == "":
            status = False
            mensagem = "Preencher Descrição do Material"
            return status, mensagem
        if context['med_forma_1'] == "":
            status = False
            mensagem = "O documento deve conter pelo menos uma medida (1)"
            return status, mensagem
        else:
            if context['med_valor_1'] == "":
                status = False
                mensagem = "Valor deve ser diferente de Zero (Medida 01)"
                return status, mensagem
            if 'med_laudo_1' not in context or context['med_laudo_1'] == "":
                status = False
                mensagem = "Falta laudo da Medida 01"
                return status, mensagem
            if context['med_forma_2'] == "" and (context['med_forma_3'] != "" or context['med_forma_4'] != "" or context['med_forma_5'] != "" or context['med_forma_6'] != "" or context['med_forma_7'] != "" or context['med_forma_8'] != "" or context['med_forma_9'] != "" or context['med_forma_10'] != "" or context['med_forma_11'] != "" or context['med_forma_12'] != "" or context['med_forma_13'] != "" or context['med_forma_14'] != "" or context['med_forma_15'] != ""):
                status = False
                mensagem = "O documento deve conter pelo menos uma medida (2)"
                return status, mensagem
            else:
                if context['med_forma_2'] != "":
                    if context['med_valor_2'] == "":
                        status = False
                        mensagem = "Valor deve ser diferente de Zero (Medida 02)"
                        return status, mensagem
                    if 'med_laudo_2' not in context or context['med_laudo_2'] == "":
                        status = False
                        mensagem = "Falta laudo da Medida 02"
                        return status, mensagem
                if context['med_forma_3'] == "" and (context['med_forma_4'] != "" or context['med_forma_5'] != "" or context['med_forma_6'] != "" or context['med_forma_7'] != "" or context['med_forma_8'] != "" or context['med_forma_9'] != "" or context['med_forma_10'] != "" or context['med_forma_11'] != "" or context['med_forma_12'] != "" or context['med_forma_13'] != "" or context['med_forma_14'] != "" or context['med_forma_15'] != ""):
                    status = False
                    mensagem = "O documento deve conter pelo menos uma medida (3)"
                    return status, mensagem
                else:
                    if context['med_forma_3'] != "":
                        if context['med_valor_3'] == "":
                            status = False
                            mensagem = "Valor deve ser diferente de Zero (Medida 03)"
                            return status, mensagem
                        if 'med_laudo_3' not in context or context['med_laudo_3'] == "":
                            status = False
                            mensagem = "Falta laudo da Medida 03"
                            return status, mensagem
                    if context['med_forma_4'] == "" and (context['med_forma_5'] != "" or context['med_forma_6'] != "" or context['med_forma_7'] != "" or context['med_forma_8'] != "" or context['med_forma_9'] != "" or context['med_forma_10'] != "" or context['med_forma_11'] != "" or context['med_forma_12'] != "" or context['med_forma_13'] != "" or context['med_forma_14'] != "" or context['med_forma_15'] != ""):
                        status = False
                        mensagem = "O documento deve conter pelo menos uma medida (4)"
                        return status, mensagem
                    else:
                        if context['med_forma_4'] != "":
                            if context['med_valor_4'] == "":
                                status = False
                                mensagem = "Valor deve ser diferente de Zero (Medida 04)"
                                return status, mensagem
                            if 'med_laudo_4' not in context or context['med_laudo_4'] == "":
                                status = False
                                mensagem = "Falta laudo da Medida 04"
                                return status, mensagem
                        if context['med_forma_5'] == "" and (context['med_forma_6'] != "" or context['med_forma_7'] != "" or context['med_forma_8'] != "" or context['med_forma_9'] != "" or context['med_forma_10'] != "" or context['med_forma_11'] != "" or context['med_forma_12'] != "" or context['med_forma_13'] != "" or context['med_forma_14'] != "" or context['med_forma_15'] != ""):
                            status = False
                            mensagem = "O documento deve conter pelo menos uma medida (5)"
                            return status, mensagem
                        else:
                            if context['med_forma_5'] != "":
                                if context['med_valor_5'] == "":
                                    status = False
                                    mensagem = "Valor deve ser diferente de Zero (Medida 05)"
                                    return status, mensagem
                                if 'med_laudo_5' not in context or context['med_laudo_5'] == "":
                                    status = False
                                    mensagem = "Falta laudo da Medida 05"
                                    return status, mensagem
                            if context['med_forma_6'] == "" and (context['med_forma_7'] != "" or context['med_forma_8'] != "" or context['med_forma_9'] != "" or context['med_forma_10'] != "" or context['med_forma_11'] != "" or context['med_forma_12'] != "" or context['med_forma_13'] != "" or context['med_forma_14'] != "" or context['med_forma_15'] != ""):
                                status = False
                                mensagem = "O documento deve conter pelo menos uma medida (6)"
                                return status, mensagem
                            else:
                                if context['med_forma_6'] != "":
                                    if context['med_valor_6'] == "":
                                        status = False
                                        mensagem = "Valor deve ser diferente de Zero (Medida 06)"
                                        return status, mensagem
                                    if 'med_laudo_6' not in context or context['med_laudo_6'] == "":
                                        status = False
                                        mensagem = "Falta laudo da Medida 06"
                                        return status, mensagem
                                if context['med_forma_7'] == "" and (context['med_forma_8'] != "" or context['med_forma_9'] != "" or context['med_forma_10'] != "" or context['med_forma_11'] != "" or context['med_forma_12'] != "" or context['med_forma_13'] != "" or context['med_forma_14'] != "" or context['med_forma_15'] != ""):
                                    status = False
                                    mensagem = "O documento deve conter pelo menos uma medida (7)"
                                    return status, mensagem
                                else:
                                    if context['med_forma_7'] != "":
                                        if context['med_valor_7'] == "":
                                            status = False
                                            mensagem = "Valor deve ser diferente de Zero (Medida 07)"
                                            return status, mensagem
                                        if 'med_laudo_7' not in context or context['med_laudo_7'] == "":
                                            status = False
                                            mensagem = "Falta laudo da Medida 07"
                                            return status, mensagem
                                    if context['med_forma_8'] == "" and (context['med_forma_9'] != "" or context['med_forma_10'] != "" or context['med_forma_11'] != "" or context['med_forma_12'] != "" or context['med_forma_13'] != "" or context['med_forma_14'] != "" or context['med_forma_15'] != ""):
                                        status = False
                                        mensagem = "O documento deve conter pelo menos uma medida (8)"
                                        return status, mensagem
                                    else:
                                        if context['med_forma_8'] != "":
                                            if context['med_valor_8'] == "":
                                                status = False
                                                mensagem = "Valor deve ser diferente de Zero (Medida 08)"
                                                return status, mensagem
                                            if 'med_laudo_8' not in context or context['med_laudo_8'] == "":
                                                status = False
                                                mensagem = "Falta laudo da Medida 08"
                                                return status, mensagem
                                        if context['med_forma_9'] == "" and (context['med_forma_10'] != "" or context['med_forma_11'] != "" or context['med_forma_12'] != "" or context['med_forma_13'] != "" or context['med_forma_14'] != "" or context['med_forma_15'] != ""):
                                            status = False
                                            mensagem = "O documento deve conter pelo menos uma medida (9)"
                                            return status, mensagem
                                        else:
                                            if context['med_forma_9'] != "":
                                                if context['med_valor_9'] == "":
                                                    status = False
                                                    mensagem = "Valor deve ser diferente de Zero (Medida 09)"
                                                    return status, mensagem
                                                if 'med_laudo_9' not in context or context['med_laudo_9'] == "":
                                                    status = False
                                                    mensagem = "Falta laudo da Medida 09"
                                                    return status, mensagem
                                            if context['med_forma_10'] == "" and (context['med_forma_11'] != "" or context['med_forma_12'] != "" or context['med_forma_13'] != "" or context['med_forma_14'] != "" or context['med_forma_15'] != ""):
                                                status = False
                                                mensagem = "O documento deve conter pelo menos uma medida (10)"
                                                return status, mensagem
                                            else:
                                                if context['med_forma_10'] != "":
                                                    if context['med_valor_10'] == "":
                                                        status = False
                                                        mensagem = "Valor deve ser diferente de Zero (Medida 010)"
                                                        return status, mensagem
                                                    if 'med_laudo_10' not in context or context['med_laudo_10'] == "":
                                                        status = False
                                                        mensagem = "Falta laudo da Medida 010"
                                                        return status, mensagem
                                                if context['med_forma_11'] == "" and (context['med_forma_12'] != "" or context['med_forma_13'] != "" or context['med_forma_14'] != "" or context['med_forma_15'] != ""):
                                                    status = False
                                                    mensagem = "O documento deve conter pelo menos uma medida (11)"
                                                    return status, mensagem
                                                else:
                                                    if context['med_forma_11'] != "":
                                                        if context['med_valor_11'] == "":
                                                            status = False
                                                            mensagem = "Valor deve ser diferente de Zero (Medida 011)"
                                                            return status, mensagem
                                                        if 'med_laudo_11' not in context or context['med_laudo_11'] == "":
                                                            status = False
                                                            mensagem = "Falta laudo da Medida 011"
                                                            return status, mensagem
                                                    if context['med_forma_12'] == "" and (context['med_forma_13'] != "" or context['med_forma_14'] != "" or context['med_forma_15'] != ""):
                                                        status = False
                                                        mensagem = "O documento deve conter pelo menos uma medida (12)"
                                                        return status, mensagem
                                                    else:
                                                        if context['med_forma_12'] != "":
                                                            if context['med_valor_12'] == "":
                                                                status = False
                                                                mensagem = "Valor deve ser diferente de Zero (Medida 012)"
                                                                return status, mensagem
                                                            if 'med_laudo_12' not in context or context['med_laudo_12'] == "":
                                                                status = False
                                                                mensagem = "Falta laudo da Medida 012"
                                                                return status, mensagem
                                                        if context['med_forma_13'] == "" and (context['med_forma_14'] != "" or context['med_forma_15'] != ""):
                                                            status = False
                                                            mensagem = "O documento deve conter pelo menos uma medida (13)"
                                                            return status, mensagem
                                                        else:
                                                            if context['med_forma_13'] != "":
                                                                if context['med_valor_13'] == "":
                                                                    status = False
                                                                    mensagem = "Valor deve ser diferente de Zero (Medida 013)"
                                                                    return status, mensagem
                                                                if 'med_laudo_13' not in context or context['med_laudo_13'] == "":
                                                                    status = False
                                                                    mensagem = "Falta laudo da Medida 013"
                                                                    return status, mensagem
                                                            if context['med_forma_14'] == "" and context['med_forma_15'] != "":
                                                                status = False
                                                                mensagem = "O documento deve conter pelo menos uma medida (14)"
                                                                return status, mensagem
                                                            else:
                                                                if context['med_forma_14'] != "":
                                                                    if context['med_valor_14'] == "":
                                                                        status = False
                                                                        mensagem = "Valor deve ser diferente de Zero (Medida 014)"
                                                                        return status, mensagem
                                                                    if 'med_laudo_14' not in context or context['med_laudo_14'] == "":
                                                                        status = False
                                                                        mensagem = "Falta laudo da Medida 014"
                                                                        return status, mensagem
                                                                if context['med_forma_15'] != "":
                                                                    if context['med_valor_15'] == "":
                                                                        status = False
                                                                        mensagem = "Valor deve ser diferente de Zero (Medida 015)"
                                                                        return status, mensagem
                                                                    if 'med_laudo_15' not in context or context['med_laudo_15'] == "":
                                                                        status = False
                                                                        mensagem = "Falta laudo da Medida 015"
                                                                        return status, mensagem
        if 'laudo_final' not in context:
            status = False
            mensagem = "Falta Laudo Final"
            return status, mensagem
        else:
            if context['laudo_final'] == "2" or context['laudo_final'] == "3" or context['laudo_final'] == "4":
                if context['obs_laudo'] == "":
                    status = False
                    mensagem = "Falta preencher Obs. do Laudo Final"
                    return status, mensagem
                if context['laudo_final'] == "2":
                    if context['liberacao_condicional'] == "":
                        status = False
                        mensagem = "Falta preencher quem liberou o Retrabalho"
                        return status, mensagem
                if context['laudo_final'] == "3":
                    if context['liberacao_condicional'] == "":
                        status = False
                        mensagem = "Falta preencher quem fez a liberação condicional"
                        return status, mensagem
                if context['laudo_final'] == "4":
                    if context['liberacao_condicional'] == "":
                        status = False
                        mensagem = "Falta preencher qual ação foi tomada com o lote reprovado"
                        return status, mensagem
        if (context['med_laudo_1'] == '4' or context['med_laudo_2'] == '4' or context['med_laudo_3'] == '4' or 
                context['med_laudo_4'] == '4' or context['med_laudo_5'] == '4' or context['med_laudo_6'] == '4' or 
                context['med_laudo_7'] == '4' or context['med_laudo_8'] == '4' or context['med_laudo_9'] == '4' or 
                context['med_laudo_10'] == '4' or context['med_laudo_11'] == '4' or context['med_laudo_12'] == '4' 
                or context['med_laudo_13'] == '4' or context['med_laudo_14'] == '4' or context['med_laudo_15'] == '4'):
            if context['laudo_final'] != "4":
                status = False
                mensagem = "Pelas respostas, Laudo Final deve ser REJEITADO"
                return status, mensagem
        else:
            if (context['med_laudo_1'] == '3' or context['med_laudo_2'] == '3' or context['med_laudo_3'] == '3' or
                    context['med_laudo_4'] == '3' or context['med_laudo_5'] == '3' or context['med_laudo_6'] == '3' or
                    context['med_laudo_7'] == '3' or context['med_laudo_8'] == '3' or context['med_laudo_9'] == '3' or
                    context['med_laudo_10'] == '3' or context['med_laudo_11'] == '3' or context['med_laudo_12'] == '3'
                    or context['med_laudo_13'] == '3' or context['med_laudo_14'] == '3' or context['med_laudo_15'] == '3'):
                if context['laudo_final'] != "3":
                    status = False
                    mensagem = "Pelas respostas, Laudo Final deve ser CONDICIONAL"
                    return status, mensagem
            else:
                if (context['med_laudo_1'] == '2' or context['med_laudo_2'] == '2' or context['med_laudo_3'] == '2' or
                        context['med_laudo_4'] == '2' or context['med_laudo_5'] == '2' or context['med_laudo_6'] == '2' or
                        context['med_laudo_7'] == '2' or context['med_laudo_8'] == '2' or context['med_laudo_9'] == '2' or
                        context['med_laudo_10'] == '2' or context['med_laudo_11'] == '2' or context['med_laudo_12'] == '2'
                        or context['med_laudo_13'] == '2' or context['med_laudo_14'] == '2' or context['med_laudo_15'] == '2'):
                    if context['laudo_final'] != "2":
                        status = False
                        mensagem = "Pelas respostas, Laudo Final deve ser RETRABALHO"
                        return status, mensagem
                else:
                    if context['laudo_final'] != "1":
                        status = False
                        mensagem = "Pelas respostas, Laudo Final deve ser OK"
                        return status, mensagem
        if status == True:
            mensagem = "Lote Salvo!"
        return status, mensagem