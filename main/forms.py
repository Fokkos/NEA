from django import forms #Library used for form specific commands
from django.contrib.auth.models import User #Imports the user information
from .models import Comment

class CommentForm(forms.ModelForm): #The new registration form that includes email!
    class Meta:
        model=Comment #Defines the model that will be affected by this change, which is the User model
        fields=["content"]