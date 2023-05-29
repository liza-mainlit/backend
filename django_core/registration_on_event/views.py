from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import RegistrationFormSerializer
from .models import RegistrationForm
from news.models import Registration
from news.serializers import RegistrationSerializer
from django.shortcuts import get_object_or_404


class RegistrationFormAPIView(CreateAPIView):
    serializer_class = RegistrationFormSerializer
    queryset = RegistrationForm.objects.all()


class RegistrationAPIView(RetrieveAPIView):
    serializer_class = RegistrationSerializer
    queryset = Registration.objects.all()

    def get_object(self):
        lookup_field = self.kwargs["id"]
        return get_object_or_404(Registration, news__pk=lookup_field)
