__author__ = 'Craig'

from django import forms
from the_watering_hole.models import UserProfile, Bar, Photo, Category
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
        fields = ('image',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('food', 'big_screen', 'beer_garden', 'real_ale', 'whisky_collection', 'children_welcome',
                  'pets_welcome', 'dartboard', 'pool_tables', 'games_machines', 'historic', 'wi_fi', 'function_room',)
