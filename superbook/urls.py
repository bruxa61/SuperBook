from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "SuperBook Admin"
admin.site.site_title = "SuperBook Painel"
admin.site.index_title = "Bem-vindo ao SuperBook"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('heroes/', include('heroes.urls')),  # rotas do app heroes
    path('posts/', include('posts.urls')),    # rotas do app posts
    path('villains/', include('villains.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)