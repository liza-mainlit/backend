from rest_framework.viewsets import ReadOnlyModelViewSet

from laboratories.serializers import LaboratorySerializer
from laboratories.models import Laboratory


class LaboratoryModelViewSet(ReadOnlyModelViewSet):
    queryset = Laboratory.objects.all()
    serializer_class = LaboratorySerializer
    lookup_field = "slug"
