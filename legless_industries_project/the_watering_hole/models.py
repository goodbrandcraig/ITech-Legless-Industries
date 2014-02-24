from django.db import models


# Create your models here.
class User(models.Model):

    #basic user account info
    uID = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=10, unique=False)
    birthdate = models.DateField(unique=False)
    email = models.EmailField(max_length=75)
    date_created = models.DateTimeField()

    def __unicode__(self):
        return self.uID


class Bar(models.Model):
    #link to owner's account
    owner = models.ForeignKey(User)

    #basic bar info
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=256, unique=True)
    bio = models.TextField()

    def __unicode__(self):
        return self.name


class Review(models.Model):
    #link to user that posted review
    poster = models.ForeignKey(User)

    #ratings
    booze = models.IntegerField(default=0)
    beats = models.IntegerField(default=0)
    bevy = models.IntegerField(default=0)
    bucks = models.IntegerField(default=0)

    #overall rating is average of all other ratings
    overall = models.IntegerField(default= 0)

    #review details
    text_review = models.TextField()
    date_posted = models.DateTimeField()
    likes = models.IntegerField(default=0)
    favourites = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text_review


class Comment(models.Model):
    poster = models.ForeignKey(User)
    text_comment = models.TextField()
    date_posted = models.DateTimeField()
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text_comment


class Categories(models.Model):
    #link to bar
    bar = models.ForeignKey(Bar)

    #true or false categories (can be added to if necessary
    food = models.BooleanField(default=False)
    big_screen = models.BooleanField(default=False)
    beer_garden = models.BooleanField(default=False)
    real_ale = models.BooleanField(default=False)
    whisky_collection = models.BooleanField(default=False)
    children_welcome = models.BooleanField(default=False)
    pets_welcome = models.BooleanField(default=False)
    dartboard = models.BooleanField(default=False)
    pool_tables = models.BooleanField(default=False)
    games_machines = models.BooleanField(default=False)
    historic = models.BooleanField(default=False)
    wi_fi = models.BooleanField(default=False)
    function_room = models.BooleanField(default=False)

    def __unicode__(self):
        return self.bar


class News(models.Model):
    #link to bar
    bar = models.ForeignKey(Bar)

    events = models.TextField()
    news = models.TextField()

    def __unicode__(self):
        return self.bar


class Photos(models.Model):
    bar = models.ForeignKey(Bar)
    image = models.ImageField(upload_to = 'uploads')

    def __unicode__(self):
        return self.bar