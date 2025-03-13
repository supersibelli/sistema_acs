# Sistema ACS (Agentes Comunitários de Saúde)

Sistema de gestão para Agentes Comunitários de Saúde que permite o registro e acompanhamento de informações de cidadãos e visitas domiciliares.

## Estado Atual
O projeto está em desenvolvimento ativo, atualmente na versão 0.1.0.

### Implementado:
- ✅ Sistema de autenticação
- ✅ Formulário de Cadastro Individual (Primeira seção)
- ⏳ Formulário de Cadastro Domiciliar (Pendente)
- ⏳ Formulário de Visita Domiciliar (Pendente)

## Tecnologias
- Python 3.8+
- Flask 2.0+
- SQLite (Desenvolvimento)
- Bootstrap 5
- JavaScript

## Instalação

1. Clonar o repositório:
   ```bash
   git clone [url-do-repositório]
   cd sistema-acs
   ```

2. Criar ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instalar dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicializar o banco de dados:
   ```bash
   flask db upgrade
   ```

5. Executar o servidor de desenvolvimento:
   ```bash
   flask run
   ```

## Estrutura do Projeto 