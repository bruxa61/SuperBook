# superbook/superbook/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('requisitos.urls')),
    # path('aulas/', include('aulas.urls')),
    path('heroes/', include('heroes.urls')),
    path('posts/', include('posts.urls')),
    path('villains/', include('villains.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
