from django.urls import path
from . import views

urlpatterns = [

    path(
        'role/', 
        views.criar_role, 
        name='criar_role'
    ),


    path(
        'organizacoes/',
        views.criar_organizacao,
        name='criar_organizacao'
    ),


    path(
        'utilizadores/',
        views.criar_utilizador,
        name='criar_utilizador'
    ),


    path(
        'categorias/',
        views.criar_categoria,
        name='criar_categoria'
    ),

    path(
        'tickets/',
        views.criar_ticket,
        name='criar_ticket'
    ),

    path(
        'documentos/',
        views.criar_documento,
        name='criar_documento'
    ),

    path(
        'chats/',
        views.criar_chat,
        name='criar_chat'
    ),

    path(
        'lembretes/',
        views.criar_lembrete,
        name='criar_lembrete'
    ),

    path(
        'logs/',
        views.criar_log,
        name='criar_log'
    ),

    path(
        'roles/',
        views.listar_roles_view,
        name='listar_roles'
    ),

    path(
        'eliminar-role/<int:id>/',
        views.eliminar_role_view,
        name='eliminar_role'
    ),

    path(
        'editar-role/<int:id>/',
        views.editar_role_view,
        name='editar_role'
    ),

    path(
        'tickets-lista/',
        views.listar_tickets_view,
        name='listar_tickets'
    ),

    path(
        'eliminar-ticket/<int:id>/',
        views.eliminar_ticket_view,
        name='eliminar_ticket'
    ),

    path(
        'editar-ticket/<int:id>/',
        views.editar_ticket_view,
        name='editar_ticket'
    ),

    path('', views.home, name='home'),

    path(
        'utilizadores-lista/',
        views.listar_utilizadores_view,
        name='listar_utilizadores'
    ),

    path(
        'eliminar-utilizador/<int:id>/',
        views.eliminar_utilizador_view,
        name='eliminar_utilizador'
    ),

    path(
        'editar-utilizador/<int:id>/',
        views.editar_utilizador_view,
        name='editar_utilizador'
    ),

    path(
        'organizacoes-lista/',
        views.listar_organizacoes_view,
        name='listar_organizacoes'
    ),

    path(
        'eliminar-organizacao/<int:id>/',
        views.eliminar_organizacao_view,
        name='eliminar_organizacao'
    ),

    path(
        'editar-organizacao/<int:id>/',
        views.editar_organizacao_view,
        name='editar_organizacao'
    ),

    path(
        'categorias-lista/',
        views.listar_categorias_view,
        name='listar_categorias'
    ),

    path(
        'eliminar-categoria/<int:id>/',
        views.eliminar_categoria_view,
        name='eliminar_categoria'
    ),

    path(
        'editar-categoria/<int:id>/',
        views.editar_categoria_view,
        name='editar_categoria'
    ),

    path(
        'documentos-lista/',
        views.listar_documentos_view,
        name='listar_documentos'
    ),

    path(
        'eliminar-documento/<int:id>/',
        views.eliminar_documento_view,
        name='eliminar_documento'
    ),

    path(
        'editar-documento/<int:id>/',
        views.editar_documento_view,
        name='editar_documento'
    ),

    path(
        'chats-lista/',
        views.listar_chats_view,
        name='listar_chats'
    ),

    path(
        'eliminar-chat/<int:id>/',
        views.eliminar_chat_view,
        name='eliminar_chat'
    ),

    path(
        'editar-chat/<int:id>/',
        views.editar_chat_view,
        name='editar_chat'
    ),

    path(
        'lembretes-lista/',
        views.listar_lembretes_view,
        name='listar_lembretes'
    ),

    path(
        'eliminar-lembrete/<int:id>/',
        views.eliminar_lembrete_view,
        name='eliminar_lembrete'
    ),

    path(
        'editar-lembrete/<int:id>/',
        views.editar_lembrete_view,
        name='editar_lembrete'
    ),

    path(
        'logs-lista/',
        views.listar_logs_view,
        name='listar_logs'
    ),

    path(
        'eliminar-log/<int:id>/',
        views.eliminar_log_view,
        name='eliminar_log'
    ),

    path(
        'editar-log/<int:id>/',
        views.editar_log_view,
        name='editar_log'
    ),

]