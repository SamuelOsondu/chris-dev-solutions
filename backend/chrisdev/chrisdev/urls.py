from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.jwt')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)