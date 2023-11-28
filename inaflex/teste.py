consulta = f"UPDATE inspecao_final SET " \
           f"correto='{context['correto']}', " \
           f"h_inicial='{context['h_inicial']}', " \
           f"h_final='{context['h_final']}', " \
           f"data='{context['data']}', " \
           f"empatacao='{context['empatacao']}', " \
           f"encaixe='{context['encaixe']}', " \
           f"encaixe_obs='{context['encaixe_obs']}', " \
           f"solda='{context['solda']}', " \
           f"solda_obs='{context['solda_obs']}', " \
           f"cordoalha='{context['cordoalha']}', " \
           f"cordoalha_obs='{context['cordoalha_obs']}', " \
           f"tipado='{context['tipado']}', " \
           f"tipado_obs='{context['tipado_obs']}', " \
           f"tag='{context['tag']}', " \
           f"tag_obs='{context['tag_obs']}', " \
           f"tag_num='{context['tag_num']}', " \
           f"cola='{context['cola']}', " \
           f"cola_obs='{context['cola_obs']}', " \
           f"pead='{context['pead']}', " \
           f"pead_obs='{context['pead_obs']}', " \
           f"corda='{context['corda']}', " \
           f"corda_obs='{context['corda_obs']}', " \
           f"corda_cor='{context['corda_cor']}', " \
           f"silicone='{context['silicone']}', " \
           f"silicone_obs='{context['silicone_obs']}', " \
           f"cupilha='{context['cupilha']}', " \
           f"cupilha_obs='{context['cupilha_obs']}', " \
           f"drenado='{context['drenado']}', " \
           f"drenado_obs='{context['drenado_obs']}', " \
           f"plaqueta='{context['plaqueta']}', " \
           f"plaqueta_obs='{context['plaqueta_obs']}', " \
           f"plaqueta_info='{context['plaqueta_info']}', " \
           f"plaqueta_info_obs='{context['plaqueta_info_obs']}', " \
           f"diametro='{context['diametro']}', " \
           f"diametro_obs='{context['diametro_obs']}', " \
           f"etiquetas='{context['etiquetas']}', " \
           f"etiquetas_obs='{context['etiquetas_obs']}', " \
           f"modelo='{context['modelo']}', " \
           f"modelo_obs='{context['modelo_obs']}', " \
           f"retrabalho='{context['retrabalho']}', " \
           f"retrabalho_obs='{context['retrabalho_obs']}', " \
           f"data_armazenamento='{context['data_armazenamento']}', " \
           f"embalagem='{context['embalagem']}', " \
           f"embalagem_obs='{context['embalagem_obs']}', " \
           f"pregos='{context['pregos']}', " \
           f"pregos_obs='{context['pregos_obs']}', " \
           f"falha='{context['falha']}', " \
           f"falha_obs='{context['falha_obs']}', " \
           f"responsavel='{context['responsavel']}', " \
           f"responsavel_obs='{context['responsavel_obs']}', " \
           f"qualidade_obs='{context['qualidade_obs']}', " \
           f"inspetor='{context['inspetor']}', " \
           f"data_inspecao='{context['data_inspecao']}' WHERE lote='{context['lote']}' "

consulta = f"INSERT INTO inspecao_final (correto, h_inicial, h_final, data, empatacao, encaixe, " \
           f"encaixe_obs, solda, solda_obs, cordoalha, cordoalha_obs, tipado, tipado_obs, tag, " \
           f"tag_obs, tag_num, cola, cola_obs, pead, pead_obs, corda, corda_obs, corda_cor, " \
           f"silicone, silicone_obs, cupilha, cupilha_obs, drenado, drenado_obs, plaqueta, " \
           f"plaqueta_obs, plaqueta_info, plaqueta_info_obs, diametro, diametro_obs, etiquetas, " \
           f"etiquetas_obs, modelo, modelo_obs, retrabalho, retrabalho_obs, data_armazenamento, " \
           f"embalagem, embalagem_obs, pregos, pregos_obs, falha, falha_obs, responsavel, " \
           f"responsavel_obs, qualidade_obs, inspetor, data_inspecao, lote) " \
           f"VALUES ('{context['correto']}', '{context['h_inicial']}', '{context['h_final']}', " \
           f"'{context['data']}', '{context['empatacao']}', '{context['encaixe']}', " \
           f"'{context['encaixe_obs']}', '{context['solda']}', '{context['solda_obs']}', " \
           f"'{context['cordoalha']}', '{context['cordoalha_obs']}', '{context['tipado']}', " \
           f"'{context['tipado_obs']}', '{context['tag']}', '{context['tag_obs']}', " \
           f"'{context['tag_num']}', '{context['cola']}', '{context['cola_obs']}', " \
           f"'{context['pead']}', '{context['pead_obs']}', '{context['corda']}', " \
           f"'{context['corda_obs']}', '{context['corda_cor']}', '{context['silicone']}', " \
           f"'{context['silicone_obs']}', '{context['cupilha']}', '{context['cupilha_obs']}', " \
           f"'{context['drenado']}', '{context['drenado_obs']}', '{context['plaqueta']}', " \
           f"'{context['plaqueta_obs']}', '{context['plaqueta_info']}', " \
           f"'{context['plaqueta_info_obs']}', '{context['diametro']}', " \
           f"'{context['diametro_obs']}', '{context['etiquetas']}', '{context['etiquetas_obs']}', " \
           f"'{context['modelo']}', '{context['modelo_obs']}', '{context['retrabalho']}', " \
           f"'{context['retrabalho_obs']}', '{context['data_armazenamento']}', " \
           f"'{context['embalagem']}', '{context['embalagem_obs']}', '{context['pregos']}" \
           f"{context['pregos_obs']}', '{context['falha']}', '{context['falha_obs']}', " \
           f"'{context['responsavel']}', '{context['responsavel_obs']}', " \
           f"'{context['qualidade_obs']}', '{context['inspetor']}', '{context['data_inspecao']}', " \
           f"'{context['lote']}')"
