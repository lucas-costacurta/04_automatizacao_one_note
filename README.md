# 04_automatizacao_one_note
Automatização para criação de caderno no OneNote

1. Registrar aplicação no Azure (IMPORTANTE)
Este é o único passo "chato", mas é necessário para acessar sua conta OneNote com segurança:

- Acesse: https://portal.azure.com
- Faça login com sua conta Microsoft (a mesma do OneNote)
- Procure por "Azure Active Directory" ou "Microsoft Entra ID"
- No menu lateral, clique em "App registrations"
- Clique em "+ New registration"
- Preencha:

    Nome: "OneNote Automation" (ou o que você quiser)
    Supported account types: Selecione "Personal Microsoft accounts only"
    Redirect URI: Selecione "Public client/native (mobile & desktop)" e coloque: http://localhost

- Clique em "Register"
- Na página que abrir, copie o "Application (client) ID" - você vai precisar dele!
- No menu lateral, clique em "API permissions"
- Clique em "+ Add a permission"
- Selecione "Microsoft Graph"
- Selecione "Delegated permissions"
- Procure e adicione:

    Notes.ReadWrite
    Notes.Create

- Clique em "Add permissions"
