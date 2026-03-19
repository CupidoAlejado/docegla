from django.urls import path
from .views import lista_produtos, detalhe_produto

urlpatterns = [
    path('', lista_produtos, name='todos'),
    path('categoria/<int:categoria_id>/', lista_produtos, name='categoria'),
    path('produto/<int:produto_id>/', detalhe_produto, name='produto'),
]