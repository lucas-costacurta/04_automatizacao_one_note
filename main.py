# Configuração + estrutura do OneNote

import os
import msal
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")

CLIENT_ID = client_id
TENANT_ID = "common"
SCOPES = ["Notes.ReadWrite", "Notes.Create"]

# Estrutura do caderno

NOTEBOOK_NAME = "Data Engineering"

SECTIONS = {
    "1. Fundamentos": [
        "Conceitos Essenciais",
        "Arquiteturas de Dados",
        "Modelagem de Dados",
        "Glossário Técnico"
    ],
    "2. SQL & Bancos de Dados": [
        "SQL Básico",
        "SQL Avançado",
        "Bancos Relacionais",
        "Bancos NoSQL",
        "Snippets SQL Úteis"
    ],
    "3. Python para Engenharia de Dados": [
        "Python Essencial",
        "Pandas",
        "Bibliotecas Importantes",
        "Code Snippets"
    ],
    "4. Cloud Computing": [
        "AWS",
        "GCP",
        "Azure",
        "Comandos CLI Úteis",
        "Comparativo de Serviços"
    ],
    "5. Ferramentas de Orquestração": [
        "Apache Airflow",
        "Prefect",
        "Dagster",
        "Outros"
    ],
    "6. Big Data & Processamento": [
        "Apache Spark",
        "Processamento em Batch",
        "Streaming"
    ],
    "7. Data Warehousing Moderno": [
        "dbt (data build tool)",
        "Snowflake",
        "BigQuery",
        "Redshift"
    ],
    "8. DevOps & Infraestrutura": [
        "Git & GitHub",
        "Docker",
        "CI/CD",
        "Kubernetes (Básico)",
        "Terraform (Básico)"
    ],
    "9. Qualidade & Governança de Dados": [
        "Data Quality",
        "Data Observability",
        "Data Governance"
    ],
    "10. Projetos & Portfolio": [
        "Projeto 1: ETL Simples",
        "Projeto 2: Data Warehouse",
        "Projeto 3: Pipeline Cloud",
        "Projeto 4: Streaming",
        "Ideias de Projetos Futuros"
    ],
    "11. Carreira & Mercado": [
        "Roadmap de Estudos",
        "Vagas e Requisitos",
        "Networking",
        "Entrevistas",
        "Currículo & LinkedIn"
    ],
    "12. Recursos & Referências": [
        "Cursos Online",
        "Livros",
        "Blogs & Sites",
        "YouTube Channels",
        "Datasets Públicos",
        "Ferramentas & SaaS"
    ],
    "13. Anotações Rápidas": [
        "Daily Notes",
        "Problemas Resolvidos",
        "Links para Revisitar",
        "Perguntas a Pesquisar"
    ]
}

# Autenticação

# Obtendo token de acesso a conta
def get_access_token():
    app = msal.PublicClientApplication(
        CLIENT_ID,
        authority = f"https://login.microsoftonline.com/{TENANT_ID}"
    )

    # Verificando credenciais em cache
    accounts = app.get_accounts()
    if accounts: 
        print("Conta encontrada...")
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
        if result:
            return result['access_token']
    print('Abrindo navegador para autenticação...')
    result = app.acquire_token_interactive(SCOPES)

    if "access_token"in result:
        print('Autenticação realizada com sucesso')
        return result['access_token']
    else: 
        print(f'Erro na autenticação: {result.get('error_description')}')
        return None

# Funções da API

def sanitize_name(name):
    invalid_chars = ['?', '*', '\\', '/', ':', '<', '>', '|', '&', '#', "'", '%', '~']
    sanitized = name
    for char in invalid_chars:
        sanitized = sanitized.replace(char, ' ')
    sanitized = ' '.join(sanitized.split())
    return sanitized

def create_notebook(token, notebook_name):
    url = "https://graph.microsoft.com/v1.0/me/onenote/notebooks"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        'displayName': notebook_name
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        notebook_id = response.json()['id']
        print(f'Notebook "{notebook_name}" criado: {notebook_id}')
        return notebook_id
    else: 
        print(f"Erro ao criar o notebook: {response.text}")
        return None
    
def get_existing_notebook(token, notebook_name):
    url = "https://graph.microsoft.com/v1.0/me/onenote/notebooks"
    headers = {'Authorization': f'Bearer {token}'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        notebooks = response.json().get('value', [])
        for notebook in notebooks:
            if notebook['displayName'] == notebook_name:
                print(f"Notebook '{notebook_name}' já existe")
                return notebook['id']
    return None
    
def create_section(token, notebook_id, section_name):
    url = f"https://graph.microsoft.com/v1.0/me/onenote/notebooks/{notebook_id}/sections"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        'displayName': section_name
    }
    
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        section_id = response.json()['id']
        print(f"Seção '{section_name}' criada.")
        return section_id
    else: 
        print(f"Erro ao criar a seção '{section_name}': {response.text}")
        return None
    
def create_page(token, section_id, page_title):
    url = f"https://graph.microsoft.com/v1.0/me/onenote/sections/{section_id}/pages"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/xhtml+xml'
    }
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
      <head>
        <title>{page_title}</title>
      </head>
      <body>
        <h1>{page_title}</h1>
        <p>📝 Anotações sobre: {page_title}</p>
        <br/>
        <p style="color: #666;">Criado automaticamente - Comece suas anotações aqui!</p>
      </body>
    </html>
    """

    response = requests.post(url, headers=headers, data=html_content)

    if response.status_code == 201:
        print(f"Página '{page_title}' criada")
        return True
    else: 
        print(f"Erro ao criar a página '{page_title}'")
        return False

#  Função principal  
def create_onenote_structure():
    print("=" * 60)
    print("CRIANDO ESTRUTURA DE ESTUDOS NO ONENOTE")
    print("=" * 60)
    print()
    
    print("PASSO 1: Autenticação")
    token = get_access_token()
    if not token:
        print("Falha na autenticação. Verifique as configurações.")
        return
    print()
    
    print("PASSO 2: Criando/Verificando Notebook")
    notebook_id =  get_existing_notebook(token, NOTEBOOK_NAME)
    if not notebook_id:
        notebook_id = create_notebook(token, NOTEBOOK_NAME)
    
    if not notebook_id:
        print("Não foi possível criar o notebook.")
        return
    print()

    print("PASSO 3: Criando Seções e Páginas")
    print("(Isso pode levar alguns minutos...)")
    print()
    
    total_sections = len(SECTIONS)
    current_section = 0
    
    for section_name, pages in SECTIONS.items():
        current_section += 1
        print(f"[{current_section}/{total_sections}] Criando seção: {section_name}")
        
        section_id = create_section(token, notebook_id, section_name)
        
        if section_id:
            # Pequeno delay para evitar rate limiting
            time.sleep(1)
            
            for page_title in pages:
                create_page(token, section_id, page_title)
                time.sleep(0.5)
        
        print()
    
    print("=" * 60)
    print("✓ ESTRUTURA CRIADA COM SUCESSO!")
    print("=" * 60)
    print()
    print(f"Abra o OneNote e você verá o notebook '{NOTEBOOK_NAME}'")
    print("com todas as seções e páginas organizadas!")

# EXECUÇÃO
if __name__ == "__main__":
    if CLIENT_ID != client_id:
        print("Validar")
    else:
        create_onenote_structure()