# *-* coding:utf-8 *-*
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from rest_framework.authtoken.views import obtain_auth_token

from api.urls import router

urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls) ),
    url(r'^$',TemplateView.as_view(template_name='api/index.html'))
]
