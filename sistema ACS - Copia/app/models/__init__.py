from app import db
from .user import User
from .cadastro import (CadastroIndividual, 
                      InfoSociodemografica, 
                      CondicoesSaude, 
                      SituacaoRua, 
                      SaidaCadastro)

# Esto hace que los modelos estén disponibles cuando se importa el paquete models
__all__ = [
    'User',
    'CadastroIndividual',
    'InfoSociodemografica', 
    'CondicoesSaude',
    'SituacaoRua',
    'SaidaCadastro'
] 