# *-* coding:utf-8 *-*
from rest_framework.routers import DefaultRouter
from rest_framework_mongoengine import routers
from . import views

router = DefaultRouter(trailing_slash=True)
#router = routers.MongoSimpleRouter()
router.register(r'usuarios', views.UsuarioViewSet, base_name="djantex")
router.register(r'cursos', views.CursoViewSet, base_name="djantex")
router.register(r'trabalhos', views.TrabalhoViewSet, base_name="djantex")
router.register(r'disciplinas', views.DisciplinaViewSet, base_name="djantex")
router.register(r'entregas', views.EntregaTrabalhoViewSet, base_name="djantex")
