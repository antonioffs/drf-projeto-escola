from django.http import response
from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso = 'CTT1', 
            descricao = 'Curso teste 1', 
            nivel = 'B'
        )
        self.curso_1 = Curso.objects.create(
            codigo_curso = 'CTT2', 
            descricao = 'Curso teste 2', 
            nivel = 'A'
        )


    # def test_falhador(self):
    #     self.fail('O teste falhou de proposito')


    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar se a requisição GET lista os cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


    def test_requisicao_post_para_criar_novo_curso(self):
        """Teste para criação de um curso, método POST"""
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso teste 3',
            'nivel': 'A'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


    def test_requisicao_delete_para_deletar_curso(self):
        """Teste para verificar a requisição DELETE não permitida para deletar um curso"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    

    def test_requisicao_put_para_atualizar_curso(self):
        """Teste para verificar requisicao PUT para atualizar curso"""
        data = {
            'codigo_curso': 'CTT1',
            'descricao': 'Curso Teste 1 Atualizado',
            'nivel': 'I'
        }
    
        response = self.client.put('/cursos/1/', data=data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)