from django.contrib import admin
from the_watering_hole.models import User, Categories, Bar, Review, Comment, News, Photos
# Import the UserProfile model individually.
from the_watering_hole.models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Categories)
admin.site.register(Bar)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(News)
admin.site.register(Photos)