from django.http import FileResponse, HttpResponseNotFound


def send_file(response, file_name):
    try:
        file = open(f'django_core/media/storage/{file_name}', 'rb')
        response = FileResponse(file)
        return response
    except FileNotFoundError:
        return HttpResponseNotFound(f'File {file_name} could not be found.')
