from django.contrib import admin

from .models import NewsType, Person, Tag, Unit, Technology

admin.site.register(NewsType)
admin.site.register(Person)
admin.site.register(Tag)
admin.site.register(Unit)
admin.site.register(Technology)
