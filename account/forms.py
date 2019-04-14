from django import forms
from captcha.fields import CaptchaField
import datetime

class Register_Form(forms.Form):
    captcha = CaptchaField(required=True,error_messages={'invalid':'验证码错误'})