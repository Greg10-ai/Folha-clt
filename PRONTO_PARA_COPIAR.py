# ═════════════════════════════════════════════════════════════════════════════
# COPIE ISTO PARA O app.py NO LUGAR DE CONTAS_CONFIGURÁVEIS
# ═════════════════════════════════════════════════════════════════════════════
# 
# Instruções:
# 1. Veja na imagem do Excel qual é a conta correta para cada rubrica
# 2. Substitua os valores XX pelos números corretos
# 3. Descomente as linhas (remova o #)
# 4. Copie tudo para dentro do CONTAS_CONFIGURÁVEIS do app.py
#
# ═════════════════════════════════════════════════════════════════════════════

CONTAS_CONFIGURÁVEIS = {
    # PROVENTOS - FÉRIAS
    'ferias_vencidas': '4.01.01.01.22',              # Rubrica 28 - FERIAS VENCIDAS
    'ferias_proporcionais': '4.01.01.01.23',         # Rubrica 29 - FERIAS PROPORCIONAIS
    'ferias_media_horas': '4.01.01.01.25',           # Rubrica 806 - FERIAS MEDIA HORAS
    'ferias_media_valor': '4.01.01.01.27',           # Rubrica 816 - FÉRIAS PROP.MÉDIA VALOR
    'ferias_vencidas_media_valor': '4.01.01.01.28',  # Rubrica 819 - FERIAS VENC.MEDIA VALOR
    'ferias_indenizadas': '4.01.01.01.24',           # Rubrica 811 - FERIAS INDENIZADAS
    'ferias_indenizadas_media_valor': '4.01.01.01.29',  # Rubrica 8156 - FERIAS IND.MEDIA VALOR
    
    # PROVENTOS - 1/3 FÉRIAS
    'terco_ferias_prop': '4.01.01.01.33',            # Rubrica 8169 - 1/3 FERIAS PROPORCIONAIS
    'terco_ferias_indenizadas': '4.01.01.01.31',     # Rubrica 8126 - 1/3 FERIAS INDENIZADAS
    'dif_terco_ferias': '4.01.01.01.30',             # Rubrica 64 - 1/3 FERIAS RESCISAO
    
    # PROVENTOS - 13º SALÁRIO
    'decimo_terceiro': '4.01.01.01.19',              # Rubrica 8550 - 13º SALÁRIO
    'decimo_terceiro_media_valor': '4.01.01.01.34',  # Rubrica 8552 - 13º SAL.MEDIA VALOR
    'decimo_terceiro_indenizado': '4.01.01.01.36',   # Rubrica 9592 - 13º SALÁRIO INDENIZADO
    'decimo_terceiro_indenizado_media_valor': '4.01.01.01.37',  # Rubrica 9600 - 13º SAL.INDEN.MEDIA
    
    # PROVENTOS - AVISO PRÉVIO
    'aviso_previo': '4.01.01.01.38',                 # Rubrica 9591 - AVISO PREVIO
    'aviso_previo_media_valor': '4.01.01.01.39',     # Rubrica 9596 - AVISO PREVIO MEDIA VALOR
    
    # PROVENTOS - SALDO DE SALÁRIO
    'saldo_salario_horas': '4.01.01.01.35',          # Rubrica 9179 - SALDO DE SALARIO HORAS
    
    # DESCONTOS/RESCISÃO - CONTAS A VERIFICAR!
    'liquido_rescisao': '4.01.01.01.44',             # Rubrica 51 - LIQUIDO RESCISAO
    'desc_va_nao_utilizado': '3.01.02.02.05',        # Rubrica 274 - DESC.VA NÃO UTILIZADO
    'desc_inss_sobre_rescisao': '2.01.01.07.11',     # Rubrica 826 - DESC.INSS SOBRE RESCISAO
    'desc_inss_13sal_rescisao': '2.01.01.07.XX',     # Rubrica 989 - DESC.INSS 13 SAL.RESCISAO ← VERIFIQUE!
}

# ═════════════════════════════════════════════════════════════════════════════
# PASSO A PASSO:
# ═════════════════════════════════════════════════════════════════════════════
#
# 1. Compare cada 'conta' acima (ex: '4.01.01.01.22') com a imagem do Excel
# 2. Se estiver diferente, corrija
# 3. Em especial, verifique:
#    - Rubrica 989: desc_inss_13sal_rescisao ← PRECISA VERIFICAR!
# 4. Copie TODO o dicionário acima
# 5. Abra app.py e procure por: CONTAS_CONFIGURÁVEIS = {
# 6. Substitua pelo dicionário que copiou
# 7. Salve e teste!
#
# ═════════════════════════════════════════════════════════════════════════════
