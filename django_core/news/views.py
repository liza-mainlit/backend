from rest_framework.generics import ListAPIView

from tags.models import Tag, NewsType, Person, Unit
from .models import NewsSection
from .serializers import NewsTagSerializer, NewsSectionSerializer, NewsTypeSerializer, NewsPersonSerializer, \
    NewsUnitSerializer


class NewsTagListView(ListAPIView):
    serializer_class = NewsTagSerializer
    queryset = Tag.objects.all()


class NewsTypeListView(ListAPIView):
    serializer_class = NewsTypeSerializer
    queryset = NewsType.objects.all()


class NewsPersonListView(ListAPIView):
    serializer_class = NewsPersonSerializer
    queryset = Person.objects.all()


class NewsUnitListView(ListAPIView):
    serializer_class = NewsUnitSerializer
    queryset = Unit.objects.all()


class NewsSectionListView(ListAPIView):
    serializer_class = NewsSectionSerializer
    queryset = NewsSection.objects.all()
