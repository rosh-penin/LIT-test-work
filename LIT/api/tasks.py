from django.conf import settings
from django.core.mail import send_mail

from LIT.celery import celery_app


@celery_app.task
def send_email_otp(email, code):
    """Task for the celery. Sends email to user."""
    message = f'''Your activation code is {code}.
    The code will expire in 10 minutes.'''
    send_mail(
        'Activation Code',
        message,
        settings.EMAIL_HOST_USER,
        [email]
    )
