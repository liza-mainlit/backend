from import_export import resources
from import_export.fields import Field
from .models import RegistrationForm


class ResourceRegistrationForm(resources.ModelResource):
    news__title = Field(attribute='news__title', column_name='Новость')
    name = Field(attribute='name', column_name='Имя')
    second_name = Field(attribute='second_name', column_name='Фамилия')
    email = Field(attribute='email', column_name='Email')
    number = Field(attribute='number', column_name='Номер телефона')
    work_or_study_place = Field(attribute='work_or_study_place', column_name='Место работы/учебы')
    comment = Field(attribute='comment', column_name='Комментарий')

    class Meta:
        model = RegistrationForm
        fields = ('news__title', 'name', 'second_name', 'email', 'number', 'work_or_study_place', 'comment')
