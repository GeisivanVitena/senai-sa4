from django.urls import path
from page_app.views import index, contato, servicos

urlpatterns = [
    # Cadastrar URLs aqui
    path('', index),

    path('contato/', contato),

    path('services/', servicos)
]