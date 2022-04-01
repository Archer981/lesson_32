from rest_framework import generics
from dogs.models import Dog
from dogs.serializers import DogSerializer


class DogListView(generics.ListAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    # TODO добавьте описание и краткое название здесь
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
