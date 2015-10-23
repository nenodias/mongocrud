# *-* coding:utf8 *-*
import mongoengine, datetime
from mongoengine import *

class Curso(Document):
    nome = StringField(required=True, max_length=100)
    nome_abreviado = StringField(required=True, max_length=4)

class Trabalho(Document):
    titulo = StringField(required=True, max_length=100)
    data_criacao = DateTimeField(default=datetime.datetime.now)
    data_entrega = DateTimeField(required=False, null=True)
    trabalhos_entregues = ListField(GenericReferenceField(required=False, null=True))

class Disciplina(Document):
    nome = StringField(max_length=120, required=True)
    curso = ReferenceField(Curso, reverse_delete_rule=CASCADE)
    ano = IntField()
    professor = GenericReferenceField(required=False, null=True)
    trabalhos = ListField(ReferenceField(Trabalho, reverse_delete_rule=CASCADE, required=False, null=True))

class Usuario(Document):
    nome = StringField(required=True, max_length=200)
    email = StringField(required=True, max_length=200)
    senha = StringField(required=True, max_length=200)
    token = StringField(required=False, max_length=200)
    disciplinas = ListField(ReferenceField(Disciplina, reverse_delete_rule=CASCADE, required=False, null=True ))

    def is_authenticated(self):
        return self.is_authenticated

    def authenticate(self, login, password):
        if login and password:
            if not isinstance(password, bytes):
                password = str.decode(password)
            password_hash = hashlib.sha256(password)
            return self.email == login and self.senha  == password_hash.hexdigest()
        return False

class EntregaTrabalho(Document):
    aluno = ReferenceField(Usuario, reverse_delete_rule=CASCADE)
    data_entrega = DateTimeField(default=datetime.datetime.now)
    arquivo = BinaryField()

if __name__ == "__main__":
    set_trace()
    curso_sis = Curso(nome="Sistemas de Informação", nome_abreviado="SIS")
    curso_sis.save()

    v9 = Usuario(nome="Vanini", email="vanini@fgp.com.br", senha="123")
    v9.save()

    disciplina_estrutura2 = Disciplina(nome="Estrutura de Dados 2", curso=curso_sis, ano=2015, professor=v9)
    disciplina_estrutura2.save()

    aluno = Usuario(nome="Horácio Dias", email="horacio.dias92@gmail.com", senha="123",disciplinas = [ disciplina_estrutura2 ])
    aluno.save()
