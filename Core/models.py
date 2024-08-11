from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatars/', 
        null=True, blank=True
    )
    subscriptions = models.ManyToManyField('User', related_name='subs', null=True, blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    is_hidden = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tag, related_name='posts', null=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, related_name='posts')

class PostComment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='comments')
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


    