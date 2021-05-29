from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post, Comment
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

# to print pretty dictionaries
from pprint import pprint

# Create your views here.

# new function that creates an object in the dictionary (refer back to screenshot)
    # look for root posts if there are any comments, and get those comments, and look
    # to check if each comment has any subcomments
def getComment(comment):
    """
    recursive function - retrieves a list of list of list of comments
    """
    # creates new comment dictionary to contain all the subcomments for each base comment
    commentDict = {}
    commentDict['text'] = comment.text  # adds other attributes to the commentDict
    commentDict['likes'] = comment.likes
    commentDict['pub_date'] = comment.pub_date

    # collects subcomments with attribute commentingOn being not null
    subComments = Comment.objects.filter(commentingOn = comment)

    # recursive statement -> loops through the loop until the
    if subComments:
        layeredComments = []
        for subComment in subComments:
            subCommentDict = getComment(subComment)

            layeredComments.append(subCommentDict)
            # pprint(layeredComments)
        commentDict['subcomments'] = layeredComments

    # print("commentDict")
    # pprint(commentDict)
    return commentDict

# default home page view
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

    alldata = []    # combined list including posts and their attributes + comments
    for post in allposts:
        postDict = {}
        # add attributes of each post into dictionary postDict
        postDict['user'] = post.user
        postDict['text'] = post.text
        postDict['likes'] = post.likes
        postDict['pub_date'] = post.pub_date

        # print("\npre")
        # pprint(postDict)

        postCommentsList = []   # to house all the comments of the post plus subcomments
        # filters out all the commentingOn comments --> will be filtered in in getComment()
        postComments = Comment.objects.filter(post=post, commentingOn__isnull = True)
        # pprint(postComments)

        for comment in postComments: # loops through the postComments queryset
            # appends the list of subcomments (and their subcomments) for each comment
            # into the postCommentsList
            if not comment.commentingOn:
                postCommentsList.append(getComment(comment))

        postDict['comments'] = postCommentsList
        # print("\npost")
        # pprint(postDict)
        alldata.append(postDict)

    pprint(alldata)

    # creates json objects with context
    context = {
        'alldata': alldata,
        'loggedIn': loggedIn,
        'user': request.user
        }

    return render(request, 'polls/index.html', context)

def profile(request, username):
    """
    for the user profile (profile page) -> for login=true only
    """
    # not really sure what the id is --> ASK?
    thisUser = User.objects.filter(id=id)
    userPosts = Post.objects.filter(user=username)  # get all posts by user
    recentPosts = userPosts.order_by('-pub_date')[:6]   # gets the five most recent posts
    context = {
        'user': user,
        'recentPosts': recentPosts
    }
    return render(request, 'polls/profile.html', context)

def post(request):
    """
    for the create new post tab -> allows the user to create a new post separate
    from the index.html template page
    """
    # entering data and saving it --> need to put it in the request.POST
    if request.POST:
        if 'postNew' in request.POST.keys():
            newPost = Post(
                text = request.POST['postNew'],
                user = request.user,
                pub_date = timezone.now(),
            )
            newPost.save()
        print("saved")
    context = {}
    return render(request, 'polls/post.html', context)
