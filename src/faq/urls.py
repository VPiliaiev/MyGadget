from django.urls import path

from faq.views import FAQView

urlpatterns = [
    path("", FAQView.as_view(), name="faq"),
]
