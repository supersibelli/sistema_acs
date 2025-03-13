import unittest
from app import create_app, db
from app.models.cadastro_individual import CadastroIndividual

class TestCadastroIndividual(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_novo_cadastro(self):
        cadastro = CadastroIndividual(
            nome_completo='Test User',
            data_nascimento='1990-01-01',
            sexo='M',
            nacionalidade='brasileira'
        )
        db.session.add(cadastro)
        db.session.commit()
        
        self.assertIsNotNone(cadastro.id) 