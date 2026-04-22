from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from datetime import date

class ModelEstudanteTestCase(TestCase):
    #def teste_falha(self):
    #    self.fail('Teste falhou :(')

    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testemodelo@gmail.com',
            cpf = '32592784004',
            data_nascimento = '2023-02-02',
            celular = '86 99999-9999'
        )
    

    def test_verifica_atributos_de_estudante(self):
        """Teste que verifica os atributos do modelo de Estudante"""
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'testemodelo@gmail.com')
        self.assertEqual(self.estudante.cpf, '32592784004')
        self.assertEqual(self.estudante.data_nascimento, '2023-02-02')
        self.assertEqual(self.estudante.celular, '86 99999-9999')




class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'Teste de Codigo',
            descricao = 'Descricao do Curso',
            nivel = 'Niveis de dificuldade'
        )

    
    def test_verifica_atributos_do_curso(self):
        """Teste que verifica os atributos do modelo de Curso"""
        self.assertEqual(self.curso.codigo, 'Teste de Codigo')
        self.assertEqual(self.curso.descricao, 'Descricao do Curso')
        self.assertEqual(self.curso.nivel, 'Niveis de dificuldade')



class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
        nome='Teste de Estudante',
        email='teste@gmail.com',
        cpf='12345678900',
        data_nascimento=date(2000, 1, 1),
        celular='11 99999-9999'
)

        self.curso = Curso.objects.create(
            codigo='CURSO2',
            descricao='Teste de Curso',
            nivel='B'
        )

        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo='Teste de periodo'
        )

    def test_verifica_atributos_da_matricula(self):
        self.assertEqual(self.matricula.estudante, self.estudante)
        self.assertEqual(self.matricula.curso, self.curso)
        self.assertEqual(self.matricula.periodo, 'Teste de periodo')