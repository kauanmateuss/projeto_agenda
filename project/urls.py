from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contact.urls'))
]

# Configurando URLs para arquivos estáticos e de mídia
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)