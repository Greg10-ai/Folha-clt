#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de teste para validar a extração das rubricas do PDF
"""

import sys
import json
from app import parse_pdf

def main():
    # Você pode testar com um PDF existente
    # Altere o caminho conforme necessário
    pdf_path = input("Digite o caminho do arquivo PDF: ").strip()
    
    if not pdf_path:
        print("❌ Nenhum arquivo informado.")
        return
    
    try:
        print(f"\n🔍 Processando: {pdf_path}")
        employees, encargos, enc_rat = parse_pdf(pdf_path)
        
        print(f"\n✅ Total de funcionários: {len(employees)}\n")
        
        for emp in employees:
            print(f"{'='*80}")
            print(f"ID: {emp['id']} | Nome: {emp['nome']} | Situação: {emp['situacao']}")
            print(f"{'='*80}")
            
            # Rubricas de Férias e Rescisão
            rubricas_importantes = [
                'ferias_vencidas', 'ferias_indenizadas', 'ferias_vencidas_media_valor',
                'ferias_indenizadas_media_valor', 'terco_ferias_indenizadas',
                'decimo_terceiro', 'decimo_terceiro_media_valor', 'decimo_terceiro_indenizado',
                'decimo_terceiro_indenizado_media_valor', 'aviso_previo', 'aviso_previo_media_valor',
                'liquido_rescisao', 'desc_vale_adiantamento', 'desc_inss_13sal_rescisao',
                'horas_afastadas_inss', 'comissoes', 'pro_labore'
            ]
            
            print("\n📋 Rubricas Importantes:")
            for rubrica in rubricas_importantes:
                valor = emp.get(rubrica, 0.0)
                if valor > 0:
                    print(f"  ✓ {rubrica:40s}: R$ {valor:>12.2f}")
            
            print(f"\n📊 Resumos:")
            print(f"  Proventos Calculados: R$ {emp.get('proventos_calculados', 0):>12.2f}")
            print(f"  Proventos (PDF):      R$ {emp.get('proventos', 0):>12.2f}")
            print(f"  Base INSS:            R$ {emp.get('base_inss', 0):>12.2f}")
            print(f"  Descontos:            R$ {emp.get('descontos', 0):>12.2f}")
            print(f"  Líquido:              R$ {emp.get('liquido', 0):>12.2f}")
            
    except Exception as e:
        print(f"❌ Erro ao processar PDF: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
