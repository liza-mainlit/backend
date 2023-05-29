from rest_framework.generics import ListAPIView
from .models import Info
from .serializers import InfoSerializer


class InfoView(ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    pagination_class = None
