from django.conf.urls import url, include
from apps.rescatado.views import index, rescatado_view, rescatado_list

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', rescatado_view, name='rescatado_crear'),
    url(r'^listar$', rescatado_list, name='rescatado_listar'),
]