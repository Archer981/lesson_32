from rest_framework import routers
from django.urls import include, path
from cats.views import CatViewSet

router = routers.SimpleRouter()
router.register('cats', CatViewSet)

urlpatterns = [
    path("", include(router.urls))
]
