from django import forms
from  webapp import  models
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def email_validate(value):
    email_re = re.compile(r'^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$')
    if not email_re.match(value):
        raise ValidationError('邮箱格式错误')

class Signup(forms.Form):
    username = forms.CharField(
        required=True,min_length=2,error_messages={'required':'用户名不能为空','min_length':'用户名至少两位'}
    )
    password =forms.CharField(
        required=True,min_length=6,error_messages={'required':'密码不能为空','min_length':'密码至少六位'}
    )
    email = forms.CharField(validators=[email_validate,],
        required=True,error_messages={'required':'邮箱不能为空'}
    )
    yzm = forms.CharField(
        required=True,min_length=4,error_messages={'required':'验证码不能为空','min_length':'验证码至少六位'}
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            if (User.objects.get(email=email)):
                raise forms.ValidationError('此邮箱已被注册')
        except Exception as e:
            print(e)
        return email

    def clean_yzm(self):
        yzm = self.cleaned_data.get('yzm')
        if (yzm != "4569"):
            raise  forms.ValidationError('验证码失效')
        return  yzm
    def clean(self):
        try:
            email = self.cleaned_data.get('email')
        except Exception as e:
            raise forms.ValidationError("邮箱格式不符合要求")
        return  self.cleaned_data