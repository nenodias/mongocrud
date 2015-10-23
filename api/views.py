from rest_framework_mongoengine.viewsets import ModelViewSet
from .mixins import DefaultMixin, LoginMixin
from .serializers import *
from .models import *

class UsuarioViewSet(DefaultMixin, ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
