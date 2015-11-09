from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Usuario

class UsuarioSerializer(DocumentSerializer):
    class Meta:
        model = Usuario
        write_only = ('senha',)
        fields = ('id', 'nome', 'email', 'disciplinas',)
