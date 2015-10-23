# *-* coding:utf-8 *-*
from rest_framework.routers import DefaultRouter
from rest_framework_mongoengine import routers
from . import views

router = DefaultRouter(trailing_slash=False)
#router = routers.MongoSimpleRouter()
router.register(r'usuarios', views.UsuarioViewSet, base_name="djantex")
