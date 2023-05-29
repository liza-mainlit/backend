from rest_framework.generics import CreateAPIView

from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
