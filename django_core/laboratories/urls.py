from rest_framework.routers import DefaultRouter

from laboratories.views import LaboratoryModelViewSet

router = DefaultRouter()
router.register("laboratories", LaboratoryModelViewSet, basename="laboratories")
urlpatterns = router.urls
