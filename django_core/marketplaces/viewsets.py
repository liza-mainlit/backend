from django.db.models import QuerySet
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin

from marketplaces.filters import SolutionsFilter
from marketplaces.models import Solution, SolutionCard
from marketplaces.serializers import SolutionsSerializer, SolutionCardSerializer


class SolutionCardViewSet(ReadOnlyModelViewSet):
    queryset = SolutionCard.objects.filter(is_hidden=False)
    filterset_class = SolutionsFilter
    serializer_class = SolutionCardSerializer

    def filter_queryset(self, queryset: QuerySet) -> QuerySet:
        queryset = super().filter_queryset(queryset)
        return queryset


class SolutionsViewSet(ReadOnlyModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionsSerializer


class SolutionsBySlugViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionsSerializer
    lookup_field = "slug"
