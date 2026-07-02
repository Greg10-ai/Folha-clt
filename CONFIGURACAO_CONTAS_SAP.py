#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CONFIGURAÇÃO DE CONTAS SAP — RUBRICAS FALTANTES
═════════════════════════════════════════════════════════════════════════════

Este arquivo contém um template com TODAS as rubricas que podem estar faltando
no seu lançamento SAP. Preencha APENAS uma vez com as contas corretas do seu
Chart of Accounts e o script usará automaticamente em todos os lançamentos.

✓ Para usar:
  1. Abra este arquivo e procure pela rubrica que falta
  2. Coloque a conta correta à direita
  3. Copie a linha e cole em CONTAS_CONFIGURÁVEIS do app.py
  4. Descomente removendo o '#'
  5. Pronto! O script usará em todos os lançamentos

═════════════════════════════════════════════════════════════════════════════
PROVENTOS / RESCISÃO
═════════════════════════════════════════════════════════════════════════════
"""

# EXEMPLO DO PDF DO JAMES (demitido):
EXEMPLO_JAMES = """
Rubrica 28 - FERIAS VENCIDAS: 1.196,68
Rubrica 29 - FERIAS PROPORCIONAIS: 186,98
Rubrica 64 - 1/3 FERIAS RESCISAO: 569,53
Rubrica 811 - FERIAS INDENIZADAS: 186,98
Rubrica 816 - FÉRIAS PROP.MÉDIA VALOR: 79,98
Rubrica 819 - FERIAS VENC.MEDIA VALOR: 511,90
Rubrica 8126 - 1/3 FERIAS INDENIZADAS: 88,99
Rubrica 8156 - FERIAS IND.MEDIA VALOR: 79,98
Rubrica 8169 - 1/3 FERIAS PROPORCIONAIS: 88,99
Rubrica 8550 - 13º SALARIO: 747,93
Rubrica 8552 - 13º SAL.MEDIA VALOR: 265,56
Rubrica 9179 - SALDO DE SALARIO HORAS: 299,17
Rubrica 9591 - AVISO PREVIO: 2.468,16
Rubrica 9592 - 13º SALÁRIO INDENIZADO: 186,98
Rubrica 9596 - AVISO PREVIO MEDIA VALOR: 1.055,79
Rubrica 9600 - 13º SAL.INDEN.MEDIA VALOR: 66,39
"""

# ═════════════════════════════════════════════════════════════════════════════
# TEMPLATE DE CONTAS PARA PREENCHER
# ═════════════════════════════════════════════════════════════════════════════

CONTAS_A_PREENCHER = {
    # ─────────────────────────────────────────────────────────────────────────
    # PROVENTOS NORMAIS
    # ─────────────────────────────────────────────────────────────────────────
    'horas_normais':                       '4.01.01.01.02',  # ✓ Já tem
    'horas_ferias':                        '4.01.01.01.09',  # ✓ Já tem
    'horas_extras_50':                     '4.01.01.01.10',  # ✓ Já tem
    
    # ─────────────────────────────────────────────────────────────────────────
    # FÉRIAS (a preencher)
    # ─────────────────────────────────────────────────────────────────────────
    'ferias_vencidas':                     '???',  # Rubrica 28
    'ferias_proporcionais':                '???',  # Rubrica 29
    'ferias_media_horas':                  '???',  # Rubrica 806
    'ferias_media_valor':                  '???',  # Rubrica 816
    'ferias_vencidas_media_valor':         '???',  # Rubrica 819
    'ferias_indenizadas':                  '???',  # Rubrica 811
    'ferias_indenizadas_media_valor':      '???',  # Rubrica 8156
    
    # ─────────────────────────────────────────────────────────────────────────
    # 1/3 DE FÉRIAS (a preencher)
    # ─────────────────────────────────────────────────────────────────────────
    'terco_ferias_prop':                   '???',  # Rubrica 8169
    'terco_ferias_indenizadas':            '???',  # Rubrica 8126
    'dif_terco_ferias':                    '???',  # Rubrica 64
    
    # ─────────────────────────────────────────────────────────────────────────
    # 13º SALÁRIO (a preencher)
    # ─────────────────────────────────────────────────────────────────────────
    'decimo_terceiro':                     '???',  # Rubrica 8550
    'decimo_terceiro_media_valor':         '???',  # Rubrica 8552
    'decimo_terceiro_indenizado':          '???',  # Rubrica 9592
    'decimo_terceiro_indenizado_media_valor': '???',  # Rubrica 9600
    
    # ─────────────────────────────────────────────────────────────────────────
    # AVISO PRÉVIO (a preencher)
    # ─────────────────────────────────────────────────────────────────────────
    'aviso_previo':                        '???',  # Rubrica 9591
    'aviso_previo_media_valor':            '???',  # Rubrica 9596
    
    # ─────────────────────────────────────────────────────────────────────────
    # SALDO DE SALÁRIO (a preencher)
    # ─────────────────────────────────────────────────────────────────────────
    'saldo_salario_horas':                 '???',  # Rubrica 9179
    
    # ─────────────────────────────────────────────────────────────────────────
    # DESCONTOS / RESCISÃO (a preencher)
    # ─────────────────────────────────────────────────────────────────────────
    'liquido_rescisao':                    '???',  # Rubrica 51
    'desc_va_nao_utilizado':               '???',  # Rubrica 274
    'desc_inss_sobre_rescisao':            '???',  # Rubrica 826
    'desc_inss_13sal_rescisao':            '???',  # Rubrica 989
}

# ═════════════════════════════════════════════════════════════════════════════
# INSTRUÇÕES DE USO
# ═════════════════════════════════════════════════════════════════════════════

INSTRUCOES = """
╔════════════════════════════════════════════════════════════════════════════╗
║                    COMO USAR ESTE ARQUIVO                                 ║
╚════════════════════════════════════════════════════════════════════════════╝

