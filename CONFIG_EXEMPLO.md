# 🔐 CONFIGURAÇÃO DE SEGURANÇA - EXEMPLO

# Este arquivo mostra onde fazer as alterações no App.py para configurar o sistema de segurança

# ════════════════════════════════════════════════════════════════════════════
# ─── PASSO 1: ALTERE A SENHA DE ADMINISTRADOR ──────────────────────────────
# ════════════════════════════════════════════════════════════════════════════

# No App.py, procure por:
SENHA_ADMIN = "admin123"  # ❌ NÃO USE ISSO EM PRODUÇÃO!

# E mude para uma senha forte, por exemplo:
SENHA_ADMIN = "minha_senha_super_segura_2026!"

# Dicas para senha forte:
# ✓ Pelo menos 12 caracteres
# ✓ Misture maiúsculas, minúsculas, números e símbolos
# ✓ Não use informações pessoais
# ✓ Não use padrões simples (123456, qwerty, etc)


# ════════════════════════════════════════════════════════════════════════════
# ─── PASSO 2: CONFIGURE O EMAIL PARA RECEBER ALERTAS ───────────────────────
# ════════════════════════════════════════════════════════════════════════════

# No App.py, procure por:
EMAIL_ADMIN = "gregorydeabreu89@gmail.com"  # ✓ Já está configurado para você!

# Este é o email que receberá os alertas quando 3 tentativas falhadas forem detectadas.
# Se quiser mudar para outro email, edite aqui.


# ════════════════════════════════════════════════════════════════════════════
# ─── PASSO 3: CONFIGURE O EMAIL DO REMETENTE (IMPORTANTE!) ──────────────────
# ════════════════════════════════════════════════════════════════════════════

# No App.py, procure por:
EMAIL_SENDER = "seu_email@gmail.com"  # ❌ MUDE ISTO!
EMAIL_PASSWORD = "sua_senha_app@gmail.com"  # ❌ MUDE ISTO!

# Exemplo de como ficar após configuração:
EMAIL_SENDER = "sua.empresa@gmail.com"
EMAIL_PASSWORD = "abcd efgh ijkl mnop"  # Senha de App do Gmail (16 caracteres)


# ════════════════════════════════════════════════════════════════════════════
# ─── COMO GERAR UMA SENHA DE APP DO GMAIL (PASSO A PASSO) ──────────────────
# ════════════════════════════════════════════════════════════════════════════

# 1. Vá para: https://myaccount.google.com/apppasswords
#    (Certifique-se de estar logado na sua conta do Gmail)

# 2. Se você NÃO VIR a opção "App passwords":
#    - Acesse: https://myaccount.google.com/security
#    - Ative a "Verificação em duas etapas"
#    - Depois retorne a apppasswords

# 3. Selecione:
#    - Select app: "Mail"
#    - Select device: "Windows Computer" (ou seu sistema)

# 4. Google gerará uma senha de 16 caracteres com espaços:
#    Exemplo: "abcd efgh ijkl mnop"

# 5. Copie e cole no App.py em EMAIL_PASSWORD

# ⚠️  SEGURANÇA CRÍTICA:
#    - NUNCA use sua senha principal do Gmail
#    - Use APENAS a "Senha de App"
#    - A senha de app é segura mesmo se compartilhada (pode ser revogada)


# ════════════════════════════════════════════════════════════════════════════
# ─── PASSO 4: CONFIGURE A CHAVE SECRETA DA SESSÃO (PRODUÇÃO) ────────────────
# ════════════════════════════════════════════════════════════════════════════

# No App.py, procure por:
app.secret_key = 'sua_chave_secreta_aqui_mude_em_producao'

# Para produção, gere uma chave aleatória. No Python, execute:
import secrets
secrets.token_hex(32)  # Isso gera uma string aleatória de 64 caracteres

# Exemplo do resultado:
app.secret_key = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6'


# ════════════════════════════════════════════════════════════════════════════
# ─── RESUMO DAS MUDANÇAS ────────────────────────────────────────────────────
# ════════════════════════════════════════════════════════════════════════════

CONFIGURAÇÕES OBRIGATÓRIAS:
  ✓ SENHA_ADMIN - Senha forte para login
  ✓ EMAIL_SENDER - Seu email do Gmail
  ✓ EMAIL_PASSWORD - Senha de App do Gmail

CONFIGURAÇÕES OPCIONAIS:
  • EMAIL_ADMIN - Email para receber alertas (já está gregorydeabreu89@gmail.com)
  • app.secret_key - Para produção apenas


# ════════════════════════════════════════════════════════════════════════════
# ─── TESTANDO A CONFIGURAÇÃO ────────────────────────────────────────────────
# ════════════════════════════════════════════════════════════════════════════

# 1. Faça as alterações acima
# 2. Execute: python App.py
# 3. Acesse: http://localhost:5050
# 4. Você será redirecionado para /login
# 5. Digite a SENHA_ADMIN que você configurou
# 6. Se entrar com sucesso, está pronto!

# Para testar o alerta de email:
# 1. Acesse http://localhost:5050/login novamente
# 2. Digite uma senha ERRADA 3 vezes
# 3. Seu IP será bloqueado
# 4. Você deverá receber um email em EMAIL_ADMIN com os detalhes da tentativa

# ⚠️  Se o email não chegar:
#    - Verifique a pasta de Spam
#    - Verifique os logs no terminal (python App.py)
#    - Confirme que EMAIL_SENDER e EMAIL_PASSWORD estão corretos
#    - Certifique-se de usar "Senha de App", não sua senha principal


# ════════════════════════════════════════════════════════════════════════════
# ─── SEGURANÇA EM PRODUÇÃO ──────────────────────────────────────────────────
# ════════════════════════════════════════════════════════════════════════════

RECOMENDAÇÕES:
  ✓ Use HTTPS (não HTTP)
  ✓ Mude app.secret_key para algo seguro
  ✓ Use um banco de dados em vez de arquivo JSON para tentativas
  ✓ Implemente rate limiting
  ✓ Use variáveis de ambiente para credenciais (não hardcoded)
  ✓ Monitore regularmente os alertas de email
  ✓ Revise o arquivo tentativas_login.json periodicamente

EXEMPLO COM VARIÁVEIS DE AMBIENTE:
  import os
  EMAIL_SENDER = os.environ.get('EMAIL_SENDER')
  EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
  SENHA_ADMIN = os.environ.get('SENHA_ADMIN')
