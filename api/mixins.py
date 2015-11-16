from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from .authentication import MyAuthentication, MyPermission

class DefaultMixin():
    '''Configurações default para autenticação, permissões, filtragem e paginação da view '''
    def __init__(self, *args, **kwargs):
        self.authentication_classes = [
            BasicAuthentication,
        ]
        self.permission_classes = (
            AllowAny,
        )
'''
    #Caso precise dispara alguma operacao antes da Criação, Atualização ou Exclusão

    def perform_create(self, serializer):
        method = 'POST'
        obj = serializer.save()

    def perform_update(self, serializer):
        obj = serializer.save()

    def perform_destroy(self, obj):
        pass
'''

class LoginMixin():
    def __init__(self, *args, **kwargs):
        self.authentication_classes = [
            MyAuthentication,
        ]
        self.permission_classes = (
            MyPermission,
        )
