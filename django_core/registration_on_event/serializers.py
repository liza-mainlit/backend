from rest_framework import serializers
from .models import RegistrationForm


class RegistrationFormSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = RegistrationForm
