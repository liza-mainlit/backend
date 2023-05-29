from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import NewsTagListView, NewsSectionListView, NewsTypeListView, NewsPersonListView, NewsUnitListView
from .viewsets import NewsViewSet

router = DefaultRouter()
router.register("", NewsViewSet, basename="news")
urlpatterns = [
    path("tags/", NewsTagListView.as_view()),
    path("news_type/", NewsTypeListView.as_view()),
    path("persons/", NewsPersonListView.as_view()),
    path("units/", NewsUnitListView.as_view()),
    path("sections/", NewsSectionListView.as_view()),
]
urlpatterns += router.urls
