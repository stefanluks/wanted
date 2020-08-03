from django.contrib import admin
from django.urls import path
from .views import inicial, Cartaz, Sobre, pesquisar, escrever, publicar, topusu, cadastrar,gerencia, addPontos

urlpatterns = [
    path('', inicial,name='inicial'),
    path('cadastrar',cadastrar,name="cadastrar"),
    path('wanted/<int:id>', Cartaz,name='wanted'),
    path('sobre', Sobre,name='sobre'),
    path('pesquisar',pesquisar,name='pesquisar'),
    path('escrever/<int:id>',escrever,name='escrever'),
    path('publicar/<int:id>',publicar,name='publicar'),
    path('topusuarios',topusu,name='topusuario'),
    path('gerencia',gerencia,name='gerencia'),
    path('addPontos/<int:id>',addPontos,name='addPontos'),
]
