from django.db import models
from django.conf import settings

# Create your models here.

class Tweet(models.Model):
    content = models.TextField(max_length=512)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
