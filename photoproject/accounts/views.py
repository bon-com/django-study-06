from django.views.generic import CreateView
from django.contrib.auth.models import User
from . import forms
from django.urls import reverse_lazy


class SignupView(CreateView):
    """会員登録"""

    model = User
    form_class = forms.SignupForm
    template_name = "signup.html"
    success_url = reverse_lazy("photo:index")
