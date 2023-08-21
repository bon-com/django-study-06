from django.urls import path
from . import views


# アプリ名の登録
app_name = "photo"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index")
]
