from django.db.models import QuerySet
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from constance import config

from marketplaces.models import FormTemplate, Notification
from marketplaces.serializers import FormTemplateSerializer, NotificationSerializer


@api_view()
def page_header(request):
    return Response(config.MARKETPLACE_PAGE_HEADER)


class FormAPIView(RetrieveAPIView):
    lookup_field = "title"
    serializer_class = FormTemplateSerializer
    queryset = FormTemplate.objects.all()

    def filter_queryset(self, queryset: QuerySet) -> QuerySet:
        queryset = super().filter_queryset(queryset)
        return queryset.prefetch_related("fields")


class NotificationAPIView(CreateAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()


