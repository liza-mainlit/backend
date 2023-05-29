from django.core.files.storage import DefaultStorage
from django.http.response import HttpResponseForbidden
from filebrowser.sites import FileBrowserSite
from filebrowser.actions import (
    flip_horizontal,
    flip_vertical,
    rotate_90_clockwise,
    rotate_90_counterclockwise,
    rotate_180
)


class CustomFileBrowserSite(FileBrowserSite):
    """
    Класс, переопределяющий базовое поведение родительского FileBrowserSite
    Отключает операцию создания папок
    Отключает операцию удаления файлов
    """
    def delete_confirm(self, request):
        return HttpResponseForbidden("Недостаточно прав")

    def delete(self, request):
        return HttpResponseForbidden("Недостаточно прав")

    def createdir(self, request):
        return HttpResponseForbidden("Недостаточно прав")


# СОЗДАНИЕ КАСТОМНОГО ФАЙЛОВОГО БРАУЗЕРА
storage = DefaultStorage()
filebrowser_site = CustomFileBrowserSite(name="filebrowser", storage=storage)
filebrowser_site.directory = "uploaded_files/"

filebrowser_site.add_action(flip_horizontal)
filebrowser_site.add_action(flip_vertical)
filebrowser_site.add_action(rotate_90_clockwise)
filebrowser_site.add_action(rotate_90_counterclockwise)
filebrowser_site.add_action(rotate_180)
