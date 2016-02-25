import logging
import hashlib
from .models import Usuario
from rest_framework import authentication
from rest_framework import exceptions

'''
Esquemas de Autenticação
'''
class MyBasicAuthentication(authentication.BaseAuthentication):

    def _is_permitir_annonimous():
        return True

    is_permitir_annonimous = staticmethod(_is_permitir_annonimous)

    def authenticate(self, request):
        print('Metodo Authenticate')
        retorno = None
        token = request.META.get('HTTP_AUTHORIZATION', '')
        if token:
            user = Usuario.objects.get(token=token)
            if user:
                retorno = (user, None)
        if not retorno and self.__class__.is_permitir_annonimous():
            # Quando permite usuário annonymoous
            print("Quando permite usuário annonymoous")
            return (object(), None)
        elif not retorno and not self.__class__.is_permitir_annonimous():
            # Quando não permite usuário annonymoous
            return None
        return retorno

    def authenticate_credentials(self, userid, password):
        logging.debug("'Metodo Authenticate Credentials'")
        user = Usuario.objects.get(email=login)
        if user is None or not user.is_active or user.authenticate(login, password):
            raise exceptions.AuthenticationFailed('Invalid username/password')
        else:
            user = None
        return (user, None)

    def authenticate_header(self, request):
        logging.debug("'Metodo Authenticate Header'")
        pass

class MyAuthentication(MyBasicAuthentication):
    
    def _is_permitir_annonimous():
        return False

    is_permitir_annonimous = staticmethod(_is_permitir_annonimous)

'''
Esquemas de Permissão
'''

class MyBasicPermission(object):

    def _is_permitir_annonimous():
        return True

    is_permitir_annonimous = staticmethod(_is_permitir_annonimous)

    def has_permission(self, request, view):
        return request.user and  (self.__class__.is_permitir_annonimous() or request.user.is_authenticated() )

    def has_object_permission(self, request, view, obj):
        return True

class MyPermission(MyBasicPermission):

    def _is_permitir_annonimous():
        return False

    is_permitir_annonimous = staticmethod(_is_permitir_annonimous)