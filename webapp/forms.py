from django import forms
from  webapp import  models
from django.contrib.auth.models import User

class Signup(forms.Form):
    username = forms.CharField(
        required=True,min_length=2,error_messages={'required':'用户名不能为空','min_length':'用户名至少两位'}
    )
    password =forms.CharField(
        required=True,min_length=6,error_messages={'required':'密码不能为空','min_length':'密码至少六位'}
    )
    email = forms.EmailField(
        required=True,min_length=6,error_messages={'required':'邮箱不能为空','min_length':'密码至少六位'}
    )
    yzm = forms.CharField(
        required=True,min_length=4,error_messages={'required':'验证码不能为空','min_length':'验证码至少六位'}
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if (User.objects.get(email = email)):
            raise forms.ValidationError('此邮箱已被注册')
        return email

    def clean_yzm(self):
        yzm = self.cleaned_data.get('yzm')
        if (yzm != "4569"):
            raise  forms.ValidationError('验证码失效')
        return  yzm