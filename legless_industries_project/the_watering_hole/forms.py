__author__ = 'Craig'

from django import forms
from the_watering_hole.models import UserProfile, Bar, Photo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


class BarForm(forms.ModelForm):
    class Meta:
        #Provide an association between the ModelForm and a model
        model = Bar
        fields = ('name', 'address', 'bio',)


class ImageForm(forms.ModelForm):
    class Meta:
        #Provide an association between the ModelForm and a model
        model = Photo
        fields = ( 'image',)

