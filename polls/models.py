from django.db import models
from django.contrib.auth.models import User
from time import localtime, strftime
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    """
    Model: a model for the post
    """
    user = models.ForeignKey(User, on_delete = models.CASCADE) # delete a user, delete their posts
    text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(default = now)

    # def __str__(self):
    #     return self.post_text

class Comment(models.Model):
    """
    Model: a model for commenting on a post
    # """
    # post = models.ForeignKey(Post, on_delete = models.CASCADE)   #doesn't work
    text = models.CharField(max_length = 200, default="")
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default = now)

    # def __str__(self):
    #     return self.comment_text
