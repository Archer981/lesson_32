from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.viewsets import ModelViewSet

from petstore.models import Application
from petstore.serializers import ApplicationSerializer


# TODO добавьте необходимый код здесь
@extend_schema_view(partial_update=extend_schema(description='Update application info', summary='Application update'))
class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
