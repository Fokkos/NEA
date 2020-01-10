#Views made specifically for routines and templates regarding user settings (creation, login etc)
#Render is used for rendering templates
#Redirect is used for redirecting users back to the homepage when an account is created
from django.shortcuts import render, redirect
from .forms import RegistrationForm, updateUser, updateProfile #Custom forms defined in forms.py
from django.contrib import messages #Used for flash messages in register
from django.contrib.auth.decorators import login_required #Ensures that a user must be logged in to access some pages.


def register(request): #Handles the user registration form and ensures that the premade Django form loads correctly
    if request.method == "POST":
        form = RegistrationForm(request.POST) #If POST, return the form with the data in the form already!
        if form.is_valid():
            form.save() #Saves the information that the form collected into the User model 
            #f string below is used to format the text "account created" as a string.
            messages.success(request, f"account created!") #Upon success, return back message verifying the creation of the account!
            return redirect("index") #Once an account has been created, the user is redirected back to the index page
    else:
        form = RegistrationForm() #Sends off the UserCreation form as a blank for user to enter data into.
    return render(request, 'users/register.html', {'form':form}) #Registers the UserCreationForm as a form and sends it to the. register template

@login_required #Means that to access this view, user must be logged in.
def profile(request): #Handles the generation of a user profile page
    if request.method == "POST": #If the view is loaded via the submit button, do the following
        userForm = updateUser(request.POST, instance=request.user) #Loads the user form and fills with data from the POST
        profileForm = updateProfile(request.POST, request.FILES, instance=request.user.profile) #FILES is used to access pfp file
        if userForm.is_valid and profileForm.is_valid: #Checks to see if the input data is valid or not
            userForm.save() #Saves the User model
            profileForm.save() #Saves changes to the Profile model
            messages.success(request, f"changes saved!") #Lets user know their changes have been saved to the model
            return redirect("profile") #Reloads page with GET method and fills form with updated info
    else:
        userForm = updateUser(instance=request.user)
        profileForm = updateProfile(instance=request.user.profile)
    context={"userForm" : userForm, "profileForm" : profileForm} #Context sent is the two forms
    return render (request, "users/profile.html", context) #renders the tenplate "profile.html"
