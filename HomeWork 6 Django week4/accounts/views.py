from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = "registration/login.html"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))