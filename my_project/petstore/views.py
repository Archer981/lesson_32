from rest_framework.viewsets import ModelViewSet

from petstore.models import Application
from petstore.serializers import ApplicationSerializer


# TODO добавьте необходимый код здесь
class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
