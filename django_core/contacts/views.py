from constance import config
from rest_framework.response import Response
from rest_framework.views import APIView


class ContactsView(APIView):
    """
    Возвращает список контактов
    """

    def get(self, request, *args, **kwargs):
        resp = {}
        for key in dir(config):
            resp[key] = getattr(config, key)
        return Response(resp)
