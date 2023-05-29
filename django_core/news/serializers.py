from rest_framework import serializers

from tags.models import Tag, NewsType, Person, Unit
from .models import News, NewsImage, NewsSection, Registration


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("image",)
        model = NewsImage


class NewsListSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    news_type = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    persons = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    units = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    order = serializers.IntegerField(default=1)

    class Meta:
        fields = "__all__"
        model = News


class NewsDetailSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    images = NewsImageSerializer(read_only=True, many=True)
    news_type = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    persons = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    units = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        fields = "__all__"
        model = News


class NewsSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsSection
        fields = "__all__"


class NewsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class NewsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsType
        fields = "__all__"


class NewsPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class NewsUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"