PASSO 1: Identifique as contas faltantes
───────────────────────────────────────
• Gere um lançamento de teste no SAP com o script atual
• Veja quais rubricas estão faltando
• Anote os números das contas corretas no seu Chart of Accounts

PASSO 2: Preencha as contas aqui
────────────────────────────────
• Substitua '???' pela conta correta
• Exemplo: 'ferias_vencidas': '4.01.01.01.XX'

PASSO 3: Copie para app.py
──────────────────────────
• Abra app.py
• Procure por: CONTAS_CONFIGURÁVEIS = {
• Copie as linhas preenchidas deste arquivo
• Descomente removendo o '#'

PASSO 4: Teste
──────────────
• Execute o script novamente
• Gere um novo lançamento
• Verifique se as rubricas agora aparecem

═════════════════════════════════════════════════════════════════════════════
EXEMPLO PRONTO PARA COPIAR (para o James):
═════════════════════════════════════════════════════════════════════════════

Se você sabe as contas do seu SAP, descomente estas linhas no app.py:

CONTAS_CONFIGURÁVEIS = {
    'ferias_vencidas': '4.01.01.01.XX',
    'ferias_proporcionais': '4.01.01.01.XX',
    'ferias_media_horas': '4.01.01.01.XX',
    'ferias_media_valor': '4.01.01.01.XX',
    'ferias_vencidas_media_valor': '4.01.01.01.XX',
    'ferias_indenizadas': '4.01.01.01.XX',
    'ferias_indenizadas_media_valor': '4.01.01.01.XX',
    'terco_ferias_prop': '4.01.01.01.XX',
    'terco_ferias_indenizadas': '4.01.01.01.XX',
    'dif_terco_ferias': '4.01.01.01.XX',
    'decimo_terceiro': '4.01.01.01.XX',
    'decimo_terceiro_media_valor': '4.01.01.01.XX',
    'decimo_terceiro_indenizado': '4.01.01.01.XX',
    'decimo_terceiro_indenizado_media_valor': '4.01.01.01.XX',
    'aviso_previo': '4.01.01.01.XX',
    'aviso_previo_media_valor': '4.01.01.01.XX',
    'saldo_salario_horas': '4.01.01.01.XX',
    'liquido_rescisao': '4.01.01.01.XX',
    'desc_va_nao_utilizado': '3.01.02.02.XX',
    'desc_inss_sobre_rescisao': '2.01.01.07.XX',
    'desc_inss_13sal_rescisao': '2.01.01.07.XX',
}

═════════════════════════════════════════════════════════════════════════════
"""

if __name__ == '__main__':
    print(INSTRUCOES)
    print("\nEXEMPLO DO PDF JAMES:")
    print(EXEMPLO_JAMES)
    print("\nCONTAS A PREENCHER:")
    for chave, valor in CONTAS_A_PREENCHER.items():
        status = "✓" if valor != '???' else "✗"
        print(f"  {status} {chave:40s} → {valor}")
