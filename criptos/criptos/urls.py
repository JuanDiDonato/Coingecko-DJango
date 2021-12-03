from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += [
    path('coins/', include('coins.urls')),
]
urlpatterns += [
    # Redirijo el inicio de mi proyecto ('/') a catalog ('/catalog)
    path('', RedirectView.as_view(url='/coins/', permanent=True)),
]
# Autentificacion de usuarios
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]