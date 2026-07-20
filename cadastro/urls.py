from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro_membro, name='cadastro_membro'),
    path('sucesso/', views.sucesso, name='sucesso'),
]