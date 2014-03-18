__author__ = 'Craig'

from django import forms
from the_watering_hole.models import UserProfile, Bar, Photo, Category, Review, Event
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(help_text="Please enter your website.", required=False)
    picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


class BarForm(forms.ModelForm):
    class Meta:
        #Provide an association between the ModelForm and a model
        model = Bar
        fields = ('name', 'address', 'bio',)


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class ReviewForm(forms.ModelForm):
    CHOICES = [(1, '1'),
               (2, '2'),
               (3, '3'),
               (4, '4'),
               (5, '5')]
    booze = forms.ChoiceField(choices=CHOICES, label="How did you find the refreshments?",
                              widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),)

    beats = forms.ChoiceField(choices=CHOICES, label="What about the music?",
                              widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),)

    barstaff = forms.ChoiceField(choices=CHOICES, label="And the Bar Staff?",
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),)

    bucks = forms.ChoiceField(choices=CHOICES, label="Did you get your money's worth?",
                              widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),)

    text_review = forms.CharField(widget=forms.Textarea, label="Add a comment to your review!")
    class Meta:
        model = Review
        fields = ('booze', 'beats', 'barstaff', 'bucks', 'text_review')


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


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('news', 'events')
