from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter
from marketplaces.models import Solution, SolutionCard
from tags.models import Tag, Technology
from django.db.models import Case, QuerySet, When
from django.contrib.postgres.search import SearchVector


class SolutionsFilter(FilterSet):
    technology = ModelMultipleChoiceFilter(
        field_name="technology__name",
        to_field_name='name',
        queryset=Technology.objects.all(),
    )
    keyword = CharFilter(method='filter_search')

    def filter_search(self, queryset, name, value):
        return queryset.annotate(search=SearchVector('title', 'description', 'technology__name')).filter(
            search=value)

    class Meta:
        model = SolutionCard
        fields = ["technology", "license"]
