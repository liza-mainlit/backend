from django import forms
from import_export.forms import ExportForm

from news.models import News


class RegistrationExportForm(ExportForm):
    news = forms.ModelChoiceField(queryset=News.objects.all(), required=False, label='Новость')

