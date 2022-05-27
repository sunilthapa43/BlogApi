from django.contrib.auth import get_user_model #new
from django.shortcuts import render
from rest_framework import viewsets  #viewsets
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset =  Post.objects.all()
    serializer_class = PostSerializer
    

class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class =  PostSerializer
    permission_classes =  (IsAuthorOrReadOnly,) #isauthororreadonly allows only the owner to change the data 



#we can set view level permissions with 
#permission_classes = (permissions.IsAuthenticated, IsAdmin etc)

#so literally giving permissions means authorization while as authentication is a lil different like user can register, login and logout



class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =  UserSerializer
    queryset = get_user_model().objects.all()




#routers and viewsets
#now all those code can be reduced to: 

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadOnly, )


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset =  get_user_model().objects.all()