from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from models import Post
from serializers import UserSerializer,  PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()#.order_by('-date_joined')
    serializer_class = PostSerializer
