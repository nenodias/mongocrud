from django.http import JsonResponse
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

    def list(request, *args, **kwargs):
        requisicao = args[0]
        if requisicao.GET and  'count' in requisicao.GET.keys():
            count = request.queryset.count()
            return JsonResponse({ "count": count })
        return super().list(request, args, kwargs)

    def get_queryset(self):
        self.queryset = self.queryset.order_by('-id')
        if self.request.GET.get('limit') and self.request.GET.get('offset'):
            limit = int(self.request.GET.get('limit'))
            offset = int(self.request.GET.get('offset'))
            limit += offset
            return self.queryset[offset:limit]
        if self.request.GET.get('limit'):
            limit = int(self.request.GET.get('limit'))
            return self.queryset[:limit]
        if self.request.GET.get('offset'):
            offset = int(self.request.GET.get('offset'))
            return self.queryset[offset:]
        return self.queryset
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
