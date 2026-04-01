from rest_framework import viewsets
from ames_api.models import Sample
from ames_api.serializers import SampleSerializer
from django_filters.rest_framework import DjangoFilterBackend


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sampleId', 'sampleName']