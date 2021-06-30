from django.contrib import admin
from django.urls import path
from apps.demo.views import (dash, index, liquid, comision, 
	entrevistas, charts,users,users_create,users_save,users_edit,users_update,users_delete, configs, login, works, rules, foro, foro_temas,foro_comentarios,)

from django.conf.urls import url

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('dash/', dash, name='dash'),
    path('rules/', rules, name='rules'),
    path('foro/', foro, name='foro'),
    path('foro_temas/', foro_temas, name='foro_temas'),
    path('foro_comentarios/', foro_comentarios, name='foro_comentarios'),
    
    # path('works/', works, name='works'),
    # path('dashboard/', index, name='index'),
    # path('liquidacion/', liquid, name='liquid'),
    # path('comision/', comision, name='comision'),
    # path('entrevistas/', entrevistas, name='entrevistas'),
    # path('charts/', charts, name='charts'),
    path('users/', users, name='users'),
    url(r'^users/users_create$', users_create, name='users_create'),
    url(r'^users/users_save$', users_save, name='users_save'),
    url(r'^users/users_edit/(?P<id>\d+)$', users_edit, name='users_edit'),
    url(r'^users/users_edit/users_update/(?P<id>\d+)$', users_update, name='users_update'),
    url(r'^users/users_delete/(?P<id>\d+)$', users_delete, name='users_delete'),
    #path('users_edit/<int:pk>/', users_edit, name='users_edit'),
    # path('configs/', configs, name='configs'),
]
