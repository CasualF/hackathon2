from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title='Messanger API',
        default_version='v1',
        description='Chatting app',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger-ui'),
    path('account/', include('account.urls')),
    path('chat/', include('chat.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
