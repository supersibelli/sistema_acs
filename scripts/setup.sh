#!/bin/bash
# Script de configuração inicial

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Inicializar banco de dados
flask db upgrade 