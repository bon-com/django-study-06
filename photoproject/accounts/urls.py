from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


# アプリ名の登録
app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", views.SignupView.as_view(), name="signup"),
]
