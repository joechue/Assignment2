from django.shortcuts import render
from django.template import Context, Template, loader
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from my_social_network.models import UserLink

def allusers (request):
  userlist = User.objects.all()#Locates all the users.
  temp = loader.get_template("my_social_network/allusers.html")
  info = Context({"users":userlist,})
  return HttpResponse(temp.render(info))#Displays all the users using the allusers.html template.

def followingusers (request,name):
  user = User.objects.get(username=name)
  links = UserLink.objects.filter(from_user=user)#Gets the user with the correct name and retrieves all userlinks of the user following.
  followedusers = []
  for link in links:
    followedusers.append(link.to_user)#Adds all followed users to a list.
  temp = loader.get_template("my_social_network/following.html")
  userinfo = Context({"followedusers":followedusers,"username":name,})
  return HttpResponse(temp.render(userinfo))#Displays info using the following.html.

def beingfollowed (request,name):
  user = User.objects.get(username=name)
  links = UserLink.objects.filter(to_user=user)
  followers = []
  for link in links:
    followers.append(link.from_user)
  temp = loader.get_template("my_social_network/followers.html")
  userinfo = Context({"followers":followers,"username":name,})
  return HttpResponse(temp.render(userinfo))#Nearly identical to previous function. Swapped to_user and from_user.
# Create your views here.