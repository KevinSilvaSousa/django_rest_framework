from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer
from rest_framework import viewsets, generics
from rest_framework.throttling import UserRateThrottle
from escola.throttles import MatriculaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class EstudanteViewSet(viewsets.ModelViewSet): 
    """
    Descrição da View:
    - Visualização dos estudantes
    - Visualização em ordem por ID
    """
    queryset = Estudante.objects.all().order_by("id")
    serializer_class = EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Visualização das Matriculas
    - Pega todas as matriculas por ordem de ID
    """
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Visualização das Matriculas
    - Pega todas as matriculas por ordem de ID
    Metodos permitidos:
    GET e POST
    """
    queryset = Matricula.objects.all().order_by("id")
    serializer_class =  MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]

class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        """
        Descrição da View:
        - Lista Matriculas por id de Estudante
        Parâmetros:
        - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
        """
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")
        return queryset
    
    serializer_class = ListaMatriculasEstudanteSerializer



class ListaMatriculaCurso(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """ 
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by("id")
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer