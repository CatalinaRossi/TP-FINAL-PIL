from django.urls import path
from .views import UsuarioView
from .views import NotaView

urlpatterns = [
    path('usuarios/', UsuarioView.as_view(), name='usuarios_list'),
    path('usuarios/<int:id>', UsuarioView.as_view(), name='usuarios_process'),
    path('notas', NotaView.as_view(), name='notas_list'),
    path('notas/<int:id>', NotaView.as_view(), name='nota_process')
]