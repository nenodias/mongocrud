from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Usuario

class UsuarioSerializer(DocumentSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'email', 'senha', 'disciplinas')
