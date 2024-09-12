from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User,Post,Todo,Album,Photo,Comment
from .serializers import UserSerializer, PostSerializer, TodoSerializer, AlbumSerializer, PhotoSerializer, CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    #Örnek ModelViewSet action -> user/1/posts : id'ye göre kullanıcının postlarını getirir
    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        user = self.get_object()
        posts = Post.objects.filter(userId=user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    # Update işlemi için örnek action -> todos/1/set_complete : id'ye göre to-do'nun completed değerini değiştirir
    @action(detail=True, methods=['post'])
    def set_complete(self, request, pk=None):
        todo = self.get_object()
        todo.completed = request.data.get('completed')
        todo.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Create add update delete

