from django.urls import path, include
from petstore.views import ApplicationViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register("petstore", ApplicationViewSet, basename="Application")


urlpatterns = [
    path("", include(router.urls))
]
