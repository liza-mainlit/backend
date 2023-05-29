from rest_framework import serializers

from laboratories.models import (
    Laboratory,
    LaboratoryEmployee,
    SocialNetResource,
    LaboratorySolutionCards
)
from marketplaces.serializers import SolutionCardSerializer


class LaboratorySolutionCardSerializer(serializers.ModelSerializer):
    solution = SolutionCardSerializer()

    class Meta:
        model = LaboratorySolutionCards
        exclude = ("id", "laboratory")


class LaboratorySocialNetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetResource
        exclude = ("id", "laboratory")


class LaboratoryEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoryEmployee
        exclude = ("id", "laboratory")


class LaboratorySerializer(serializers.ModelSerializer):
    laboratory_url = serializers.ReadOnlyField()
    employees = LaboratoryEmployeeSerializer(many=True)
    social_nets = LaboratorySocialNetSerializer(many=True)
    solution_cards = LaboratorySolutionCardSerializer(many=True)

    class Meta:
        model = Laboratory
        exclude = ("slug",)
