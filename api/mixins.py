from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from .authentication import MyAuthentication, MyPermission

class PaginateMixin(object):
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class DefaultMixin(PaginateMixin):
    '''Configurações default para autenticação, permissões, filtragem e paginação da view '''
    def __init__(self, *args, **kwargs):
        super(PaginateMixin, self).__init__(*args, **kwargs)
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

class LoginMixin(PaginateMixin):
    def __init__(self, *args, **kwargs):
        super(PaginateMixin, self).__init__(*args, **kwargs)
        self.authentication_classes = [
            MyAuthentication,
        ]
        self.permission_classes = (
            MyPermission,
        )
