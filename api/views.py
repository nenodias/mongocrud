import django_filters
from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework import filters
from .mixins import DefaultMixin, LoginMixin
from .serializers import *
from .models import *

class UsuarioViewSet(DefaultMixin, ModelViewSet):
    serializer_class = UsuarioSerializer
    #queryset = Usuario.objects.all()

    def get_queryset(self):
        queryset = Usuario.objects.all()
        if self.request.GET.get('email'):
            queryset = queryset.filter(email=self.request.GET['email'])
        if self.request.GET.get('nome'):
            queryset = queryset.filter(nome=self.request.GET['nome'])
        return queryset
