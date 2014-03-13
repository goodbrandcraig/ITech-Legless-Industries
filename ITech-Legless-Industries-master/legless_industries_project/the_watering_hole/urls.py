from django.conf.urls import patterns, url
from the_watering_hole import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^sorted_index/(?P<category>\w+)/$', views.sorted_index, name='sorted'),
                       url(r'^about', views.about, name='about'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^add_bar/$', views.add_bar, name='add_bar'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^bar_page/(?P<bar_name_url>\w+)/$', views.bar_page, name='bar'),
                       url(r'^like_review/$', views.like_review, name='like_review'),
                       url(r'^profile_page/(?P<username>\w+)/$', views.profile_page, name='profile'),
                       url(r'^review_bar/(?P<bar_name_url>\w+)/$', views.add_review, name='review'),
                       )
