from django.core.mail import send_mail

from django_core.celery import app


@app.task
def handle_form(data, email_subject: str, from_email: str, recipients: list) -> None:
    """ Таска в celery для отправления заявки на почту """

    email_message = '\n'.join([f'{k}: {v}' for k, v in data.items()])
    # send_mail(
    #     email_subject,
    #     email_message,
    #     from_email,
    #     recipients,
    #     fail_silently=False,
    # )
