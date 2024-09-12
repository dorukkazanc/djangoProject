from django.db import models


class User(models.Model):
    name= models.CharField(max_length=100)
    username= models.CharField(max_length=100)
    email= models.EmailField()
    address= models.JSONField()
    phone= models.CharField(max_length=20)
    website= models.CharField(max_length=100)
    company= models.JSONField()


class Album(models.Model):
    userId= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=100)


class Photo(models.Model):
    albumId= models.ForeignKey(Album, on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    url= models.URLField()
    thumbnailUrl= models.URLField()


class Todo(models.Model):
    userId= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    completed= models.BooleanField()


class Post(models.Model):
    userId= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    body= models.TextField()


class Comment(models.Model):
    postId= models.ForeignKey(Post, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    email= models.EmailField()
    body= models.TextField()

