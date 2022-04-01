from django.urls import path
from dogs.views import DogListView


urlpatterns = [
    path("dogs/", DogListView.as_view())
]
