from rest_framework_mongoengine.viewsets import ModelViewSet
from .mixins import DefaultMixin, LoginMixin
from .serializers import *
from .models import *

class UsuarioViewSet(DefaultMixin, ModelViewSet):
    serializer_class = UsuarioSerializer
    #queryset = Usuario.objects.all()

    def get_queryset(self):
        queryset = Usuario.objects.all()
        queryset = queryset.order_by('-id')
        if self.request.GET.get('email'):
            queryset = queryset.filter(email=self.request.GET['email'])
        if self.request.GET.get('nome'):
            queryset = queryset.filter(nome=self.request.GET['nome'])
        return queryset
