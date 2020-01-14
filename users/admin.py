from django.contrib import admin
from .models import Profile, Follow

#Registers classes into the admin site and allows for them to be edited
admin.site.register(Profile) 
admin.site.register(Follow)
