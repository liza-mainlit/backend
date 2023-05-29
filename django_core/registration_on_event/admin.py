from django.contrib import admin
from django.core.files.storage import get_storage_class

from import_export.admin import ExportMixin

from .models import RegistrationForm
from .resources import ResourceRegistrationForm
from .forms import RegistrationExportForm


@admin.register(RegistrationForm)
class RegistrationFormAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('news', 'name', 'second_name', 'email', 'number', 'work_or_study_place', 'comment')
    list_filter = ('news__title',)
    resource_classes = (ResourceRegistrationForm,)
    export_form_class = RegistrationExportForm

    def get_data_for_export(self, request, queryset, *args, **kwargs):
        export_form = kwargs.pop('export_form', None)
        queryset = queryset.filter(news=export_form.cleaned_data['news'])
        return self.choose_export_resource_class(export_form)(
            **self.get_export_resource_kwargs(request, *args, **kwargs)
        ).export(queryset, *args, **kwargs)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
