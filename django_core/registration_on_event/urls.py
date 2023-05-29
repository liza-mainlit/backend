from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import RegistrationAPIView, RegistrationFormAPIView

urlpatterns = [
    path("", RegistrationFormAPIView.as_view()),
    path("<slug:id>/", RegistrationAPIView.as_view())

]
