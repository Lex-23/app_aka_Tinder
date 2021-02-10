from django.contrib import admin
from django.urls import path, include
from users.views import RegisterUserView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('register/', RegisterUserView.as_view(), name='register'),
    path(r'^', include('django_private_chat.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
