from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from petstore.views import ApplicationViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register("api/petstore", ApplicationViewSet, basename="Application")


urlpatterns = [
    path("", include(router.urls))
    path('api/petstore/docs/', SpectacularAPIView.as_view(), name='schema'),
    path('petstore/api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'))
]
