from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Usuario

class UsuarioSerializer(DocumentSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'email', 'senha', 'disciplinas',)
        extra_kwargs = {
                'senha': {'write_only': True},
                'id' : {'read_only': True}
        }

    def create(self, validated_data):
        usuario = Usuario.objects.create(**validated_data)
        usuario._criptografar_senha()
        usuario.save()
        return usuario

    def validate_disciplinas(self, value):
        if isinstance(value, list) or isinstance(value, tuple):
            return value
        return None
'''
    def update(self, instance, validated_data):
        updated_instance = super(UsuarioSerializer, self).update(instance, validated_data)
        updated_instance.save()
        return updated_instance
        '''
