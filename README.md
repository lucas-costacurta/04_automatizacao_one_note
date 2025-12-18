# OneNote Automation - Estrutura de Estudos para Engenharia de Dados

> Automatize a criação de uma estrutura completa e organizada de estudos no OneNote usando Python e Microsoft Graph API

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Microsoft Graph API](https://img.shields.io/badge/Microsoft%20Graph-API-orange)](https://docs.microsoft.com/graph/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Índice

- [Sobre](#sobre)
- [Funcionalidades](#funcionalidades)
- [Estrutura Criada](#estrutura-criada)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração Azure](#configuração-azure)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Troubleshooting](#troubleshooting)
- [Aprendizados](#aprendizados)
- [Melhorias Futuras](#melhorias-futuras)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

---

## 🎯 Sobre

Este projeto automatiza a criação de um notebook completo no **Microsoft OneNote** com uma estrutura organizada para estudos em **Engenharia de Dados**. 

Ao invés de criar manualmente 13 seções e mais de 50 páginas, este script faz tudo automaticamente em alguns minutos usando a **Microsoft Graph API**.

**Problema resolvido:** Organização é fundamental para absorver conhecimento em uma área extensa como Engenharia de Dados. Este script elimina o trabalho manual de estruturação inicial.

**Contexto:** Desenvolvido como parte da minha transição de **Analista de BI Sênior** para **Engenheiro de Dados**, aplicando conceitos de automação e integração com APIs.

---

## ✨ Funcionalidades

- ✅ **Criação automática** de notebook no OneNote
- ✅ **13 seções organizadas** por tópicos de Engenharia de Dados
- ✅ **50+ páginas** pré-estruturadas para anotações
- ✅ **Autenticação segura** via OAuth2 com Microsoft
- ✅ **Validação de nomes** (remove caracteres inválidos automaticamente)
- ✅ **Verificação de duplicatas** (não recria se já existe)
- ✅ **Rate limiting inteligente** (evita bloqueio da API)
- ✅ **Cache de credenciais** (não precisa logar toda vez)

---

## 📚 Estrutura Criada

O script cria automaticamente o seguinte notebook:

```
📓 Data Engineering
│
├── 📂 1. Fundamentos
│   ├── 📄 Conceitos Essenciais
│   ├── 📄 Arquiteturas de Dados
│   ├── 📄 Modelagem de Dados
│   └── 📄 Glossário Técnico
│
├── 📂 2. SQL e Bancos de Dados
│   ├── 📄 SQL Básico
│   ├── 📄 SQL Avançado
│   ├── 📄 Bancos Relacionais
│   ├── 📄 Bancos NoSQL
│   └── 📄 Snippets SQL Úteis
│
├── 📂 3. Python para Engenharia de Dados
│   ├── 📄 Python Essencial
│   ├── 📄 Pandas
│   ├── 📄 Bibliotecas Importantes
│   └── 📄 Code Snippets
│
├── 📂 4. Cloud Computing
│   ├── 📄 AWS
│   ├── 📄 GCP
│   ├── 📄 Azure
│   ├── 📄 Comandos CLI Úteis
│   └── 📄 Comparativo de Serviços
│
├── 📂 5. Ferramentas de Orquestração
├── 📂 6. Big Data e Processamento
├── 📂 7. Data Warehousing Moderno
├── 📂 8. DevOps e Infraestrutura
├── 📂 9. Qualidade e Governança de Dados
├── 📂 10. Projetos e Portfolio
├── 📂 11. Carreira e Mercado
├── 📂 12. Recursos e Referências
└── 📂 13. Anotações Rápidas
```

**Total:** 13 seções | 50+ páginas

---

## 🛠️ Tecnologias

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| Python | 3.8+ | Linguagem principal |
| MSAL | 1.24+ | Autenticação Microsoft |
| Requests | 2.31+ | Consumo da API |
| python-dotenv | 1.0+ | Gerenciamento de variáveis de ambiente |
| Microsoft Graph API | v1.0 | API do OneNote |

---

## 📦 Pré-requisitos

Antes de começar, você precisa ter:

- ✅ [Python 3.8+](https://www.python.org/downloads/)
- ✅ [Git](https://git-scm.com/)
- ✅ Conta Microsoft (Hotmail, Outlook, etc.)
- ✅ OneNote instalado ou acesso ao OneNote Online
- ✅ Conta no Azure Portal (gratuita)

> ⚠️ **Importante:** O registro no Azure Portal é **100% gratuito** e não gera custos!

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/lucas-costacurta/onenote-automation.git
cd onenote-automation
```

### 2. Crie um ambiente virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar no Windows:
venv\Scripts\activate

# Ativar no Linux/Mac:
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

**Conteúdo do `requirements.txt`:**
```
msal==1.24.0
requests==2.31.0
python-dotenv==1.0.0
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
CLIENT_ID=seu-client-id-aqui
```

> ⚠️ **Importante:** Você vai obter o `CLIENT_ID` na próxima etapa (Configuração Azure)

---

## ☁️ Configuração Azure

Esta é a etapa mais importante! Siga cuidadosamente:

### Passo 1: Acessar o Azure Portal

1. Acesse: https://portal.azure.com
2. Faça login com sua conta Microsoft (a mesma do OneNote)

### Passo 2: Criar App Registration

1. Procure por **"Azure Active Directory"** ou **"Microsoft Entra ID"**
2. No menu lateral esquerdo, clique em **"App registrations"**
3. Clique em **"+ New registration"**

### Passo 3: Configurar o App

Preencha os campos:

| Campo | Valor |
|-------|-------|
| **Name** | `OneNote Automation` (ou qualquer nome) |
| **Supported account types** | Selecione: **"Accounts in any organizational directory and personal Microsoft accounts"** |
| **Redirect URI** | Tipo: `Public client/native (mobile & desktop)`<br>URL: `http://localhost` |

4. Clique em **"Register"**

### Passo 4: Copiar Client ID

1. Na página que abrir, você verá **"Application (client) ID"**
2. **Copie este ID** - você vai precisar dele!
3. Cole no arquivo `.env` que você criou

### Passo 5: Configurar Permissões

1. No menu lateral esquerdo, clique em **"API permissions"**
2. Clique em **"+ Add a permission"**
3. Selecione **"Microsoft Graph"**
4. Selecione **"Delegated permissions"**
5. Na busca, procure e marque:
   - ☑️ `Notes.ReadWrite`
   - ☑️ `Notes.Create`
6. Clique em **"Add permissions"**

### Passo 6: Ajustar Audience (se necessário)

Se você receber erro de `userAudience`:

1. Clique em **"Manifest"** no menu lateral
2. Procure por `"signInAudience"`
3. Certifique-se que está como:
   ```json
   "signInAudience": "AzureADandPersonalMicrosoftAccount",
   ```
4. Clique em **"Save"**

✅ **Pronto!** Configuração do Azure concluída!

---

## 💻 Como Usar

### Execução básica

```bash
python main.py
```

### O que acontece ao executar:

1. 🔐 **Autenticação** - Abrirá o navegador para login (só na primeira vez)
2. 📓 **Criação do notebook** - Verifica se já existe, senão cria
3. 📂 **Criação das seções** - Cria as 13 seções principais
4. 📄 **Criação das páginas** - Cria todas as páginas dentro de cada seção

**Tempo estimado:** 3-5 minutos

### Saída esperada:

```
============================================================
CRIANDO ESTRUTURA DE ESTUDOS NO ONENOTE
============================================================

PASSO 1: Autenticação
Abrindo navegador para autenticação...
✓ Autenticação realizada com sucesso!

PASSO 2: Criando/Verificando Notebook
✓ Notebook 'Data Engineering' criado: abc123...

PASSO 3: Criando Seções e Páginas
(Isso pode levar alguns minutos...)

[1/13] Criando seção: 1. Fundamentos
  ✓ Seção '1. Fundamentos' criada
    ✓ Página 'Conceitos Essenciais' criada
    ✓ Página 'Arquiteturas de Dados' criada
    ✓ Página 'Modelagem de Dados' criada
    ✓ Página 'Glossário Técnico' criada

[2/13] Criando seção: 2. SQL e Bancos de Dados
...

============================================================
✓ ESTRUTURA CRIADA COM SUCESSO!
============================================================

Abra o OneNote e você verá o notebook 'Data Engineering'
com todas as seções e páginas organizadas!
```

---

## 📁 Estrutura do Projeto

```
onenote-automation/
│
├── docs/
│   └── images/
│       └── onenote-structure.png
│
├── main.py                 # Script principal
├── requirements.txt        # Dependências Python
├── .env                    # Variáveis de ambiente (CLIENT_ID)
├── .env.example           # Exemplo de .env
├── .gitignore             # Arquivos ignorados pelo Git
└── README.md              # Este arquivo
```

---

## 🔧 Troubleshooting

### Erro: "invalid_tenant" ou "commom not found"

**Causa:** Typo no código - escreveu `"commom"` ao invés de `"common"`

**Solução:** 
```python
TENANT_ID = "common"  # ✅ Correto (com 1 "m")
```

---

### Erro: "userAudience configuration"

**Causa:** App configurado como "Personal accounts only" mas usando endpoint `/common/`

**Solução:** Siga o [Passo 6 da Configuração Azure](#passo-6-ajustar-audience-se-necessário)

---

### Erro: "The name value contains invalid characters"

**Causa:** Caracteres especiais (`&`, `#`, etc.) no nome das seções

**Solução:** O script já tem a função `sanitize_name()` que resolve isso automaticamente. Se ainda ocorrer, verifique se está usando a versão atualizada.

---

### Erro: "Rate limit exceeded"

**Causa:** Muitas requisições em pouco tempo

**Solução:** O script já tem delays (`time.sleep()`). Se persistir, aumente os valores:
```python
time.sleep(2)  # Era 1, aumentou para 2
```

---

### Seções não aparecem no OneNote

**Solução:**
1. Feche e abra o OneNote
2. Clique em "Sincronizar"
3. Aguarde alguns segundos

---

### Precisa autenticar toda vez

**Solução:** O cache de credenciais funciona automaticamente. Se pedir toda vez:
1. Verifique se tem permissão de escrita na pasta
2. Execute o script sempre da mesma pasta

---

## 🎓 Aprendizados Técnicos

Este projeto foi uma excelente oportunidade para aprender:

### 1. **Autenticação OAuth2**
- Fluxo de autenticação interativa
- Token de acesso e refresh
- Cache de credenciais

### 2. **APIs REST**
- Consumo da Microsoft Graph API
- Headers de autenticação (Bearer token)
- Tratamento de respostas HTTP

### 3. **Rate Limiting**
- Por que APIs limitam requisições
- Estratégias de delay entre chamadas
- Importância do `time.sleep()`

### 4. **Validação de Dados**
- Sanitização de strings
- Remoção de caracteres especiais
- Normalização de espaços

### 5. **Integração com Serviços Cloud**
- Azure Active Directory
- Microsoft Graph API
- Permissões delegadas

### 6. **Boas Práticas**
- Variáveis de ambiente (`.env`)
- Separação de configuração e código
- Funções modulares e reutilizáveis

---

## 🗺️ Melhorias Futuras

- [ ] Interface gráfica (GUI) com Tkinter/PyQt
- [ ] Suporte para estruturas customizadas (JSON/YAML)
- [ ] Backup/exportação da estrutura
- [ ] Integração com Notion/Obsidian
- [ ] Templates diferentes por área de estudo
- [ ] CLI interativo para escolher seções
- [ ] Deploy como webapp (Flask/Streamlit)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

---

## 👤 Autor

**Lucas Costacurta Ferro**

- GitHub: [@lucas-costacurta](https://github.com/lucas-costacurta)
- LinkedIn: [Lucas Costacurta Ferro](https://www.linkedin.com/in/lucascferro/)

---

## 📚 Recursos Úteis

- [Microsoft Graph Explorer](https://developer.microsoft.com/graph/graph-explorer) - Teste APIs online
- [OneNote API Reference](https://docs.microsoft.com/graph/api/resources/onenote)
- [OAuth 2.0 Explained](https://oauth.net/2/)
