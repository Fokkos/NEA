from django.db import models
from django.conf import settings
from django.contrib.auth.models import User #Imports the user model
from django.dispatch import receiver #Imports the signal reciever, used to initiate functions upon a certaon signal
from django.db.models.signals import post_save #Signal sent at the end of a save() in order to save the files
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.

class Profile(models.Model): #Defines the model that extends the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Defines a one-to-one model with User
    pfp = models.ImageField(default='media/pfps/default.png', upload_to='media/pfps') #Define field that will hold profile pictures
    description = models.TextField(max_length=70, default="", blank=True) #User Profile description
    history = models.CharField(validators=[validate_comma_separated_integer_list], max_length=250, default ='')
    
    def __str__(self): #Defines how the titles of each profile is shown in the admin view
        return f'{self.user.username}\'s Profile'

class Follow(models.Model): #Model created to manage the follow system for the project
    users = models.ManyToManyField(User, blank=True) #Established MtM relationship so that many users can be followed by a user
    current_user = models.OneToOneField(User, related_name="owner", on_delete=models.CASCADE,) #Each user can have one follow model

    @classmethod
    def follow(cls, current_user, following): #Defines how users are added to a follow list
        follower, created = cls.objects.get_or_create( #If user already has a follower list, one is made. otehrwise their already existing list is imported
            current_user=current_user) #Sets the current user as... the current user lol
        follower.users.add(following) #Adds user referred to as the second arg to the current users follow list
    
    @classmethod
    def unfollow(cls, current_user, following): #Defines how users are removed from a follow list
        follower, created = cls.objects.get_or_create( #If user already has a follower list, one is made. otehrwise their already existing list is imported
            current_user=current_user)  #Sets the current user as... the current user lol
        follower.users.remove(following) #Removes user referred to as the second arg from the current users follow list

    def __str__(self):
        return f'{self.current_user.username}\'s following list'
    


@receiver(post_save, sender=User) #When User model is saved, the following function happens
def create_profile(sender, **kwargs): #Defines function that creates a profile if one doesnt already exist
    if kwargs.get('created', False): #If a Profile has not been created already, do the following
        Profile.objects.get_or_create(user=kwargs.get('instance')) #Creates a profile linked to the current instance
        Follow.objects.get_or_create(current_user=kwargs.get('instance')) #Creates a profile linked to the current instance


