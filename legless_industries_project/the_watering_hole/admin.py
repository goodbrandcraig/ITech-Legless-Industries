from django.contrib import admin
from the_watering_hole.models import Category, Bar, Review, Comment, Event, Photo
# Import the UserProfile model individually.
from the_watering_hole.models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Bar)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Event)
admin.site.register(Photo)