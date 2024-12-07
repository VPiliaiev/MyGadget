from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from accounts.utils.token_geneators import TokenGenerator


def send_registration_email(user_instance, request):
    token = TokenGenerator().make_token(user_instance)
    uid = urlsafe_base64_encode(force_bytes(user_instance.pk))

    message = render_to_string(
        "emails/email_registration.html",
        {
            "user": user_instance,
            "domain": get_current_site(request),
            "token": token,
            "uid": uid,
        },
    )

    email = EmailMessage(
        subject=settings.REGISTRATION_EMAIL_SUBJECT,
        body=message,
        to=[user_instance.email],
        cc=[settings.EMAIL_HOST_USER],
    )
    email.content_subtype = "html"
    email.send(fail_silently=settings.EMAIL_FAIL_SILENTLY)
