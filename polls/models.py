from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """
    Model: a model for the post
    """
    user = models.ForeignKey(User, on_delete = models.CASCADE) # delete a user, delete their posts
    text = models.CharField(max_length = 200) 

class Comment(models.Model):
    """
    Model: a model for commenting on a post
    """
