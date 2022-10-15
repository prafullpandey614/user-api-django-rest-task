
from django.urls import path 
from . import views
urlpatterns = [
   
  path("",views.apiOverview),
  path("user-list/",views.usersList),
  path("user-detail/<slug:pk>",views.usersDetail),
  path("create-user/",views.addUser),
  path("add-friends/",views.addFriend),
  path("show-friend/<slug:pk>",views.showFriends),
  path("delete-friend/<slug:pk>/<slug:pk1>",views.deleteFriends),
]