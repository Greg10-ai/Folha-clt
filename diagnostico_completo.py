#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script avançado para testar e diagnosticar problemas de email no App.py
"""

import sys
import os

# Importa as configurações do App.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from App import EMAIL_SENDER, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT, obter_info_ip, enviar_email_alerta
    print("✓ Configurações carregadas do App.py com sucesso\n")
except Exception as e:
    print(f"✗ Erro ao carregar App.py: {e}\n")
    sys.exit(1)

import smtplib

def verificar_configuracoes():
    """Verifica se as configurações estão válidas."""
    print("="*70)
    print("🔍 VERIFICANDO CONFIGURAÇÕES")
    print("="*70 + "\n")
    
    print("📧 EMAIL_SENDER:")
    if EMAIL_SENDER and "@gmail.com" in EMAIL_SENDER:
        print(f"   ✓ {EMAIL_SENDER}")
    else:
        print(f"   ✗ INVÁLIDO: {EMAIL_SENDER}")
        return False
    
    print("\n🔑 EMAIL_PASSWORD:")
    if EMAIL_PASSWORD and len(EMAIL_PASSWORD) >= 15:
        print(f"   ✓ {EMAIL_PASSWORD[:4]}***{EMAIL_PASSWORD[-4:]} ({len(EMAIL_PASSWORD)} caracteres)")
    else:
        print(f"   ✗ INVÁLIDO: Muito curto ou vazio ({len(EMAIL_PASSWORD) if EMAIL_PASSWORD else 0} caracteres)")
        return False
    
    print("\n🔌 SMTP_SERVER:")
    print(f"   ✓ {SMTP_SERVER}:{SMTP_PORT}")
    
    return True

def testar_conexao():
    """Testa a conexão com o servidor SMTP."""
    print("\n" + "="*70)
    print("🧪 TESTANDO CONEXÃO COM GMAIL")
    print("="*70 + "\n")
    
    try:
        print("⏳ Conectando a smtp.gmail.com:587...")
        servidor = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10)
        print("✓ Conexão estabelecida")
        
        print("⏳ Iniciando TLS...")
        servidor.starttls()
        print("✓ TLS ativado")
        
        print("⏳ Autenticando...")
        servidor.login(EMAIL_SENDER, EMAIL_PASSWORD)
        print("✓ Autenticação bem-sucedida")
        
        servidor.quit()
        print("\n✓ TODAS AS VERIFICAÇÕES PASSARAM!")
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"\n✗ ERRO DE AUTENTICAÇÃO: {e}")
        print("\nSOLUÇÕES:")
        print("1. Verifique EMAIL_SENDER no App.py (deve ser @gmail.com)")
        print("2. Verifique EMAIL_PASSWORD (deve ter 16 caracteres com espaços)")
        print("3. Gere uma nova Senha de App em: https://myaccount.google.com/apppasswords")
        print("4. Ative Verificação em 2 Etapas no Gmail")
        return False
        
    except smtplib.SMTPException as e:
        print(f"\n✗ ERRO SMTP: {e}")
        print("\nSOLUÇÕES:")
        print("1. Verifique sua conexão com a internet")
        print("2. Seu firewall/antivírus pode estar bloqueando porta 587")
        print("3. Desative VPN/Proxy temporariamente")
        return False
        
    except Exception as e:
        print(f"\n✗ ERRO DESCONHECIDO: {e}")
        return False

def testar_geolocalizacao():
    """Testa a função de geolocalização."""
    print("\n" + "="*70)
    print("🌍 TESTANDO GEOLOCALIZAÇÃO DE IP")
    print("="*70 + "\n")
    
    print("⏳ Obtendo localização do IP 8.8.8.8 (Google DNS)...")
    info = obter_info_ip("8.8.8.8")
    
    print(f"✓ IP: {info['ip']}")
    print(f"✓ País: {info['pais']}")
    print(f"✓ Estado: {info['estado']}")
    print(f"✓ Cidade: {info['cidade']}")
    print(f"✓ ISP: {info['isp']}")
    
    if info['pais'] != "Não disponível":
        print("\n✓ Geolocalização funcionando!")
        return True
    else:
        print("\n⚠️  Geolocalização indisponível")
        return False

def simular_alerta():
    """Simula um envio de alerta."""
    print("\n" + "="*70)
    print("📧 SIMULANDO ENVIO DE ALERTA DE SEGURANÇA")
    print("="*70 + "\n")
    
    ip_teste = "203.0.113.42"
    info_ip_teste = {
        "ip": ip_teste,
        "ip_publico": ip_teste,
        "pais": "Brazil",
        "estado": "São Paulo",
        "cidade": "São Paulo",
        "isp": "Vivo Telecom"
    }
    
    print(f"Simulando bloqueio do IP: {ip_teste}")
    print(f"Destinatário: {EMAIL_SENDER}")
    print()
    
    sucesso = enviar_email_alerta(ip_teste, info_ip_teste, EMAIL_SENDER)
    
    if sucesso:
        print("\n✓ Email simulado enviado com sucesso!")
        print(f"Verifique sua caixa de entrada em {EMAIL_SENDER}")
        return True
    else:
        print("\n✗ Falha ao enviar email simulado")
        return False

def main():
    print("\n")
    print("████████████████████████████████████████████████████████████████████████")
    print("█                                                                      █")
    print("█     🔒 DIAGNÓSTICO COMPLETO - SISTEMA DE SEGURANÇA FOLHA PAG.      █")
    print("█                                                                      █")
    print("████████████████████████████████████████████████████████████████████████")
    print("\n")
    
    # Etapa 1: Verificar configurações
    if not verificar_configuracoes():
        print("\n❌ FALHA: Configurações inválidas. Verifique App.py")
        return False
    
    # Etapa 2: Testar conexão
    if not testar_conexao():
        print("\n❌ FALHA: Não conseguiu conectar ao Gmail")
        return False
    
    # Etapa 3: Testar geolocalização
    testar_geolocalizacao()
    
    # Etapa 4: Simular alerta
    simular_alerta()
    
    print("\n" + "="*70)
    print("✓ DIAGNÓSTICO COMPLETO CONCLUÍDO")
    print("="*70)
    print("\nProximas etapas:")
    print("1. Execute: python App.py")
    print("2. Acesse: http://localhost:5050")
    print("3. Tente fazer login com senha errada")
    print("4. Verifique o email em " + EMAIL_SENDER)
    print("\n")

if __name__ == "__main__":
    main()
