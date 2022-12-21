from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('fortune/', include('fortune.urls', namespace='fortune')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('coins/', include('coins.urls', namespace='coins')),
    ]
if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT
                              )
