from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.core.validators import MinLengthValidator


class SignupForm(UserCreationForm):
    """会員登録フォーム"""

    # エラーメッセージ定義
    username = forms.CharField(
        max_length=100,
        error_messages={
            "required": "ユーザー名は必須です。",
            "max_length": "ユーザー名は100文字以下で入力してください。",
        },
    )
    email = forms.EmailField(error_messages={"required": "メールアドレスは必須です。"})
    # パスワード
    password1 = forms.CharField(
        validators=[MinLengthValidator(8, message="パスワードは最低8文字以上必要です。")],
        error_messages={"required": "パスワードは必須です。"},
    )
    # パスワード確認用
    password2 = forms.CharField(
        validators=[MinLengthValidator(8, message="パスワード（確認用）は最低8文字以上必要です。")],
        error_messages={"required": "パスワード（確認用）は必須です。"},
    )

    class Meta:
        model = models.CustomUser
        fields = ("username", "email", "password1", "password2")
