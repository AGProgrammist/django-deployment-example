from django import forms
from basic_app.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    portfolia = forms.URLField(required=False)
    profile_pic = forms.ImageField(required=False)
    class Meta():
        model = UserProfileInfo
        fields = ('portfolia', 'profile_pic')
