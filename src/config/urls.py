from django.contrib import admin
from django.urls import include, path

from common.views import IndexView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("faq/", include("faq.urls")),
    path("accounts/", include("accounts.urls")),
    path("mygadget/", include("mygadget.urls")),
]
