from django.urls import path
from .views import send_file

urlpatterns = [
    path("<str:file_name>", send_file),
]
