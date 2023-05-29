import django_filters
from django.db.models import Case, F, Q, QuerySet, Value, When
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import News
from .serializers import NewsDetailSerializer, NewsListSerializer


class NewsFilter(django_filters.FilterSet):
    section = django_filters.NumberFilter(method="filter_and_order_by_section")
    q = django_filters.CharFilter(method="filter_by_keyword")

    def filter_and_order_by_section(
        self, queryset: QuerySet, name: str, value: int
    ) -> QuerySet:
        queryset = queryset.filter(placements__section__pk=value)
        queryset = queryset.annotate(order=F("placements__order"))
        queryset = queryset.order_by("order")
        return queryset

    def filter_by_keyword(self, queryset: QuerySet, name: str, value: str) -> QuerySet:
        queryset = (
            queryset.filter(
                Q(title__icontains=value) | Q(short_description__icontains=value)
            ).annotate(
                priority=Case(
                    When(title__istartswith=value, then=Value(0)),
                    When(title__icontains=value, then=Value(1)),
                    When(short_description__icontains=value, then=Value(2)),
                ),
                default=Value(3),
            )
        ).order_by("priority")
        return queryset

    class Meta:
        model = News
        fields = ["tags", "news_type", "persons", "units"]


class NewsViewSet(ReadOnlyModelViewSet):
    queryset = News.objects.none()
    filterset_class = NewsFilter
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "retrieve":
            return NewsDetailSerializer
        else:
            return NewsListSerializer

    def get_queryset(self):
        if self.action == "retrieve":
            return News.objects.filter(is_draft=False, is_deleted=False)
        else:
            return News.objects.filter(
                is_draft=False, is_deleted=False, show_in_feed=True
            )

    def filter_queryset(self, queryset: QuerySet) -> QuerySet:
        queryset = super().filter_queryset(queryset)
        return queryset.prefetch_related("tags")
