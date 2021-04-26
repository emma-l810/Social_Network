from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post, Comment
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    """
    first view (home page) - questions: need to get the post to actually show up
    """
    # checks if any form data has been submitted
    if request.POST:
        # checks if the form submitted is the login form by checking for username input
        if 'inputUsername' in request.POST.keys():
            # attempt authentication of login info
            user = authenticate(username=request.POST['inputUsername'], password=request.POST['inputPassword'])
            if user is not None:
                # if the user exists, then log in the user
                login(request, user)

    if request.user.is_authenticated:
        loggedIn = True
    else:
        loggedIn = False

    allposts = Post.objects.order_by('-pub_date')
    allcomments = Comment.objects.order_by('-pub_date')
    context = {
        'allposts': allposts,
        'allcomments': allcomments,
        'loggedIn': loggedIn,
        'user': request.user
        }

    print(context)
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
