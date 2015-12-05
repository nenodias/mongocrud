# *-* coding:utf8 *-*
import datetime
import hashlib
import json
import logging
from django.conf import settings

import mongoengine, datetime
from mongoengine import *

class Curso(Document):
    nome = StringField(required=True, max_length=100)
    nome_abreviado = StringField(required=True, max_length=4)

class Trabalho(Document):
    titulo = StringField(required=True, max_length=100)
    descricao = StringField(required=False, max_length=5000)
    data_criacao = DateTimeField(default=datetime.datetime.now)
    data_entrega = DateTimeField(required=False, null=True)
    anexo = BinaryField(required=False, max_bytes=52428800)
    trabalhos_entregues = ListField(GenericReferenceField(required=False, null=True))

class Disciplina(Document):
    nome = StringField(max_length=120, required=True)
    curso = ReferenceField(Curso, reverse_delete_rule=CASCADE)
    ano = IntField()
    professor = ObjectIdField(required=False, null=True)
    trabalhos = ListField(ReferenceField(Trabalho, reverse_delete_rule=CASCADE, required=False, null=True))

class Usuario(Document):
    nome = StringField(required=True, max_length=200)
    email = StringField(required=True, max_length=200)
    senha = StringField(required=True, max_length=200)
    salt = StringField(max_length=200)
    token = StringField(required=False, max_length=200)
    disciplinas = ListField(ReferenceField(Disciplina, reverse_delete_rule=CASCADE, required=False, null=True ))

    def _criptografar_senha(self):
        secret = str.encode(settings.SECRET_KEY)
        if not isinstance(self.senha, bytes):
            password = str.encode(self.senha)
        if not self.salt:
            timestamp = str.encode( str( datetime.datetime.now().timestamp() ) )
            self.salt = str( hashlib.sha256(secret+ timestamp ).hexdigest() )
        salt = str.encode(self.salt)
        password_hash = hashlib.sha256(secret+ salt + password)
        self.senha = str( password_hash.hexdigest() )

    def clean(self):
        insert = True if self.pk == None else False

        if insert:
            email = self.email
            usuario = Usuario.objects(email=email)
            if usuario:
                raise ValueError('Email já cadastrado!')
        return True

    def is_authenticated(self):
        return self.is_authenticated

    def authenticate(self, login, password):
        if login and password:
            secret = str.encode(settings.SECRET_KEY)
            if not isinstance(password, bytes):
                password = str.encode(password)
            if not self.salt:
                logging.error("Usuario com id: %s não possui salt" %(self.id) )
            salt = str.encode(self.salt)
            password_hash = hashlib.sha256(secret+ salt + password)

            resultado = self.email == login and self.senha  == password_hash.hexdigest()
            if resultado:
                timestamp = str.encode( str( datetime.datetime.now().timestamp() ) )
                token = str( hashlib.sha256(secret+ timestamp ).hexdigest() )
                self.token = token
                self.save()
            return resultado
        return False

class EntregaTrabalho(Document):
    aluno = ReferenceField(Usuario, reverse_delete_rule=CASCADE)
    data_entrega = DateTimeField(default=datetime.datetime.now)
    arquivo = BinaryField(max_bytes=52428800)
