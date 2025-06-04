from django.urls import path
from . import views

app_name = 'socialNetworks'

urlpatterns = [
    path('adicionar/', views.add_socialNetwork, name='add_socialNetwork'),
    path('', views.list_socialNetworks, name='list_socialNetworks'),
    path('editar/<int:id_socialNetwork>/', views.edit_socialNetwork, name='edit_socialNetwork'),
    path('excluir/<int:id_socialNetwork>/', views.delete_socialNetwork, name='delete_socialNetwork'),
]