from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("cats.urls")),
    path('api/', include("dogs.urls")),
    path('api/', include("petstore.urls")),
    path('api/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
