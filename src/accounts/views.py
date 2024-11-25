from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, DetailView, RedirectView, UpdateView

from accounts.forms import CustomerProfileForm, UserRegistrationForm
from accounts.models import Customer
from accounts.services.emails import send_registration_email
from accounts.utils.token_geneators import TokenGenerator


class UserLogin(LoginView):
    pass


class UserLogout(LogoutView):
    next_page = reverse_lazy("login")


class UserRegistration(CreateView):
    template_name = "registration/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        send_registration_email(user_instance=self.object, request=self.request)
        return super().form_valid(form)


class UserActivationView(RedirectView):
    url = reverse_lazy("index")

    def get(self, request, uuid64, token, *args, **kwargs):
        print(f"UUID: {uuid64}, Token: {token}")
        try:
            pk = force_str(urlsafe_base64_decode(uuid64))
            print(f"Decoded PK: {pk}")
            current_user = get_user_model().objects.get(pk=pk)
        except (get_user_model().DoesNotExist, ValueError, TypeError):
            return HttpResponse("Wrong data!!!")

        if current_user and TokenGenerator().check_token(current_user, token):
            current_user.is_active = True
            current_user.save()

            login(request, current_user)

            return super().get(request, *args, **kwargs)

        return HttpResponse("Wrong data!!!")


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = "profile/user_profile.html"
    context_object_name = "customer"

    def get_object(self, queryset=None):
        return self.request.user


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerProfileForm
    template_name = "profile/profile_update.html"
    success_url = reverse_lazy("user_profile")

    def get_object(self, queryset=None):
        return self.request.user
