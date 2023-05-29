from django.urls import path
from rest_framework.routers import DefaultRouter

from marketplaces.views import FormAPIView, NotificationAPIView
from marketplaces.viewsets import SolutionCardViewSet, SolutionsViewSet, SolutionsBySlugViewSet
from marketplaces.views import page_header

router = DefaultRouter()
router.register("solutions", SolutionCardViewSet, basename="solutions")
router.register("solution_page", SolutionsViewSet, basename="solution_pages")
router.register("solution_page_by_slug", SolutionsBySlugViewSet, basename="solution_page_by_slug")
urlpatterns = [
    path("forms/<slug:title>/", FormAPIView.as_view()),
    path("send_form/", NotificationAPIView.as_view()),
    path("page_header", page_header),
] + router.urls
