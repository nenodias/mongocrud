from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from api.models import Usuario

class LogonView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('/login')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario = Usuario.objects.get(email=str.encode(email))
        return usuario
