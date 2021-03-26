from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post, Comment

# Create your views here.
def index(request):
    """
    first view (home page)
    """
    allposts = Post.object.all()
    context = {"allpost": allposts, }
    return render(request, 'polls/index.html', context)

def twit(request):
    """
    for the twitter post box -> for login=true only
    """
    context = {}
    return render(request, 'polls/twit.html', context)

def reply(request):
    """
    for the reply box -> for login=true only
    """
    context = {}
    return render(request, 'polls/reply.html', context)
