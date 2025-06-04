from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'modeloapp2'

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)