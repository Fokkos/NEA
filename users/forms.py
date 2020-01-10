from django import forms #Library used for form specific commands
from django.contrib.auth.models import User #Imports the user information
from django.contrib.auth.forms import UserCreationForm #Imports the form that I wish to inherit off of
from .models import Profile
class RegistrationForm(UserCreationForm): #The new registration form that includes email!
    email=forms.EmailField(required=True) #Specifies that a valid email address must be entered, and the field is not optional

    class Meta:
        model=User #Defines the model that will be affected by this change, which is the User model
        fields=["username","email","password1","password2"] #defines the fields that will appear in the form and the order they appear in
                                                            #password1 is the initial password input and password2 is the check that theyre the same

class updateUser(forms.ModelForm): #The new registration form that includes email!
    email=forms.EmailField() #Specifies that a valid email address must be entered, and the field is not optional
    class Meta:
        model=User #Defines the model that will be affected by this change, which is the User model
        fields=["username","email"] #defines the fields that will appear in the form and the order they appear in

class updateProdile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["description","pfp"]