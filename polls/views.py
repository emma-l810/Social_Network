from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post, Comment
from django.contrib.auth import authenticate, login, logout

# to print pretty dictionaries
from pprint import pprint

# Create your views here.

# new function that creates an object in the dictionary (refer back to screenshot)
    # look for root posts if there are any comments, and get those comments, and look
    # to check if each comment has any subcomments
def getComment(comment):
    allcomments = []
    subComments = Comment.objects.filter(commentingOn = comment)

    if subComments:
<<<<<<< HEAD
        layeredComments = []
=======
>>>>>>> 96773816dec7f03cfcc0a225758c4880d22d0f37
        return True
    else:
        return False

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

    # START OF TRAIL AND ERROR

    #loop through the posts

    alldata = []    # combined list including posts and their attributes + comments
    for post in allposts:
        postDict = {}
        # add attributes of each post into dictionary postDict
        postDict['user'] = post.user
        postDict['text'] = post.text
        postDict['pub_date'] = post.pub_date

        print("pre")
        pprint(postDict)

        postCommentsList = []   # to house all the comments of the post plus subcomments
        # filters out all the commentingOn comments --> will be filtered in in getComment()
        postComments = Comment.objects.filter(post=post, commentingOn__isnull = True)
        pprint(postComments)

        for comment in postComments: # loops through the postComments queryset
            # appends the list of subcomments (and their subcomments) for each comment
            # into the postCommentsList
            pprint(comment.text)
            postCommentsList.append(getComment(comment))

        postDict['comments'] = postCommentsList
        print("post")
        pprint(postDict)

    # END OF TRIAL AND ERROR

    # creates json objects with context
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
