from rest_framework import serializers
from .core_serializers import DocumentSerializer
from .models import Usuario, Curso, Trabalho, Disciplina, EntregaTrabalho

class UsuarioSerializer(DocumentSerializer):
    
    perfil_display = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'email', 'senha', 'disciplinas', 'perfil_display', 'perfil')
        extra_kwargs = {
                'senha': {'write_only': True},
                'perfil': {'write_only': True},
                'id' : {'read_only': True}
        }

    def get_perfil_display(self, obj):
        valor = [ perfil for perfil in Usuario.PERFILS if perfil[0] == obj.perfil ]
        return valor[0][1]

    def create(self, validated_data):
        usuario = Usuario.objects.create(**validated_data)
        usuario._criptografar_senha()
        usuario.save()
        return usuario

    def validate_perfil(self, value):
        request = self.context['request']
        valor = [ perfil for perfil in Usuario.PERFILS if perfil[1] == value ]
        '''
        Só permite o cadastro de Professores e Administradores se for admin
        Caso contrário irá salvar com perfil Aluno
        '''
        if len(valor) and hasattr(request.user,'perfil') and request.user.perfil == Usuario.ADMINISTRADOR:
            return valor[0][0]
        return None

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
