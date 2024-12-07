from django.urls import path

from accounts.views import (
    UserActivationView,
    UserLogin,
    UserLogout,
    UserProfileDetailView,
    UserProfileUpdateView,
    UserRegistration,
)

urlpatterns = [
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("registration/", UserRegistration.as_view(), name="registration"),
    path(
        "activate/<str:uuid64>/<str:token>/",
        UserActivationView.as_view(),
        name="activate_user",
    ),
    path("profile/", UserProfileDetailView.as_view(), name="user_profile"),
    path(
        "profile/update/", UserProfileUpdateView.as_view(), name="user_profile_update"
    ),
]
