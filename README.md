# Folha de Pagamento → Excel com Sistema de Segurança

Aplicação Flask para converter extratos de folha de pagamento (PDF) em planilhas Excel formatadas, com um **robusto sistema de segurança** que monitora tentativas de acesso.

## 🔐 Sistema de Segurança

### Funcionalidades Implementadas:

✅ **Autenticação por Senha**
- Proteção de todas as rotas principais
- Redirect automático para login se não autenticado

✅ **Monitoramento de Tentativas Falhadas**
- Contador de tentativas por IP do cliente
- Armazena histórico em arquivo JSON

✅ **Bloqueio após 3 Tentativas**
- IP bloqueado após 3 senhas incorretas
- Mensagem informando que foi bloqueado

✅ **Alerta de Segurança por Email**
- Captura informações do IP do cliente
- Obtém geolocalização (país, estado, cidade, ISP)
- Envia email detalhado para o administrador
- Email inclui: IP público, IP privado, localização completa, data/hora da tentativa

✅ **Armazenamento de Dados**
- Arquivo `tentativas_login.json` para rastrear tentativas
- Seguro e fácil de revisar

---

## 🚀 Configuração Inicial

### 1. **Instale as Dependências**

```bash
pip install -r requirements.txt
```

### 2. **Configure as Credenciais de Email** (IMPORTANTE!)

Edite o arquivo `App.py` e procure pela seção `CONFIGURAÇÃO DE SEGURANÇA`:

```python
# ════════════════════════════════════════════════════════════════════════════
# ─── CONFIGURAÇÃO DE SEGURANÇA ───────────────────────────────────────────
# ════════════════════════════════════════════════════════════════════════════

SENHA_ADMIN = "admin123"  # 👈 MUDE ISSO PARA UMA SENHA FORTE!
EMAIL_ADMIN = "gregorydeabreu89@gmail.com"  # 👈 Email para receber alertas
ARQUIVO_TENTATIVAS = 'tentativas_login.json'

# Configuração de email
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "seu_email@gmail.com"  # 👈 MUDE PARA SEU EMAIL DO GMAIL
EMAIL_PASSWORD = "sua_senha_app@gmail.com"  # 👈 MUDE PARA SENHA DE APP DO GMAIL
```

#### **Como Gerar Senha de App do Gmail:**

Se estiver usando Gmail:

1. Acesse [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Selecione "Mail" e "Windows Computer"
3. Google vai gerar uma senha com 16 caracteres
4. Cole essa senha em `EMAIL_PASSWORD`

**⚠️ SEGURANÇA:** Nunca use sua senha de Gmail diretamente! Use sempre a "Senha de App".

---

### 3. **Inicie a Aplicação**

```bash
python App.py
```

A aplicação estará disponível em: **http://localhost:5050**

---

## 📋 Fluxo de Uso

### **Login Bem-Sucedido:**
1. Usuário acessa `http://localhost:5050`
2. Redireciona para `/login`
3. Digite a senha correta
4. Acesso concedido → Página principal

### **Tentativa Falhada:**
1. Senha incorreta → Mensagem de erro
2. Mostra tentativas restantes (ex: 2 de 3)
3. Após 3 erros → IP bloqueado
4. **Email de alerta enviado automaticamente**

---

## 📧 Conteúdo do Email de Alerta

Quando 3 tentativas falhadas são detectadas, um email é enviado com:

- **IP Público:** Ex: `203.0.113.42`
- **IP do Cliente:** Ex: `192.168.1.100`
- **País:** Ex: `Brazil`
- **Estado/Região:** Ex: `São Paulo`
- **Cidade:** Ex: `São Paulo`
- **ISP/Operadora:** Ex: `Vivo Telecom`
- **Data/Hora:** `02/06/2026 às 14:35:42`

---

## 📁 Arquivos do Sistema

```
Leitura da folha/
├── App.py                    # Aplicação Flask principal
├── index.html                # Página principal (protegida)
├── login.html                # Formulário de login
├── requirements.txt          # Dependências Python
├── tentativas_login.json     # Arquivo de histórico (criado automaticamente)
└── README.md                 # Este arquivo
```

---

## 🔄 Redefinindo Tentativas Bloqueadas

Se precisar desbloquear um IP, edite o arquivo `tentativas_login.json`:

```json
{
  "203.0.113.42": {
    "tentativas": 3,
    "bloqueado": true,
    "primeira_tentativa": "2026-06-02T14:30:00",
    "ultima_tentativa": "2026-06-02T14:35:42"
  }
}
```

**Para desbloquear:** Delete a entrada do IP ou mude `"bloqueado": false`

---

## 🛡️ Dicas de Segurança

✓ Use uma senha forte (não use `admin123`)  
✓ Use "Senha de App" do Gmail, não sua senha principal  
✓ Monitore o arquivo `tentativas_login.json` regularmente  
✓ Mude a `app.secret_key` para uma chave segura em produção  
✓ Use HTTPS em produção  

---

## 🐛 Troubleshooting

### **Email não está sendo enviado:**
- Verifique se EMAIL_SENDER e EMAIL_PASSWORD estão corretos
- Certifique-se de usar "Senha de App" do Gmail
- Verifique se o Gmail permitiu acesso a apps menos seguros (configurações)

### **IP não está sendo capturado corretamente:**
- Se estiver usando proxy/reverse proxy, configure:
  ```python
  if request.headers.getlist("X-Forwarded-For"):
      ip = request.headers.getlist("X-Forwarded-For")[0]
  ```

### **Geolocalização não funciona:**
- A API `ipapi.co` é gratuita e não requer chave
- Alguns IPs privados (192.168.x.x) não podem ser geolocalizados
- A função retorna "Não disponível" se a API falhar

---

## 📞 Suporte

Para problemas com a geolocalização de IP ou envio de emails, revise os logs da aplicação quando executar:

```bash
python App.py
```

Mensagens de sucesso/erro serão exibidas no terminal.

---

## 📜 Licença

Sistema de Gestão de Folha de Pagamento — Junho 2026
