from rest_framework import serializers

from marketplaces.models import FormTemplate, Field, Notification, Solution, SolutionCard, DataSourceBlock, DataSource, \
    SolutionResourceButton


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "id",
            "title",
        ]
        model = Field


class FormTemplateSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)

    class Meta:
        fields = [
            "id",
            "title",
            "fields",
        ]
        model = FormTemplate


class NotificationSerializer(serializers.ModelSerializer):
    form_id = serializers.IntegerField(required=True)
    message = serializers.DictField(required=True)

    def validate(self, data):
        errors = {}
        message, form_id = data.get("message"), data.get("form_id")
        form: FormTemplate = FormTemplate.objects.filter(pk=form_id).first()
        if not form:
            errors["form_id"] = 'Form id must exist'
        elif {field.title for field in form.fields.all()} != message.keys():
            errors["message"] = f'Keys are not correct for form with id={form_id}'
        if errors:
            raise serializers.ValidationError(errors)
        return data

    class Meta:
        fields = [
            "id",
            "message",
            "form_id",
        ]
        model = Notification


class SolutionResourceButtonSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id', 'solution')
        model = SolutionResourceButton


class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = DataSource


class DataSourceBlockSerializer(serializers.ModelSerializer):
    data_sources = DataSourceSerializer(many=True)

    class Meta:
        depth = 1
        exclude = ('id', 'solution')
        model = DataSourceBlock


class SolutionsSerializer(serializers.ModelSerializer):
    technology = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    unit = serializers.SlugRelatedField(slug_field="name", read_only=True)
    url = serializers.ReadOnlyField()
    resource_button = SolutionResourceButtonSerializer(many=True)
    data_source_block = DataSourceBlockSerializer(many=True)

    class Meta:
        exclude = ('slug', "published_at")
        model = Solution
        depth = 2


class SolutionCardSerializer(serializers.ModelSerializer):
    technology = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    url = serializers.ReadOnlyField()

    class Meta:
        exclude = ("is_hidden",)
        model = SolutionCard
