from django.conf.urls import include, url
from . import views


urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^registro/nuevo/$', views.registro,name='registro'),
        url(r'^cita/(?P<pk>[0-9]+)/$', views.cita,name='cita'),
    ]
