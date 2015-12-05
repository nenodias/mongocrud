from .core_serializers import DocumentSerializer
from .models import Usuario, Curso, Trabalho, Disciplina, EntregaTrabalho

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

class CursoSerializer(DocumentSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'nome', 'nome_abreviado',)
        extra_kwargs = {
                'id' : {'read_only': True}
        }

class TrabalhoSerializer(DocumentSerializer):
    class Meta:
        model = Trabalho
        fields = ('id', 'titulo', 'descricao', 'data_criacao', 'data_entrega', 'anexo', 'trabalhos_entregues',)
        extra_kwargs = {
                'id' : {'read_only': True}
        }
class DisciplinaSerializer(DocumentSerializer):
    class Meta:
        model = Disciplina
        fields = ('id', 'nome', 'curso', 'ano', 'professor', 'trabalhos',)
        extra_kwargs = {
                'id' : {'read_only': True}
        }

class EntregaTrabalhoSerializer(DocumentSerializer):
    class Meta:
        model = EntregaTrabalho
        fields = ('id', 'aluno', 'data_entrega','arquivo',)
        extra_kwargs = {
                'id' : {'read_only': True}
        }
