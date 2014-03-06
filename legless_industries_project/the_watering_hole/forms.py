__author__ = 'Craig'

from django import forms
from the_watering_hole.models import UserProfile, Bar
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

    #basic bar info
    name = forms.CharField(max_length=128, help_text="Please enter the bar name")
    address = forms.CharField(max_length=128, help_text="Please enter the bar's address")
    bio = forms.CharField(widget=forms.widgets.Textarea(attrs={'rows': 5, 'cols': 30}))

     # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Bar
        fields = ('name', 'address', 'bio')