from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Neighbourhood, Business, Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']

class AddHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['user_profile', 'profile']

class AddBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['business_owner', 'business_hood']

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['poster', 'post_hood']
