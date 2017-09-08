from django import forms
from  webapp import  models
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

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
            # 判断邮箱是否被注册
            User.objects.get(email=email)
        except ObjectDoesNotExist as e:
            return email
        raise forms.ValidationError('该邮箱已被使用')
        return email

    def clean_yzm(self):
        yzm = self.cleaned_data.get('yzm')
        if (yzm != "4569"):
            raise  forms.ValidationError('验证码失效')
        return  yzm

class Signin(forms.Form):
    login_password =forms.CharField(
        required=True,min_length=6,error_messages={'required':'密码不能为空','min_length':'密码至少六位'}
    )
    login_email = forms.CharField(validators=[email_validate,],
        required=True,error_messages={'required':'邮箱不能为空'}
    )
