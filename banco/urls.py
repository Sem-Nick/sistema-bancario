from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('clientes', views.listar_clientes, name='listar_clientes'),
    path('clientes/novo/', views.criar_clientes, name='criar_clientes'),
    path('clientes/editar/<int:id>/', views.atualizar_cliente, name='atualizar_cliente'),
    path('clientes/deletar/<int:id>/', views.deletar_cliente, name='deletar_cliente'),
    path('exportar_clientes_pdf/', views.exportar_clientes_pdf, name='exportar_clientes_pdf'),

    path('cartoes', views.listar_cartoes, name='listar_cartoes'),
    path('cartoes/novo/', views.solicitar_cartao, name='solicitar_cartao'),
    path('cartoes/limite/<int:id>/', views.solicitar_limite, name='solicitar_limite'),
    path('cartoes/cancelar/<int:id>/', views.cancelar_cartao, name='cancelar_cartao'),
    path('exportar_cartoes_pdf/', views.exportar_cartao_pdf, name='exportar_cartoes_pdf'),


    path('emprestimo', views.listar_emprestimo, name='listar_emprestimo'),
    path('emprestimo/novo/', views.solicitar_emprestimo, name='solicitar_emprestimo'),
    path('emprestimo/cancelar/<int:id>/', views.cancelar_emprestimo, name='cancelar_emprestimo'),

    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    
    # URL para fazer logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
