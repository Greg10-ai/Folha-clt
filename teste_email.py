#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de teste para verificar se o email está configurado corretamente
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ════════════════════════════════════════════════════════════════════════════
# CONFIGURE AQUI COM OS SEUS DADOS
# ════════════════════════════════════════════════════════════════════════════

EMAIL_SENDER = "gregorydeabreu89@gmail.com"  # SEU EMAIL DO GMAIL
EMAIL_PASSWORD = "bdif vdvc idfo gwih"       # SUA SENHA DE APP (com espaços!)
EMAIL_DESTINO = "gregorydeabreu89@gmail.com" # ONDE ENVIAR O TESTE

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# ════════════════════════════════════════════════════════════════════════════

def testar_email():
    print("=" * 70)
    print("🧪 TESTE DE ENVIO DE EMAIL")
    print("=" * 70)
    
    print(f"\n📧 Email Remetente: {EMAIL_SENDER}")
    print(f"📧 Email Destinatário: {EMAIL_DESTINO}")
    print(f"🔌 Servidor: {SMTP_SERVER}:{SMTP_PORT}")
    print(f"🔑 Senha: {'*' * len(EMAIL_PASSWORD)} (oculta)")
    
    try:
        print("\n⏳ Conectando ao servidor Gmail...")
        servidor = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        servidor.starttls()
        print("✓ Conexão SSL/TLS estabelecida com sucesso")
        
        print("\n⏳ Autenticando...")
        servidor.login(EMAIL_SENDER, EMAIL_PASSWORD)
        print("✓ Autenticação bem-sucedida!")
        
        print("\n⏳ Preparando mensagem...")
        assunto = "🧪 TESTE - Sistema de Segurança Folha de Pagamento"
        
        corpo_html = """
        <html>
            <head>
                <style>
                    body { font-family: Arial, sans-serif; }
                    .container { max-width: 600px; margin: 0 auto; padding: 20px; }
                    .header { background-color: #22c55e; color: white; padding: 20px; border-radius: 5px; }
                    .content { background-color: #f5f5f5; padding: 20px; margin-top: 20px; border-radius: 5px; }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h2>✓ EMAIL FUNCIONANDO!</h2>
                    </div>
                    <div class="content">
                        <p>Este é um email de teste. Se você recebeu isso, significa que o sistema de envio de emails está funcionando corretamente!</p>
                        <p><strong>Informações do Teste:</strong></p>
                        <ul>
                            <li>Remetente: """ + EMAIL_SENDER + """</li>
                            <li>Data/Hora: """ + str(__import__('datetime').datetime.now().strftime('%d/%m/%Y %H:%M:%S')) + """</li>
                        </ul>
                        <p>Você pode começar a usar o sistema de segurança com confiança!</p>
                    </div>
                </div>
            </body>
        </html>
        """
        
        mensagem = MIMEMultipart("alternative")
        mensagem["Subject"] = assunto
        mensagem["From"] = EMAIL_SENDER
        mensagem["To"] = EMAIL_DESTINO
        
        mensagem.attach(MIMEText(corpo_html, "html"))
        print("✓ Mensagem preparada")
        
        print("\n⏳ Enviando email...")
        servidor.sendmail(EMAIL_SENDER, EMAIL_DESTINO, mensagem.as_string())
        servidor.quit()
        
        print("\n" + "=" * 70)
        print("✓✓✓ EMAIL ENVIADO COM SUCESSO! ✓✓✓")
        print("=" * 70)
        print(f"\nVerifique seu email em: {EMAIL_DESTINO}")
        print("O email deve chegar em poucos segundos.")
        print("\nSe não receber, verifique a pasta de SPAM/Lixo.")
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print("\n" + "=" * 70)
        print("✗ ERRO DE AUTENTICAÇÃO")
        print("=" * 70)
        print("\n❌ Falha ao fazer login no Gmail!")
        print("\nPossíveis causas:")
        print("1. EMAIL_SENDER está incorreto")
        print("2. EMAIL_PASSWORD está incorreto ou faltam caracteres")
        print("3. Você não gerou a 'Senha de App' do Gmail")
        print("4. Verificação em duas etapas não está ativada")
        print(f"\nErro: {e}")
        return False
        
    except smtplib.SMTPException as e:
        print("\n" + "=" * 70)
        print("✗ ERRO DE SMTP")
        print("=" * 70)
        print(f"\n❌ Erro de conexão com o servidor Gmail: {e}")
        print("\nPossíveis causas:")
        print("1. Problemas de conexão com a internet")
        print("2. Firewall bloqueando a porta 587")
        print("3. Gmail recusando a conexão")
        return False
        
    except Exception as e:
        print("\n" + "=" * 70)
        print("✗ ERRO DESCONHECIDO")
        print("=" * 70)
        print(f"\n❌ Erro: {e}")
        print(f"Tipo: {type(e).__name__}")
        return False

if __name__ == "__main__":
    testar_email()
