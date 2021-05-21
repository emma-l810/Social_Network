from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post, Comment
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# new function that creates an object in the dictionary (refer back to screenshot)
    # look for root posts if there are any comments, and get those comments, and look
    # to check if each comment has any subcomments
def getPostDict(post):
    postDict = {}   # post dictionary for one post
    # adding model attributes to dictionary --> find a more efficient way to do this?...
    postDic['user'] = post.user
    postDict['text'] = post.text
    postDict['pub_date'] = post.pub_date
    postDict['comments'] = []
    # if a post has comments
    if Comments.objects.filter(post = post).exists():
        for comment in Comment.objects.order_by('-pub_date'):
            # if comment's commentingOn = null:
                # append comment to postDict['comments']
            # else:
                # loop through getPostDict(comment), and keep doing this until
                # commentingOn is null
                # question: make a dictionary in place of simply a comment?
            pass

def index(request):
    """
    first view (home page) - move login to own view?
    """
    # checks if any form data has been submitted
    if request.POST:
        # checks if the form submitted is the login form (by checking for username input)
        if 'inputUsername' in request.POST.keys():
            # attempt authentication of login info
            user = authenticate(username=request.POST['inputUsername'],
                password=request.POST['inputPassword'])
            if user is not None:
                # if the user exists, then log in the user
                login(request, user)
            else:
                # go on to the next check
                pass
        # checks if the form submitted is the logout form
        elif 'logout' in request.POST.keys():
            # kill the section
            logout(request)

    # sets loggedIn variable to be used in HTML
    if request.user.is_authenticated:
        loggedIn = True
    else:
        loggedIn = False

    # # gets all posts and comments from the respective models
    allposts = Post.objects.order_by('-pub_date')
    allcomments = Comment.objects.order_by('-pub_date')
    for post in allposts:
        print(Comment.objects.filter(post = post))

    # START OF TRAIL AND ERROR

    # allPosts = Post.objects.all()
    # postList = []
    # for post in allPosts:
    #     postDict = {}
    #     postDict['post'] = post
    #
    #     comments = Comment.objects.filter(post = post)
    #     postDict['comments'] = comments
    #     postList.append(postDict)
    postList = []
    for post in allposts:
        postDict = getPostDict(post)
        postList.append(postDict)

    # END OF TRIAL AND ERROR

    # creates json
    context = {
        'allposts': allposts,
        'allcomments': allcomments,
        'loggedIn': loggedIn,
        'user': request.user
        }

    return render(request, 'polls/index.html', context)

def profile(request):
    """
    for the user profile (profile page) -> for login=true only
    """
    context = {}
    return render(request, 'polls/profile.html', context)
