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
        if self.request.GET.get('limit') and self.request.GET.get('offset'):
            limit = int(self.request.GET.get('limit'))
            offset = int(self.request.GET.get('offset'))
            limit += offset
            return queryset[offset:limit]
        if self.request.GET.get('limit'):
            limit = int(self.request.GET.get('limit'))
            return queryset[:limit]
        if self.request.GET.get('offset'):
            offset = int(self.request.GET.get('offset'))
            return queryset[offset:]
        return queryset
