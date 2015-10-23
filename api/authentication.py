import hashlib
from .models import Usuario
from rest_framework import authentication
from rest_framework import exceptions

class MyAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        print('Metodo Authenticate')
        token = request.META.get('HTTP_AUTHORIZATION', '')
        if not token:
            return None
        user = Usuario.objects.get(token=token)
        if not user:
            raise exceptions.AuthenticationFailed('No such user')
        return (user, None)

    def authenticate_credentials(self, userid, password):
        print('Metodo Authenticate Credentials')
        user = Usuario.objects.get(email=login)
        if user is None or not user.is_active or user.authenticate(login, password):
            raise exceptions.AuthenticationFailed('Invalid username/password')
        else:
            user = None
        return (user, None)

    def authenticate_header(self, request):
        print('Metodo Authenticate Header')
        pass

class MyPermission(object):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        return True
