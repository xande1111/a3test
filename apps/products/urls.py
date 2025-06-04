from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('adicionar/', views.add_product, name='add_product'),
    path('', views.list_products, name='list_products'),
    path('editar/<int:id_product>/', views.edit_product, name='edit_product'),
    path('excluir/<int:id_product>/', views.delete_product, name='delete_product'),
]