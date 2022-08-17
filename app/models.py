from email import message
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tag_set = models.ManyToManyField('Tag', blank=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()


# class Comment2(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     message = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
