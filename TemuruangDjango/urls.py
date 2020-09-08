from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v0/', include('apps.urls')),
    path('apidoc/', get_swagger_view(title='Temuruang API Documentation')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "Temuruang Admin"
admin.site.site_title = "Temuruang Admin Portal"
admin.site.index_title = "Welcome to Temuruang Admin Portal"
