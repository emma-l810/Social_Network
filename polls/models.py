from django.db import models
from django.contrib.auth.models import User
from time import localtime, strftime
from django.utils.timezone import now

# Create your models here.
class Profile(models.Model):
    """
    Model: a model for the user's profile
    -include opportunity for the user to add a profile picture
    """
    # OneToOne relationship with built-in User model (doesn't return a QuerySet)
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    bio = models.TextField(default="", blank=True)

    # use of OneToOne restricts it so that there can only be a single User can only have
    # one profile, essentially (no repeats) -- it also makes it so that I can call user.bio
    # instead of user.objects.filter(bio = bio)

class Post(models.Model):
    """
    Model: a model for the post
    -add an attribute for numLikes (add heart picture - animation?)
    """
    # links to the built-in User model
    user = models.ForeignKey(User, on_delete = models.CASCADE) # delete a user, delete their posts
    text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(default = now)

    # def __str__(self):
    #     return self.post_text

class Comment(models.Model):
    """
    Model: a model for commenting on a post
    -add a like attribute and allow for commenting for comments
    """
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True, blank = True)
    text = models.CharField(max_length = 200, default="")
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default = now)

    # in case there are comments under root comments; null = True for root comments
    commentingOn = models.ForeignKey("Comment", on_delete = models.CASCADE, null = True, blank = True)

    # def __str__(self):
    #     return self.comment_text

    # this.post = Post.objects.get(pk=postID)
    # comments.objects.filter(post=thisPost) # instance of the object
