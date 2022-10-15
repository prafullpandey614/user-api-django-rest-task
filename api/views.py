
from django.shortcuts import render,HttpResponse

# Create your views here.
from django.shortcuts import render
# from django.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FriendShip, User
from .serializers import UserSerializer , FriendShipSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'users-list': '/users-list/',
        'create-user' : '/create-user/',
        'add-friends' : '/add-friends/',
        'delete-friend' : '/delete-friend/',
    }
    return Response(api_urls)
@api_view(['GET'])
def usersList(request):
    users = User.objects.all()
    serilizer = UserSerializer(users,many=True)
    return Response(serilizer.data)
    
@api_view(['GET'])
def usersDetail(request,pk):
    users = User.objects.get(id=pk)
    serilizer = UserSerializer(users,many=False)
    return Response(serilizer.data)

@api_view(['POST'])
def addUser(request):
    print(request.data)    
    serilizer = UserSerializer(data=request.data)
    
    if serilizer.is_valid():
        serilizer.save()
        
        print(serilizer.data)
        
    return Response(serilizer.data)

@api_view(['POST'])
def addFriend(request):   
    
    print(request.data)
    
   
   
    serializer = FriendShipSerializer(data=request.data)
    # serilizer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)
@api_view(['GET'])
def showFriends(request,pk):
    friend_list = FriendShip.objects.filter(user_one=pk)
    for friend in friend_list:
        
        print(friend_list)
    # print(friend_list.to_user_id)
    serializer  = FriendShipSerializer(friend_list,data = friend_list , many=True)
    if serializer.is_valid():
        serializer.save()
        # return Response(serializer.data)
    return Response(serializer.data)
    # return HttpResponse("serializer.data")

def deleteFriends(request,pk,pk1):
    friend_ship =  FriendShip.objects.get(user_one=pk , user_two=pk1)
    friend_ship.delete()
    return HttpResponse("Deleted SuccesFully")

    