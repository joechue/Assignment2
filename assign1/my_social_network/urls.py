from django.conf.urls import patterns, include, url
from django.contrib import admin
from my_social_network import views

urlpatterns = patterns('',
    url(r'^$', views.allusers, name="Users"),
    url(r'(?P<name>\w+)/following', views.followingusers),
    url(r'(?P<name>\w+)/followers', views.beingfollowed),
)