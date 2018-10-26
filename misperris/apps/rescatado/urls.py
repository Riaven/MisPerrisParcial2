from django.conf.urls import url, include
from apps.rescatado.views import index, rescatado_view, rescatado_list, rescatado_edit, rescatado_delete, somos, servicios

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', rescatado_view, name='rescatado_crear'),
    url(r'^listar$', rescatado_list, name='rescatado_listar'),
    url(r'^editar/(?P<id_rescatado>\d+)/$', rescatado_edit, name='rescatado_editar'),
    url(r'^eliminar/(?P<id_rescatado>\d+)/$', rescatado_delete, name='rescatado_eliminar'),
    url(r'^somos$', somos, name='somos'),
    url(r'^servicios$', servicios, name='servicios'),
]