from django.db import models
from django.conf import settings
from django.contrib.auth.models import User #Imports the user model
from django.dispatch import receiver #Imports the signal reciever, used to initiate functions upon a certaon signal
from django.db.models.signals import post_save #Signal sent at the end of a save() in order to save the files
from annoying.fields import AutoOneToOneField
# Create your models here.

class Profile(models.Model): #Defines the model that extends the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Defines a one-to-one model with User
    pfp = models.ImageField(default='media/pfps/default.png', upload_to='media/pfps') #Define field that will hold profile pictures
    description = models.TextField(max_length=200, default="", blank=True) #User Profile description
    
    def __str__(self): #Defines how the titles of each profile is shown in the admin view
        return f'{self.user.username}\'s Profile'

class Follow(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE, null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)
    
    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)

    def __str__(self):
        return f'{self.current_user.username}\'s following list'
    


@receiver(post_save, sender=User) #When User model is saved, the following function happens
def create_profile(sender, **kwargs): #Defines function that creates a profile if one doesnt already exist
    if kwargs.get('created', False): #If a Profile has not been created already, do the following
        Profile.objects.get_or_create(user=kwargs.get('instance')) #Creates a profile linked to the current instance


