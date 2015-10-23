from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from .authentication import MyAuthentication, MyPermission

class DefaultMixin(object):
    '''Configurações default para autenticação, permissões, filtragem e paginação da view '''
    def __init__(self, *args, **kwargs):
        self.authentication_classes = [
            MyAuthentication,
        ]
        self.permission_classes = (
            MyPermission,
        )
        self.paginated_by = 25
        self.paginated_by_param = 'page_size'
        self.max_paginate_by = 100

    def perform_create(self, serializer):
        method = 'POST'
        obj = serializer.save()

    def perform_update(self, serializer):
        obj = serializer.save()

    def perform_destroy(self, obj):
        pass

class UsuarioViewSet(DefaultMixin, ModelViewSet):
    authentication_classes = MyAuthentication
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
