from django.db import models
from django.contrib.auth.models import User #Imports the user model
# Create your models here.

class Profile(models.Model): #Defines the model that extends the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Defines a one-to-one model with User
    pfp = models.ImageField(default='media/pfps/default.png', upload_to='media/pfps') #Define field that will hold profile pictures

    def __str__(self): #Defines what gets displayed when a Profile is displayed (customises)
        return f'{self.user.username} \'s Profile' #Prints "username"'s profile
    
