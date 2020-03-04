from django import forms
from .models import Post
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')

class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')


# class ListForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'body']

# class PublishForm(forms.ModelForm):
#     # title_name = forms.CharField(label='标题',max_length=70)#标题
#     # title_body = forms.CharField(widget=forms.Textarea)#文本
#     # title_time = forms.DateTimeField(label='日期')#日期
#     # title_excerpt = forms.CharField(label='摘录')
#     # title_category = forms.CharField(label='种类')#种类
#     # title_tags = forms.CharField(label='标题')#标签
#     # title_author = forms.CharField(label='楼主')#作者
#     class Meta:
#         model = Post
#         fields = ['title','body','modified_time','chuckle','uthor']