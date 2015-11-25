from rest_framework_mongoengine.viewsets import ModelViewSet
from .mixins import DefaultMixin, LoginMixin
from .serializers import *
from .models import *

class UsuarioViewSet(DefaultMixin, ModelViewSet):
    serializer_class = UsuarioSerializer
    #queryset = Usuario.objects.all()

    def __init__(self, *args, **kwargs):
        self.queryset = Usuario.objects.all()

    def get_queryset(self):
        self.queryset = super().get_queryset()
        if self.request.GET.get('email'):
            self.queryset = self.queryset.filter(email=self.request.GET['email'])
        if self.request.GET.get('nome'):
            self.queryset = self.queryset.filter(nome=self.request.GET['nome'])
        return self.queryset
