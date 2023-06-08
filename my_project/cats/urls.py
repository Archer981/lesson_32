from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from django.urls import include, path
from cats.views import CatViewSet

router = routers.SimpleRouter()
router.register('api/cats', CatViewSet)

urlpatterns_cats = [
    path("", include(router.urls)),
    path('api/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'))
]
