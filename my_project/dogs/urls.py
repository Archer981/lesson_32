from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from dogs.views import DogListView


urlpatterns_dogs = [
    path("api/dogs/", DogListView.as_view()),
    path('api/dogs/docs/', SpectacularAPIView.as_view(), name='schema'),
    path('dogs/api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'))
]
