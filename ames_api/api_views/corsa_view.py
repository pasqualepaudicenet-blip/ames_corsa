from rest_framework import viewsets, filters
from ames_api.models import Corsa
from ames_api.serializers import CorsaSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CorsaViewSet(viewsets.ModelViewSet):
    queryset = Corsa.objects.all()
    serializer_class = CorsaSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['description', 'type']

    #filter_backends = [filters.SearchFilter]

    #search_fields = ['description', 'type'] 