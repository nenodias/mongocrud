import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from api.models import Usuario

class LogonView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('/login')

    def post(self, request, *args, **kwargs):
        retorno = {}
        status_retornado = 500
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if not email and not senha:
            json_body=json.loads(request.body.decode())
            email = json_body['email']
            senha = json_body['senha']
        usuario = Usuario.objects.filter(email=email)
        if usuario.count() == 1:
            usuario = usuario.get(0)
            if usuario.authenticate(email, senha):
                status_retornado = 200
                retorno['id'] = str(usuario.id)
                retorno['nome'] = usuario.nome
                retorno['email'] = usuario.email
                retorno['token'] = usuario.token
        return HttpResponse(json.dumps(retorno) ,content_type="application/json", status=status_retornado)
