from django.contrib import admin
from django.urls import path
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from comercio.views import pagina

urlpatterns = [
    path('principal/', admin.site.urls),
    path('fresco/',include('comercio.urls')),
    path('',pagina)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 