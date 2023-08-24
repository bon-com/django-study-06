from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


# アプリ名の登録
app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
