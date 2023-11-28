class FuncoesExtras:
    @staticmethod
    def verifica_se_orcamento_completo(context):
        try:
            teste = context['ckl_01']
        except:
            context['ckl_01'] = '0'
        try:
            teste = context['ckl_02']
        except:
            context['ckl_02'] = '0'
        try:
            teste = context['ckl_03']
        except:
            context['ckl_03'] = '0'
        try:
            teste = context['ckl_04']
        except:
            context['ckl_04'] = '0'
        try:
            teste = context['ckl_05']
        except:
            context['ckl_05'] = '0'
        try:
            teste = context['ckl_06']
        except:
            context['ckl_06'] = '0'
        try:
            teste = context['ckl_07']
        except:
            context['ckl_07'] = '0'
        try:
            teste = context['ckl_08']
        except:
            context['ckl_08'] = '0'
        try:
            teste = context['ckl_09']
        except:
            context['ckl_09'] = '0'
        try:
            teste = context['ckl_10']
        except:
            context['ckl_10'] = '0'
        try:
            teste = context['ckl_11']
        except:
            context['ckl_11'] = '0'
        try:
            teste = context['ckl_12']
        except:
            context['ckl_12'] = '0'
        try:
            teste = context['ckl_13']
        except:
            context['ckl_13'] = '0'
        try:
            teste = context['ckl_14']
        except:
            context['ckl_14'] = '0'
        try:
            teste = context['ckl_15']
        except:
            context['ckl_15'] = '0'
        try:
            teste = context['ckl_16']
        except:
            context['ckl_16'] = '0'
        status = True
        if context['quando'] == "":
            status = False
            mensagem = "Preencher a Data"
            return status, mensagem
        if context['ckl_01'] == "0":
            status = False
            mensagem = "Preencher o Checklist 01"
            return status, mensagem
        if context['ckl_02'] == "0":
            status = False
            mensagem = "Preencher o Checklist 02"
            return status, mensagem
        if context['ckl_03'] == "0":
            status = False
            mensagem = "Preencher o Checklist 03"
            return status, mensagem
        if context['ckl_04'] == "0":
            status = False
            mensagem = "Preencher o Checklist 04"
            return status, mensagem
        if context['ckl_05'] == "0":
            status = False
            mensagem = "Preencher o Checklist 05"
            return status, mensagem
        if context['ckl_06'] == "0":
            status = False
            mensagem = "Preencher o Checklist 06"
            return status, mensagem
        if context['ckl_07'] == "0":
            status = False
            mensagem = "Preencher o Checklist 07"
            return status, mensagem
        if context['ckl_08'] == "0":
            status = False
            mensagem = "Preencher o Checklist 08"
            return status, mensagem
        if context['ckl_09'] == "0":
            status = False
            mensagem = "Preencher o Checklist 09"
            return status, mensagem
        if context['ckl_10'] == "0":
            status = False
            mensagem = "Preencher o Checklist 10"
            return status, mensagem
        if context['ckl_11'] == "0":
            status = False
            mensagem = "Preencher o Checklist 11"
            return status, mensagem
        if context['ckl_12'] == "0":
            status = False
            mensagem = "Preencher o Checklist 12"
            return status, mensagem
        if context['ckl_13'] == "0":
            status = False
            mensagem = "Preencher o Checklist 13"
            return status, mensagem
        if context['ckl_14'] == "0":
            status = False
            mensagem = "Preencher o Checklist 14"
            return status, mensagem
        if context['ckl_15'] == "0":
            status = False
            mensagem = "Preencher o Checklist 15"
            return status, mensagem
        if context['ckl_16'] == "0":
            status = False
            mensagem = "Preencher o Checklist 16"
            return status, mensagem
        if status == True:
            mensagem = "Lote Salvo!"
        return status, mensagem