"""
URL configuration for modeloapp2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('accounts.urls', namespace='accounts')),
    path('', include('core.urls', namespace='core')),
    path('categorias/', include('categories.urls', namespace='categories')),
    path('produtos/', include('products.urls', namespace='products')),
    path('redes/', include('socialNetworks.urls', namespace='socialNetworks')),
    path('clientes/', include('clients.urls', namespace='clients')),
    path('pedidos/', include('orders.urls', namespace='orders')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
