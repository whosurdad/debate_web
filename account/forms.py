from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
import datetime
from django.contrib.auth.models import User

class 自定义注册表单(UserCreationForm):
    昵称 = forms.CharField(required=False,max_length=50)
    生日 = forms.DateField(required=False)
    验证码 = CaptchaField()

    class Meta:
        model = User
        fields = ('username','password1','password2','email','昵称','生日')

class 自定义编辑表单(UserChangeForm):
    昵称 = forms.CharField(required=False, max_length=50)
    生日 = forms.DateField(required=False)

    class Meta:
        model = User
        fields = ('username','password','email', '昵称', '生日')


class 自定义登录表单(AuthenticationForm):
    验证码 = CaptchaField()