#Views made specifically for routines and templates regarding user settings (creation, login etc)
#Render is used for rendering templates
#Redirect is used for redirecting users back to the homepage when an account is created
from django.shortcuts import (
    render,  #Used to render templates for function based views
    redirect, #Used to redirect users to a specific page once a function has finished
    get_object_or_404 #Used to render custom 404 pages
)
from main.models import Post
from .forms import (
    RegistrationForm, #Custom made user registration form
    updateUser,  #Form made to update the User model
    updateProfile, #Form made to update the Profile model
)
from django.contrib import messages #Used for flash messages in register
from django.contrib.auth.decorators import login_required #Ensures that a user must be logged in to access some pages.
from .models import (
    Profile,  #Add-on to User model, adds pfp and description fields
    Follow,
)
from django.contrib.auth.models import User #Imports the user model


def register(request): #Handles the user registration form and ensures that the premade Django form loads correctly
    if request.method == "POST":
        form = RegistrationForm(request.POST) #If POST, return the form with the data in the form already!
        if form.is_valid():
            form.save() #Saves the information that the form collected into the User model 
            #f string below is used to format the text "account created" as a string.
            messages.success(request, f"account created!") #Upon success, return back message verifying the creation of the account!
            return redirect("feed") #Once an account has been created, the user is redirected back to the index page
    else:
        form = RegistrationForm() #Sends off the UserCreation form as a blank for user to enter data into.
    return render(request, 'users/register.html', {'form':form}) #Registers the UserCreationForm as a form and sends it to the. register template

# def follow(request):


@login_required #Means that to access this view, user must be logged in.
def profile(request): #Handles the generation of a user profile page
    if request.method == "POST": #If the view is loaded via the submit button, do the following
        userForm = updateUser(request.POST, instance=request.user) #Loads the user form and fills with data from the POST
        profileForm = updateProfile(request.POST, request.FILES, instance=request.user.profile) #FILES is used to access pfp file
        if userForm.is_valid and profileForm.is_valid: #Checks to see if the input data is valid or not
            userForm.save() #Saves the User model
            try: #If the file is an image file
                profileForm.save() #Saves changes to the Profile model
                messages.success(request, f"changes saved!") #Lets user know their changes have been saved to the model
            except: #Otherwise...
                messages.warning(request, f"pfp filetype not correct") #Lets user know their changes have not been saved
            return redirect("profile") #Reloads page with GET method and fills form with updated info
    else: #Upon first generation of the page...
        userForm = updateUser(instance=request.user) 
        profileForm = updateProfile(instance=request.user.profile)
    context={"userForm" : userForm, "profileForm" : profileForm} #Context sent is the two forms
    return render (request, "users/profile.html", context) #renders the tenplate "profile.html"



@login_required #Means that to access this view, user must be logged in.
def manage_follow(request, operation, username): #Manages a users follow list, adding and removing users
    following = User.objects.get(username=username) #User that is added/removed from list is the User with matching username
    if operation == "add": #If url has "add/"...
        Follow.follow(request.user, following) #Redirects to follow classmethod in model
    elif operation == "remove": #If url has "remove/"...
        Follow.unfollow(request.user, following) #Redirects to unfollow classmethod in model
    return redirect("following") #Redirects user to page that lists who they are following

@login_required #Means that to access this view, user must be logged in.
def followerList(request): #Defined a page that lists all of the users the logged in user is following
    following = Follow.objects.get(current_user=request.user) #Defines the user whos Follow object will be accessed
    followList = following.users.all() #Attributes the list of the users followed accounts to variable "following"
    args = { "following": followList} #Sets the arguments for the following page (list of followers)
    return render(request,"users/following.html", args) #Renders template that displays list of followed users