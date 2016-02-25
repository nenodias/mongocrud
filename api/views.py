from rest_framework_mongoengine.viewsets import ModelViewSet
from .mixins import DefaultMixin, LoginMixin
from .serializers import *
from .models import *

class UsuarioViewSet(DefaultMixin, ModelViewSet):
    serializer_class = UsuarioSerializer

    def __init__(self, *args, **kwargs):
        super(UsuarioViewSet, self).__init__(*args, **kwargs)
        self.queryset = Usuario.objects.all()

    def get_queryset(self):
        self.queryset = super().get_queryset()
        if self.request.GET.get('email'):
            self.queryset = self.queryset.filter(email=self.request.GET['email'])
        if self.request.GET.get('nome'):
            self.queryset = self.queryset.filter(nome=self.request.GET['nome'])
        return self.queryset

class CursoViewSet(LoginMixin, ModelViewSet):
    serializer_class = CursoSerializer

    def __init__(self, *args, **kwargs):
        super(CursoViewSet, self).__init__(*args, **kwargs)
        self.queryset = Curso.objects.all()

class TrabalhoViewSet(LoginMixin, ModelViewSet):
    serializer_class = TrabalhoSerializer

    def __init__(self, *args, **kwargs):
        super(TrabalhoViewSet, self).__init__(*args, **kwargs)
        self.queryset = Trabalho.objects.all()

class DisciplinaViewSet(LoginMixin, ModelViewSet):
    serializer_class = DisciplinaSerializer

    def __init__(self, *args, **kwargs):
        super(DisciplinaViewSet, self).__init__(*args, **kwargs)
        self.queryset = Disciplina.objects.all()

class EntregaTrabalhoViewSet(LoginMixin, ModelViewSet):
    serializer_class = EntregaTrabalhoSerializer

    def __init__(self, *args, **kwargs):
        super(EntregaTrabalhoViewSet, self).__init__(*args, **kwargs)
        self.queryset = EntregaTrabalho.objects.all()
